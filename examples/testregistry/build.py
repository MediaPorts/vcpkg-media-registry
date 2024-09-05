import argparse
import collections
import inspect
import json
import logging
import os
import platform
import shutil
import subprocess


vcpkg_conf = collections.namedtuple('vcpkg_conf', ('repository', 'reference', 'baseline'))
cli_args = collections.namedtuple('cli_args', ('vcpkg_root_dir', 'vcpkg_bootstrap', 'vcpkg_triplet', 'cmake_generate', 'cmake_build', 'config'))



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


def default_triplet() -> str:
    os_name = platform.system()

    if os_name == 'Windows':
        return 'x64-windows'
    elif os_name == 'Darwin':
        return 'arm64-osx'
    elif os_name == 'Linux':
        return 'x64-linux-dynamic'
    else:
        logging.error('unsupport os: %s', os_name)
        return ''

def parse_cli_args() -> cli_args:
    logging.info(inspect.currentframe().f_code.co_name)

    invalid_result = cli_args('', '', '', '', '', '')

    arg_parser = argparse.ArgumentParser(description="vcpkg bootstrap/cmake generate/cmake build")
    
    default_vcpkg_root_dir = os.path.abspath('./vcpkg')
    arg_parser.add_argument(
        '--vcpkg-root-dir', 
        type=str, 
        default=default_vcpkg_root_dir, 
        help=f'set vcpkg root dir path (default {default_vcpkg_root_dir})'
    )

    default_triplet_ = default_triplet()
    if default_triplet_ == '':
        return invalid_result
    arg_parser.add_argument(
        '--vcpkg-triplet', 
        type=str, 
        default=default_triplet_, 
        help=f'set vcpkg triplet (default {default_triplet_})'
    )
    
    arg_parser.add_argument(
        '--vcpkg-bootstrap', 
        type=bool, 
        default=False, 
        help=f'fetch vcpkg and bootstrap it (default False)'
    )
    
    arg_parser.add_argument(
        '--cmake-generate', 
        type=bool, 
        default=False, 
        help=f'cmake generate build system (default False)'
    )
    
    arg_parser.add_argument(
        '--cmake-build', 
        type=bool, 
        default=False, 
        help=f'cmake build (default False)'
    )
    
    arg_parser.add_argument(
        '--config', 
        type=str, 
        default='Debug', 
        help=f'cmake build config (default Debug)'
    )

    args = arg_parser.parse_args()

    if not args.vcpkg_bootstrap and not args.cmake_generate and not args.cmake_build:
        arg_parser.print_help()
        return invalid_result

    return cli_args(
        vcpkg_root_dir=args.vcpkg_root_dir,
        vcpkg_bootstrap=args.vcpkg_bootstrap,
        vcpkg_triplet=args.vcpkg_triplet,
        cmake_generate=args.cmake_generate,
        cmake_build=args.cmake_build,
        config=args.config
    )
    

def parse_vcpkg_conf() -> vcpkg_conf:
    logging.info(inspect.currentframe().f_code.co_name)
    
    invalid_conf = vcpkg_conf('', '', '')

    conf_file = 'vcpkg-configuration.json'
    if not os.path.exists(conf_file) or not os.path.isfile(conf_file):
        return invalid_conf
    
    with open(conf_file) as f:
        try:
            data = json.load(f)
        except Exception as e:
            logging.error('read vcpkg-configuration.json error, exception: %s', str(e))
            return invalid_conf
        
        registry = data.get('default-registry', {})
        return vcpkg_conf(
            repository=registry.get('repository', ''),
            reference=registry.get('reference', ''),
            baseline=registry.get('baseline', ''),
        )


def shell(args, **kwargs):
    logging.info('run: %s', ' '.join(args))
    return subprocess.run(args=args, **kwargs)


def bootstrap_vcpkg(root_dir: str, conf: vcpkg_conf, triplet: str):
    logging.info(inspect.currentframe().f_code.co_name)

    cwd = os.getcwd()

    if not os.path.exists(root_dir):
        # clone
        shell(args=['git', 'clone', conf.repository, root_dir])
        os.chdir(root_dir)
    else:
        # fetch
        os.chdir(root_dir)
        shell(args=['git', 'fetch'])

    # switch branch
    current_branch = shell(args=['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, text=True).stdout.strip()
    if conf.reference != current_branch:
        shell(args=['git', 'checkout', conf.reference])

    # reset
    git_status = shell(args=['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True).stdout.strip()
    if git_status != '':
        shell(args=['git', 'stash'])
    shell(args=['git', 'reset', '--hard', conf.baseline])
    if git_status != '':
        shell(args=['git', 'stash', 'pop'])

    # bootstrap
    if triplet == 'arm64-osx':
        triplet = 'x64-arm64-osx'
    current_tool = 'vcpkg'
    prebuilt_tool = f'prebuilt/vcpkg.{triplet}'
    if platform.system() == 'Windows':
        current_tool += '.exe'
        prebuilt_tool += '.exe'
    prebuilt_tool = prebuilt_tool.replace('-static', '')
    prebuilt_tool = prebuilt_tool.replace('-dynamic', '')
    if not os.path.exists(current_tool):
        if os.path.exists(prebuilt_tool):
            shutil.copy(prebuilt_tool, current_tool)
        else:
            shell(args=['bootstrap-vcpkg.bat' if current_tool.endswith('.exe') else 'bootstrap-vcpkg.sh'])

    os.chdir(cwd)


def cmake_generate(vcpkg_root_dir: str, triplet: str):
    logging.info(inspect.currentframe().f_code.co_name)

    shell(args=[
        'cmake.exe' if 'windows' in triplet else 'cmake',
        '-B', f'build/{triplet}',
        f'-DCMAKE_TOOLCHAIN_FILE={vcpkg_root_dir}/scripts/buildsystems/vcpkg.cmake',
        f'-DVCPKG_TARGET_TRIPLET={triplet}',
        f'-DVCPKG_HOST_TRIPLET={triplet}',
    ])


def cmake_build(triplet: str, config: str):
    logging.info(inspect.currentframe().f_code.co_name)

    shell(args=[
        'cmake.exe' if 'windows' in triplet else 'cmake',
        '--build', f'build/{triplet}',
        '--config', config
    ])


def main():
    setup_logger()
    
    args = parse_cli_args()
    if args.vcpkg_root_dir == '':
        return
    
    conf = parse_vcpkg_conf()
    if conf.repository == '':
        logging.error('invalid vcpkg-configuration.json')
        return
    
    if args.vcpkg_bootstrap:
        bootstrap_vcpkg(root_dir=args.vcpkg_root_dir, conf=conf, triplet=args.vcpkg_triplet)

    if args.cmake_generate:
        cmake_generate(vcpkg_root_dir=args.vcpkg_root_dir, triplet=args.vcpkg_triplet)

    if args.cmake_build:
        cmake_build(triplet=args.vcpkg_triplet, config=args.config)


if __name__ == "__main__":
    main()