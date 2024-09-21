import argparse
import collections
import configparser
import copy
import inspect
import json
import logging
import os
import subprocess


MY_BRANCH = 'main'
MSFT_BRANCH = 'msft'

MICROSOFT_VCPKG_URL = 'https://github.com/microsoft/vcpkg.git'
MICROSOFT_VCPKG_BRANCH = 'master'
MICROSOFT_VCPKG_BASELINE = '91f002cae2281636da5155efc5a11d67efa72415'

RUN_GIT_ENV = {'TZ': 'Asia/Shanghai'}

EXIST_COMMITS = set()


git_commit_info_data = collections.namedtuple(
    'get_commit_info',
    (
        'hash',
        'datetime'
    )
)


cli_args = collections.namedtuple(
    'cli_args',
    (
        'msft_vcpkg_url',
        'msft_vcpkg_branch',
        'msft_vcpkg_baseline',
        'my_vcpkg_branch',
        'pick_port'
    )
)


def setup_logger():
    class ColoredFormatter(logging.Formatter):
        class Color:
            INFO = "\033[94m"  # Light Blue
            WARNING = "\033[93m"  # Yellow
            ERROR = "\033[91m"  # Red
            RESET = "\033[0m"  # Reset to default

        def format(self, record):
            if record.levelno == logging.INFO:
                record.msg = f"{self.Color.INFO}{record.msg}{self.Color.RESET}"
            elif record.levelno == logging.WARNING:
                record.msg = f"{self.Color.WARNING}{record.msg}{self.Color.RESET}"
            elif record.levelno == logging.ERROR:
                record.msg = f"{self.Color.ERROR}{record.msg}{self.Color.RESET}"
            return super().format(record)
        
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = ColoredFormatter('%(asctime)s - %(lineno)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def parse_cli_args() -> cli_args:
    logging.info(inspect.currentframe().f_code.co_name)

    arg_parser = argparse.ArgumentParser(description="pick port from microsoft/vcpkg")
        
    arg_parser.add_argument(
        '--msft-vcpkg-url',
        type=str,
        default=MICROSOFT_VCPKG_URL,
        help=f'microsoft/vcpkg git url (default: {MICROSOFT_VCPKG_URL})'
    )

    arg_parser.add_argument(
        '--msft-vcpkg-branch',
        type=str,
        default=MICROSOFT_VCPKG_BRANCH,
        help=f'microsoft/vcpkg git branch (default: {MICROSOFT_VCPKG_BRANCH})'
    )

    arg_parser.add_argument(
        '--msft-vcpkg-baseline',
        type=str,
        default=MICROSOFT_VCPKG_BASELINE,
        help=f'microsoft/vcpkg git baseline (default: {MICROSOFT_VCPKG_BASELINE})'
    )

    arg_parser.add_argument(
        '--my-vcpkg-branch',
        type=str,
        default=MY_BRANCH,
        help=f'my vcpkg git branch (default: {MY_BRANCH})'
    )

    arg_parser.add_argument(
        '--pick-port',
        type=str,
        help=f'port name to pick from microsoft/vcpkg'
    )

    args = arg_parser.parse_args()

    return cli_args(
        msft_vcpkg_url=args.msft_vcpkg_url, msft_vcpkg_branch=args.msft_vcpkg_branch,
        msft_vcpkg_baseline=args.msft_vcpkg_baseline, my_vcpkg_branch=args.my_vcpkg_branch, pick_port=args.pick_port
    )


def shell(args, silent=False, **kwargs):
    if not silent:
        logging.info('run: %s', ' '.join(args))
    return subprocess.run(args=args, **kwargs)


class VcpkgPathBuilder:
    def __init__(self):
        self._vcpkg_json_name = 'vcpkg.json'
        self._ports_dir_name = 'ports'
        self._versions_dir_name = 'versions'
        self._baseline_json_name = 'baseline.json'

    def ports(self) -> str:
        return f'{self._ports_dir_name}'

    def port(self, port) -> str:
        return f'{self._ports_dir_name}/{port}'

    def vcpkg_json(self, port: str) -> str:
        return f'{self._ports_dir_name}/{port}/{self._vcpkg_json_name}'

    def versions_json(self, port: str) -> str:
        return f'{self._versions_dir_name}/{port[:1]}-/{port}.json'

    def baseline_json(self) -> str:
        return f'{self._versions_dir_name}/{self._baseline_json_name}'


class VcpkgDataParser:
    def __init__(self, path_builder: VcpkgPathBuilder):
        self._path_builder = path_builder

    def find_necessary(self, port: str) -> set:
        results = set()
        results.add(port)

        self._find_necessary(port=port, results=results)

        logging.warning(
            '%s has %d necessary ports: %s',
            port, len(results), json.dumps(list(sorted(results)))
        )

        return results

    def _find_necessary(self, port: str, results: set):
        path = self._path_builder.vcpkg_json(port)
        if not os.path.exists(path) or not os.path.isfile(path):
            logging.error('%s not found', path)
            return

        old = copy.deepcopy(results)

        with open(path) as f:
            data = json.load(f)
            for dep in data.get('dependencies', []):
                results.add(dep if isinstance(dep, str) else dep['name'])
            for (_, feature_deps) in data.get('features', {}).items():
                for dep in feature_deps.get('dependencies', []):
                    results.add(dep if isinstance(dep, str) else dep['name'])

        update = results - old
        for dep in update:
            self._find_necessary(port=dep, results=results)



class VcpkgGitParser:
    def __init__(self, path_builder: VcpkgPathBuilder):
        self._path_builder = path_builder

    def find_ordered_necessary_commits(self, ports: set) -> list:
        results = set()

        for port in ports:
            results.add(self.get_commit_info(path=self._path_builder.port(port)))
            results.add(self.get_commit_info(path=self._path_builder.versions_json(port)))

        return list(sorted(results, key=lambda t: t.datetime))
        
    def get_commit_info(self, path: str) -> git_commit_info_data:
        cwd = os.getcwd()
        if os.path.isfile(path):
            os.chdir(os.path.dirname(path))
            target = os.path.basename(path)
        else:
            os.chdir(path)
            target = '.'

        commit_hash = shell(
            silent=True, stdout=subprocess.PIPE, text=True,
            args=['git', 'log', '-1', '--pretty=format:%H', target]
        ).stdout.strip()
        commit_datetime = shell(
            silent=True, env=RUN_GIT_ENV, stdout=subprocess.PIPE, text=True,
            args=['git', 'log', '-1', '--date=format:%Y-%m-%d %H:%M:%S', '--pretty=%ad', '--date=iso', target]
        ).stdout.strip()

        if cwd != os.getcwd():
            os.chdir(cwd)

        return git_commit_info_data(hash=commit_hash, datetime=commit_datetime)
    

class VcpkgGitPicker:
    def __init__(self, args: cli_args):
        self._args = args

    def update_msft(self):
        logging.info(inspect.currentframe().f_code.co_name)
        
        remote = MSFT_BRANCH
        branch = remote
        remote_msft_key = f'remote "{remote}"'
        branch_msft_key = f'branch "{branch}"'

        git_config = configparser.ConfigParser()
        git_config.read('.git/config')

        try:
            git_config[remote_msft_key]
        except Exception as _:
            shell(args=['git', 'remote', 'add', remote, self._args.msft_vcpkg_url])
            shell(args=['git', 'fetch', remote, self._args.msft_vcpkg_branch])

        try:
            git_config[branch_msft_key]
        except Exception as _:
            shell(args=['git', 'checkout', '-b', branch, f'{remote}/{self._args.msft_vcpkg_branch}'])
            shell(args=['git', 'reset', '--hard', self._args.msft_vcpkg_baseline])
        else:
            shell(args=['git', 'checkout', branch])

    def cherry_pick(self):
        msft_path_builder = VcpkgPathBuilder()
        msft_data_parser = VcpkgDataParser(msft_path_builder)
        msft_git_parser = VcpkgGitParser(msft_path_builder)

        necessary_ports = msft_data_parser.find_necessary(self._args.pick_port)
        necessary_commits = msft_git_parser.find_ordered_necessary_commits(necessary_ports)
        
        shell(args=['git', 'checkout', self._args.my_vcpkg_branch])

        for commit in necessary_commits:
            info = shell(
                silent=True, env=RUN_GIT_ENV, stdout=subprocess.PIPE, text=True,
                args=['git', 'log', '-1', '--stat', '--date=iso', commit.hash]
            ).stdout
            logging.info(info)

            shell(args=['git', 'cherry-pick', commit.hash])


def main():
    setup_logger()
    
    args = parse_cli_args()
    if args.pick_port == '':
        logging.error('please input port name with --pick-port option')
        return
    logging.info(args)

    picker = VcpkgGitPicker(args)
    picker.update_msft()
    picker.cherry_pick()


if __name__ == '__main__':
    main()
