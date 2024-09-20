import argparse
import inspect
import json
import logging
import os
import shutil
import subprocess



VCPKG_JSON = 'vcpkg.json'

MY_VCPKG_PORTS_DIR = 'ports'
MY_VCPKG_VERSIONS_DIR = 'versions'
MY_VCPKG_VERSIONS_BASELINE_JSON = f'{MY_VCPKG_VERSIONS_DIR}/baseline.json'

MICROSOFT_VCPKG_ROOT_DIR = 'downloads/vcpkg'
MICROSOFT_VCPKG_URL = 'https://github.com/microsoft/vcpkg.git'
MICROSOFT_VCPKG_BRANCH = 'master'
MICROSOFT_VCPKG_BASELINE = '91f002cae2281636da5155efc5a11d67efa72415'
MICROSOFT_VCPKG_PORTS_DIR = f'{MICROSOFT_VCPKG_ROOT_DIR}/{MY_VCPKG_PORTS_DIR}'
MICROSOFT_VCPKG_VERSIONS_DIR = f'{MICROSOFT_VCPKG_ROOT_DIR}/{MY_VCPKG_VERSIONS_DIR}'
MICROSOFT_VCPKG_VERSIONS_BASELINE_JSON = f'{MICROSOFT_VCPKG_ROOT_DIR}/{MY_VCPKG_VERSIONS_BASELINE_JSON}'

EXIST_PORTS = set()


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


def parse_cli_args() -> str:
    logging.info(inspect.currentframe().f_code.co_name)

    arg_parser = argparse.ArgumentParser(description="pick port from microsoft vcpkg")
    
    arg_parser.add_argument(
        '--port', 
        type=str, 
        help=f'port name'
    )

    args = arg_parser.parse_args()
    return args.port


def shell(args, **kwargs):
    logging.info('run: %s', ' '.join(args))
    return subprocess.run(args=args, **kwargs)


def update_github_microsoft_vcpkg():
    logging.info(inspect.currentframe().f_code.co_name)

    cwd = os.getcwd()

    os.makedirs(os.path.dirname(MICROSOFT_VCPKG_ROOT_DIR), exist_ok=True)
    if not os.path.exists(MICROSOFT_VCPKG_ROOT_DIR):
        # clone
        shell(args=['git', 'clone', MICROSOFT_VCPKG_URL, MICROSOFT_VCPKG_ROOT_DIR])
        os.chdir(MICROSOFT_VCPKG_ROOT_DIR)
    else:
        # fetch
        os.chdir(MICROSOFT_VCPKG_ROOT_DIR)
        shell(args=['git', 'fetch'])

    # switch branch
    current_branch = shell(args=['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, text=True).stdout.strip()
    if MICROSOFT_VCPKG_BRANCH != current_branch:
        shell(args=['git', 'checkout', MICROSOFT_VCPKG_BRANCH])

    # reset
    git_status = shell(args=['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True).stdout.strip()
    if git_status != '':
        shell(args=['git', 'stash'])
    shell(args=['git', 'reset', '--hard', MICROSOFT_VCPKG_BASELINE])
    if git_status != '':
        shell(args=['git', 'stash', 'pop'])

    os.chdir(cwd)


def pick_sub_port(port, commit=False):
    # pick dependencies
    with open(f'{MICROSOFT_VCPKG_PORTS_DIR}/{port}/{VCPKG_JSON}') as f:
        for dep in json.load(f).get('dependencies', []):
            name = dep if isinstance(dep, str) else dep['name']
            if name in EXIST_PORTS:
                return
            pick_sub_port(name)
        
    # skip exists
    if port in EXIST_PORTS:
        return
    if os.path.exists(f'{MY_VCPKG_PORTS_DIR}/{port}/{VCPKG_JSON}'):
        EXIST_PORTS.add(port)
        return

    logging.info('%s(%s)', inspect.currentframe().f_code.co_name, port)

    # pick port's version in baseline from microsoft vcpkg
    version = {}
    with open(MICROSOFT_VCPKG_VERSIONS_BASELINE_JSON) as f:
        for (k, v) in json.load(f)['default'].items():
            if k == port:
                version = v

    if len(version) == 0:
        logging.error('%s was not found in %s', port, MICROSOFT_VCPKG_VERSIONS_BASELINE_JSON)

    # update port's version in baseline to my vcpkg
    with open(MY_VCPKG_VERSIONS_BASELINE_JSON) as f:
        data = json.load(f)
    with open(MY_VCPKG_VERSIONS_BASELINE_JSON, mode='w') as f:
        data['default'][port] = version
        json.dump(data, f, indent=4, ensure_ascii=True, sort_keys=True)

    # copy port's data
    if os.path.exists(f'{MY_VCPKG_PORTS_DIR}/{port}'):
        shutil.rmtree(f'{MY_VCPKG_PORTS_DIR}/{port}')
    shutil.copytree(f'{MICROSOFT_VCPKG_PORTS_DIR}/{port}', f'{MY_VCPKG_PORTS_DIR}/{port}')

    # copy port's version
    prefix = f'{port[:1]}-'
    os.makedirs(f'{MY_VCPKG_VERSIONS_DIR}/{prefix}', exist_ok=True)
    shutil.copyfile(f'{MICROSOFT_VCPKG_VERSIONS_DIR}/{prefix}/{port}.json', f'{MY_VCPKG_VERSIONS_DIR}/{prefix}/{port}.json')

    if commit:
        # pick port's git commit message
        cwd = os.getcwd()
        os.chdir(f'{MICROSOFT_VCPKG_PORTS_DIR}/{port}')
        commit_message = shell(args=['git', 'log', '-1', '--pretty=%s', '--', '.'], stdout=subprocess.PIPE, text=True).stdout.strip()
        os.chdir(cwd)
        shell(args=['git', 'add', '-f', f'{MY_VCPKG_PORTS_DIR}/{port}/*', MY_VCPKG_VERSIONS_BASELINE_JSON, f'{MY_VCPKG_VERSIONS_DIR}/{prefix}/{port}.json'])
        shell(args=['git', 'commit', '-m', commit_message])


def pick_port_microsoft_vcpkg(port):
    prefix = f'{port[:1]}-'

    # like boost
    if port.endswith('*'):
        for name in os.listdir(MICROSOFT_VCPKG_PORTS_DIR):
            pick_sub_port(name, False)
            shell(args=['git', 'add', '-f', f'{MY_VCPKG_PORTS_DIR}/{port}/*', MY_VCPKG_VERSIONS_BASELINE_JSON, f'{MY_VCPKG_VERSIONS_DIR}/{prefix}/{port}.json'])
        # pick port's git commit message
        cwd = os.getcwd()
        os.chdir(f'{MICROSOFT_VCPKG_PORTS_DIR}/{port.rstrip("*")}')
        commit_message = shell(args=['git', 'log', '-1', '--pretty=%s', '--', '.'], stdout=subprocess.PIPE, text=True).stdout.strip()
        os.chdir(cwd)
        shell(args=['git', 'commit', '-m', commit_message])

    # pick
    pick_sub_port(port, True)


def main():
    setup_logger()
    
    port = parse_cli_args()
    if port == '':
        return

    update_github_microsoft_vcpkg()

    pick_port_microsoft_vcpkg(port)


if __name__ == '__main__':
    main()
