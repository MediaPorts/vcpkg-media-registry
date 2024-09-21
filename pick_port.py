import argparse
import collections
import configparser
import copy
import inspect
import json
import logging
import re
import os
import subprocess


# my branch name
MY_BRANCH = 'main'
# microsoft/vcpkg -> my temp branch
MSFT_BRANCH = 'msft'

# default microsoft/vcpkg git repo url
MICROSOFT_VCPKG_URL = 'https://github.com/microsoft/vcpkg.git'
# default microsoft/vcpkg branch
MICROSOFT_VCPKG_BRANCH = 'master'
# default microsoft/vcpkg commit hash
MICROSOFT_VCPKG_BASELINE = '98aa6396292d57e737a6ef999d4225ca488859d5'

# default timezone
RUN_GIT_ENV = {'TZ': 'Asia/Shanghai'}


# git commit information
GitCommitInfo = collections.namedtuple(
    'GitCommitInfo',
    (
        'hash',
        'datetime'
    )
)

# command line arguments
CliArgs = collections.namedtuple(
    'CliArgs',
    (
        'msft_vcpkg_url',
        'msft_vcpkg_branch',
        'msft_vcpkg_baseline',
        'my_vcpkg_branch',
        'pick_port'
    )
)


# configure stdout logger
def setup_logger():
    class ColoredFormatter(logging.Formatter):
        class Color:
            INFO = "\033[94m"  # Light Blue
            WARNING = "\033[93m"  # Yellow
            ERROR = "\033[91m"  # Red
            RESET = "\033[0m"  # Reset to default

        def format(self, record):
            if record.levelno >= logging.ERROR:
                record.msg = f"{self.Color.ERROR}{record.msg}{self.Color.RESET}"
            elif record.levelno >= logging.WARNING:
                record.msg = f"{self.Color.WARNING}{record.msg}{self.Color.RESET}"
            else:
                record.msg = f"{self.Color.INFO}{record.msg}{self.Color.RESET}"
            
            return super().format(record)
        
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = ColoredFormatter('%(asctime)s - %(lineno)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)


# parse command line arguments
def parse_cli_args() -> CliArgs:
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

    return CliArgs(
        msft_vcpkg_url=args.msft_vcpkg_url, msft_vcpkg_branch=args.msft_vcpkg_branch,
        msft_vcpkg_baseline=args.msft_vcpkg_baseline, my_vcpkg_branch=args.my_vcpkg_branch, pick_port=args.pick_port
    )


# run command lines
def shell(args, silent=False, **kwargs):
    if not silent:
        logging.info('run: %s', ' '.join(args))
    return subprocess.run(args=args, **kwargs)


# build vpckg paths
class VcpkgPathBuilder:
    def __init__(self):
        self._vcpkg_json_name = 'vcpkg.json'
        self._ports_dir_name = 'ports'
        self._versions_dir_name = 'versions'
        self._baseline_json_name = 'baseline.json'

    # ports/
    def ports(self) -> str:
        return f'{self._ports_dir_name}'

    # ports/{name}
    def port(self, port) -> str:
        return f'{self._ports_dir_name}/{port}'

    # ports/{name}/vcpkg.json
    def vcpkg_json(self, port: str) -> str:
        return f'{self._ports_dir_name}/{port}/{self._vcpkg_json_name}'

    # versions/{prefix}-/{name}.json
    def versions_json(self, port: str) -> str:
        return f'{self._versions_dir_name}/{port[:1]}-/{port}.json'

    # versions/baseline.json
    def baseline_json(self) -> str:
        return f'{self._versions_dir_name}/{self._baseline_json_name}'


# parse vcpkg port's relationships
class VcpkgDataParser:
    def __init__(self, path_builder: VcpkgPathBuilder):
        self._path_builder = path_builder

    # find port's dependencies including self
    def find_necessary(self, port: str) -> set:
        results = set()
        results.add(port)

        self._find_necessary(port=port, results=results)

        logging.warning(
            '%s has %d necessary ports: %s',
            port, len(results), json.dumps(list(sorted(results)))
        )

        return results

    # find port's dependencies
    def _find_necessary(self, port: str, results: set):
        path = self._path_builder.vcpkg_json(port)
        if not os.path.exists(path) or not os.path.isfile(path):
            logging.error('%s not found', path)
            return

        old = copy.deepcopy(results)

        with open(path) as f:
            data = json.load(f)
            # direct dependencies
            for dep in data.get('dependencies', []):
                results.add(dep if isinstance(dep, str) else dep['name'])
            # features' dependencies
            for (_, feature_deps) in data.get('features', {}).items():
                for dep in feature_deps.get('dependencies', []):
                    results.add(dep if isinstance(dep, str) else dep['name'])

        # recurse
        update = results - old
        for dep in update:
            self._find_necessary(port=dep, results=results)


# parse git commit information
class VcpkgGitParser:
    def __init__(self, path_builder: VcpkgPathBuilder):
        self._path_builder = path_builder

    # get commits' info ordered by commit datetime
    def find_ordered_necessary_commits(self, ports: set) -> list:
        results = set()

        for port in ports:
            results.add(self.get_commit_info(path=self._path_builder.port(port)))
            results.add(self.get_commit_info(path=self._path_builder.versions_json(port)))

        return list(sorted(results, key=lambda t: t.datetime))
        
    # get git commit hash and datetime
    def get_commit_info(self, path: str) -> GitCommitInfo:
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

        return GitCommitInfo(hash=commit_hash, datetime=commit_datetime)
    

# git cherry-pick and auto fix conflicts
class VcpkgGitPicker:
    def __init__(self, args: CliArgs):
        self._args = args
        self._path_builder = VcpkgPathBuilder()
        self._data_parser = VcpkgDataParser(self._path_builder)
        self._git_parser = VcpkgGitParser(self._path_builder)

    # add microsoft/vcpkg to git remote and check a branch from its branch 
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

    # find port from output text
    def find_port(self, output) -> str:
        for line in output.split('\n'):
            if not re.search(r'(\S+)\s+\|\s+(\d+)\s+([\+\-]+)', line):
                continue
            matches = re.search(r'ports/(.*)/', output)
            if not matches:
                matches = re.search(r'versions/[0-1a-z]-/(.*)\.json', output)
            if matches:
                return matches.group(1)
        return ''
    
    # auto fix conflicts
    def fix_conflicts(self, my_versions, msft_versions, port, output):
        # def is_port_files(port, line) -> bool:
        #     return any((
        #         self._path_builder.baseline_json() in line,
        #         self._path_builder.versions_json(port) in line,
        #         line.startswith(self._path_builder.port(port))
        #     ))

        my_versions[port] = msft_versions[port]
        with open(self._path_builder.baseline_json(), 'w') as f:
            json.dump({'default': my_versions}, f, sort_keys=True, indent=4)
        
        # adds = [self._path_builder.baseline_json()]
        # removes = []
        if 'CONFLICT' in output:
            shell(args=['git', 'add', '.'])
            shell(args=['git', 'cherry-pick', '--continue'])
        #     stdout = shell(args=['git', 'status'], stdout=subprocess.PIPE, text=True).stdout.strip()
        #     for line in stdout.split('\n'):
        #         if 'deleted' in line or 'modified' in line:
        #             path = line.partition(':')[-1].strip()
        #             if is_port_files(port, path):
        #                 adds.append(path)
        #             else:
        #                 removes.append(path)

        # if len(removes) > 0:
        #     args = ['git', 'rm']
        #     args += removes
        #     shell(args)
        # if len(adds) > 0:
        #     args = ['git', 'add']
        #     args += adds
        #     shell(args)
        # if len(removes) > 0 or len(adds) > 0:
        #     shell(args=['git', 'cherry-pick', '--continue'])

    # cherry-pick and fix conflicts
    def cherry_pick(self):
        necessary_ports = self._data_parser.find_necessary(self._args.pick_port)
        necessary_commits = self._git_parser.find_ordered_necessary_commits(necessary_ports)

        # read microsoft/vcpkg baseline versions
        with open(self._path_builder.baseline_json()) as f:
            msft_versions = json.load(f)['default']
        
        shell(args=['git', 'checkout', self._args.my_vcpkg_branch])

        # read my vcpkg baseline versions
        with open(self._path_builder.baseline_json()) as f:
            my_versions = json.load(f)['default']

        # cherry-pick commit by commit
        for commit in necessary_commits:
            info = shell(
                silent=True, env=RUN_GIT_ENV, stdout=subprocess.PIPE, text=True,
                args=['git', 'log', '-1', '--stat', '--date=iso', commit.hash]
            ).stdout

            port = self.find_port(output=info)
            logging.info('%s\n%s', port, info)

            sh = shell(args=['git', 'cherry-pick', commit.hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = f'{sh.stdout.strip()}\n{sh.stderr.strip()}'
            self.fix_conflicts(my_versions, msft_versions, port, output)


# main entry
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


# entry point
if __name__ == '__main__':
    main()
