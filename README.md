## 1. How to add your port from git named libexample from scratch

- 1.1. add ports/libexample/portfile.cmake
- 1.2. add ports/libexample/vcpkg.json
- 1.3. add other files if necessary
- 1.4. git add ports/libexample/*
- 1.5. git commit -m "[libexample] add new port"
- 1.6. git rev-parse HEAD:ports/libexample
- 1.7. update versions/l-/libexample.json with git-parse result (git-tree)
- 1.8. vcpkg search libexample
- 1.9. vcpkg install libexample
- 1.10. update versions/baseline.json (or vcpkg x-add-version libexample)
- 1.11. git add versions/l-/libexample.json versions/baseline.json versions/l-/libexample.json
- 1.12. git commit -m "[libexample] add port to versions"
- 1.13. git push


## 2. How to pick exists port from microsoft/vcpkg
```
python pick_port.py --port=exists_msft_vcpkg_port
```
for examples, pick spdlog, boost, ffmpeg and their dependencies
```log
PS D:\sources\MediaPorts\vcpkg-media-registry> python pick_port.py --pick-port=spdlog
2024-09-22 13:16:59,662 - 91 - INFO - parse_cli_args
2024-09-22 13:16:59,663 - 396 - INFO - CliArgs(msft_vcpkg_root_dir='downloads/vcpkg', msft_vcpkg_url='https://github.com/microsoft/vcpkg.git', msft_vcpkg_branch='master', msft_vcpkg_baseline='98aa6396292d57e737a6ef999d4225ca488859d5', my_vcpkg_branch='main', pick_port='spdlog')
2024-09-22 13:16:59,663 - 287 - INFO - update_msft
2024-09-22 13:16:59,663 - 147 - INFO - run: git fetch
2024-09-22 13:17:00,425 - 147 - INFO - run: git rev-parse --abbrev-ref HEAD
2024-09-22 13:17:00,442 - 147 - INFO - run: git reset --hard 98aa6396292d57e737a6ef999d4225ca488859d5
HEAD is now at 98aa63962 [fast-double-parser] update to 0.8.0 (#40975)
2024-09-22 13:17:00,506 - 196 - WARNING - spdlog has 5 necessary ports: ["benchmark", "fmt", "spdlog", "vcpkg-cmake", "vcpkg-cmake-config"]
2024-09-22 13:17:03,248 - 147 - INFO - run: git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.
2024-09-22 13:17:03,292 - 360 - WARNING - copy downloads/vcpkg/ports/spdlog -> ./ports/spdlog
2024-09-22 13:17:03,293 - 369 - WARNING - copy downloads/vcpkg/versions/s-/spdlog.json -> ./versions/s-/spdlog.json
2024-09-22 13:17:03,293 - 382 - INFO - spdlog
commit 20110b4104f8a8cd0d439b7cdb2dbbebf29df939
Author: miyanyan <40262194+miyanyan@users.noreply.github.com>
Date:   2024-05-03 13:04:19 +0800

    [spdlog] update to 1.14.1 (#38508)

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [ ] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [ ] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [ ] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

 ports/spdlog/portfile.cmake | 2 +-
 ports/spdlog/vcpkg.json     | 2 +-
 versions/baseline.json      | 2 +-
 versions/s-/spdlog.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:17:03,293 - 147 - INFO - run: git add .
2024-09-22 13:17:03,314 - 147 - INFO - run: git commit -m [spdlog] update to 1.14.1 (#38508) --author miyanyan <40262194+miyanyan@users.noreply.github.com>
[main d63ff3186] [spdlog] update to 1.14.1 (#38508)
 Author: miyanyan <40262194+miyanyan@users.noreply.github.com>
 4 files changed, 303 insertions(+)
 create mode 100644 ports/spdlog/portfile.cmake
 create mode 100644 ports/spdlog/usage
 create mode 100644 ports/spdlog/vcpkg.json
 create mode 100644 versions/s-/spdlog.json
2024-09-22 13:17:03,373 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-cmake-config -> ./ports/vcpkg-cmake-config
2024-09-22 13:17:03,375 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-cmake-config.json -> ./versions/v-/vcpkg-cmake-config.json
2024-09-22 13:17:03,375 - 382 - INFO - vcpkg-cmake-config
commit 233f0965361166a454611bddab15c522cdf73965
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-06-06 10:25:03 +0200

    [vcpkg-cmake-config] Fix fixup of `)` paths (#38921)

    Cherry-picked from https://github.com/microsoft/vcpkg/pull/38847:

    Fix processing of `INTERFACE_LINK_LIBS` when it contain `)` inside `"`,
    e.g. for
    `C:/Program Files (x86)/Windows
    Kits/10/Lib/10.0.22621.0/um/x64/User32.Lib`
    created by `pkg_check_modules` from `-luser32` as found in icu pc files.

    Without the fix, the property is not processed at all, pulling release
    libs into debug builds.

 ports/vcpkg-cmake-config/vcpkg.json                |  5 ++-
 .../vcpkg_cmake_config_fixup.cmake                 | 42 ++++++++++++++++------
 versions/baseline.json                             |  4 +--
 versions/v-/vcpkg-cmake-config.json                |  5 +++
 4 files changed, 40 insertions(+), 16 deletions(-)

2024-09-22 13:17:03,375 - 147 - INFO - run: git add .
2024-09-22 13:17:03,395 - 147 - INFO - run: git commit -m [vcpkg-cmake-config] Fix fixup of `)` paths (#38921) --author Kai Pastor <dg0yt@darc.de>
[main baecf8554] [vcpkg-cmake-config] Fix fixup of `)` paths (#38921)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 389 insertions(+)
 create mode 100644 ports/vcpkg-cmake-config/copyright
 create mode 100644 ports/vcpkg-cmake-config/portfile.cmake
 create mode 100644 ports/vcpkg-cmake-config/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-cmake-config/vcpkg.json
 create mode 100644 ports/vcpkg-cmake-config/vcpkg_cmake_config_fixup.cmake
 create mode 100644 versions/v-/vcpkg-cmake-config.json
2024-09-22 13:17:03,446 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-cmake -> ./ports/vcpkg-cmake
2024-09-22 13:17:03,448 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-cmake.json -> ./versions/v-/vcpkg-cmake.json
2024-09-22 13:17:03,448 - 382 - INFO - vcpkg-cmake
commit 81bf2ee689f9861bba7891502e0e6aa07cbeb26e
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-06-14 20:34:23 +0200

    [vcpkg-cmake] get more logs (#38409)

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

 ports/vcpkg-cmake/vcpkg.json                  |  2 +-
 ports/vcpkg-cmake/vcpkg_cmake_configure.cmake | 21 +++++++++++++++++++--
 versions/baseline.json                        |  2 +-
 versions/v-/vcpkg-cmake.json                  |  5 +++++
 4 files changed, 26 insertions(+), 4 deletions(-)

2024-09-22 13:17:03,448 - 147 - INFO - run: git add .
2024-09-22 13:17:03,468 - 147 - INFO - run: git commit -m [vcpkg-cmake] get more logs (#38409) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main db7f9ba62] [vcpkg-cmake] get more logs (#38409)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 7 files changed, 662 insertions(+)
 create mode 100644 ports/vcpkg-cmake/portfile.cmake
 create mode 100644 ports/vcpkg-cmake/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-cmake/vcpkg.json
 create mode 100644 ports/vcpkg-cmake/vcpkg_cmake_build.cmake
 create mode 100644 ports/vcpkg-cmake/vcpkg_cmake_configure.cmake
 create mode 100644 ports/vcpkg-cmake/vcpkg_cmake_install.cmake
 create mode 100644 versions/v-/vcpkg-cmake.json
2024-09-22 13:17:03,524 - 360 - WARNING - copy downloads/vcpkg/ports/fmt -> ./ports/fmt
2024-09-22 13:17:03,525 - 369 - WARNING - copy downloads/vcpkg/versions/f-/fmt.json -> ./versions/f-/fmt.json
2024-09-22 13:17:03,526 - 382 - INFO - fmt
commit fe1cde61e971d53c9687cf9a46308f8f55da19fa
Author: miyanyan <40262194+miyanyan@users.noreply.github.com>
Date:   2024-08-03 15:41:25 +0800

    [fmt] update to 11.0.2 (#39738)

 .../buck-yeh-bux/fix-build-error-with-fmt11.patch  |  12 +++
 ports/buck-yeh-bux/portfile.cmake                  |   2 +
 ports/buck-yeh-bux/vcpkg.json                      |   2 +-
 ports/fizz/fix-build-error-with-fmt11.patch        |  13 +++
 ports/fizz/portfile.cmake                          |   1 +
 ports/fizz/vcpkg.json                              |   1 +
 ports/fmt/fix-visibility.patch                     |  12 ---
 ports/fmt/portfile.cmake                           |   5 +-
 ports/fmt/vcpkg.json                               |   3 +-
 ports/folly/fix-fmt11-cmake.patch                  |  13 +++
 ports/folly/portfile.cmake                         |   8 ++
 ports/folly/vcpkg.json                             |   1 +
 ports/libtorch/fix-build-error-with-fmt11.patch    |  36 +++++++
 ports/libtorch/portfile.cmake                      |   1 +
 ports/libtorch/vcpkg.json                          |   2 +-
 ports/saucer/fix-build-error-with-fmt11.patch      |  12 +++
 ports/saucer/portfile.cmake                        |   1 +
 ports/saucer/vcpkg.json                            |   1 +
 ports/seacas/fix-build-error-with-fmt11.patch      | 108 +++++++++++++++++++++
 ports/seacas/portfile.cmake                        |   1 +
 ports/seacas/vcpkg.json                            |   2 +-
 ports/shogun/fix-build-error-with-fmt11.patch      |  24 +++++
 ports/shogun/portfile.cmake                        |   1 +
 ports/shogun/vcpkg.json                            |   1 +
 .../vowpal-wabbit/fix-build-error-with-fmt11.patch |  89 +++++++++++++++++
 ports/vowpal-wabbit/portfile.cmake                 |   4 +-
 ports/vowpal-wabbit/vcpkg.json                     |   2 +-
 ports/wasmedge/fix-build-error-with-fmt11.patch    |  13 +++
 ports/wasmedge/portfile.cmake                      |   1 +
 ports/wasmedge/vcpkg.json                          |   2 +-
 ports/wpilib/fix-build-error-with-fmt11.patch      |  36 +++++++
 ports/wpilib/portfile.cmake                        |   1 +
 ports/wpilib/vcpkg.json                            |   1 +
 versions/b-/buck-yeh-bux.json                      |   5 +
 versions/baseline.json                             |  24 ++---
 versions/f-/fbthrift.json                          |   5 +
 versions/f-/fizz.json                              |   5 +
 versions/f-/fmt.json                               |   5 +
 versions/f-/folly.json                             |   5 +
 versions/l-/libtorch.json                          |   5 +
 versions/s-/saucer.json                            |   5 +
 versions/s-/seacas.json                            |   5 +
 versions/s-/shogun.json                            |   5 +
 versions/v-/vowpal-wabbit.json                     |   5 +
 versions/w-/wasmedge.json                          |   5 +
 versions/w-/wpilib.json                            |   5 +
 46 files changed, 461 insertions(+), 35 deletions(-)

2024-09-22 13:17:03,526 - 147 - INFO - run: git add .
2024-09-22 13:17:03,545 - 147 - INFO - run: git commit -m [fmt] update to 11.0.2 (#39738) --author miyanyan <40262194+miyanyan@users.noreply.github.com>
[main d217abd8e] [fmt] update to 11.0.2 (#39738)
 Author: miyanyan <40262194+miyanyan@users.noreply.github.com>
 5 files changed, 349 insertions(+)
 create mode 100644 ports/fmt/fix-write-batch.patch
 create mode 100644 ports/fmt/portfile.cmake
 create mode 100644 ports/fmt/usage
 create mode 100644 ports/fmt/vcpkg.json
 create mode 100644 versions/f-/fmt.json
2024-09-22 13:17:03,596 - 360 - WARNING - copy downloads/vcpkg/ports/benchmark -> ./ports/benchmark
2024-09-22 13:17:03,597 - 369 - WARNING - copy downloads/vcpkg/versions/b-/benchmark.json -> ./versions/b-/benchmark.json
2024-09-22 13:17:03,598 - 382 - INFO - benchmark
commit 9b9928a957d2dbe705773615684091fd958c64c1
Author: Ryan Zoeller <ryan.zoeller@aliaro.com>
Date:   2024-09-09 22:25:20 -0500

    [benchmark] update to 1.9.0 (#40839)

 ports/benchmark/portfile.cmake | 2 +-
 ports/benchmark/vcpkg.json     | 2 +-
 versions/b-/benchmark.json     | 5 +++++
 versions/baseline.json         | 2 +-
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:17:03,598 - 147 - INFO - run: git add .
2024-09-22 13:17:03,618 - 147 - INFO - run: git commit -m [benchmark] update to 1.9.0 (#40839) --author Ryan Zoeller <ryan.zoeller@aliaro.com>
[main 3aff7509d] [benchmark] update to 1.9.0 (#40839)
 Author: Ryan Zoeller <ryan.zoeller@aliaro.com>
 3 files changed, 186 insertions(+)
 create mode 100644 ports/benchmark/portfile.cmake
 create mode 100644 ports/benchmark/vcpkg.json
 create mode 100644 versions/b-/benchmark.json
PS D:\sources\MediaPorts\vcpkg-media-registry> python pick_port.py --pick-port=openssl
2024-09-22 13:17:07,655 - 91 - INFO - parse_cli_args
2024-09-22 13:17:07,656 - 396 - INFO - CliArgs(msft_vcpkg_root_dir='downloads/vcpkg', msft_vcpkg_url='https://github.com/microsoft/vcpkg.git', msft_vcpkg_branch='master', msft_vcpkg_baseline='98aa6396292d57e737a6ef999d4225ca488859d5', my_vcpkg_branch='main', pick_port='openssl')
2024-09-22 13:17:07,656 - 287 - INFO - update_msft
2024-09-22 13:17:07,656 - 147 - INFO - run: git fetch
2024-09-22 13:17:08,408 - 147 - INFO - run: git rev-parse --abbrev-ref HEAD
2024-09-22 13:17:08,424 - 147 - INFO - run: git reset --hard 98aa6396292d57e737a6ef999d4225ca488859d5
HEAD is now at 98aa63962 [fast-double-parser] update to 0.8.0 (#40975)
2024-09-22 13:17:08,499 - 196 - WARNING - openssl has 4 necessary ports: ["openssl", "vcpkg-cmake", "vcpkg-cmake-config", "vcpkg-cmake-get-vars"]
2024-09-22 13:17:11,715 - 147 - INFO - run: git checkout main
Already on 'main'
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)
2024-09-22 13:17:11,787 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-cmake-get-vars -> ./ports/vcpkg-cmake-get-vars
2024-09-22 13:17:11,790 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-cmake-get-vars.json -> ./versions/v-/vcpkg-cmake-get-vars.json
2024-09-22 13:17:11,790 - 382 - INFO - vcpkg-cmake-get-vars
commit 8ccb84df727bdf83045e53c319af05c554838b80
Author: Yury Bura <yurybura@gmail.com>
Date:   2024-01-22 19:56:30 +0100

    [boost] Update to v1.84.0 (#35693)

    * [scripts] update Boost ports generation script, fixes #35187

    * [boost] remove obsolete patches and re-generate ports

    * update versions

    * [boost] remove redundant vcpkg_minimum_required

    * update versions

    * [scripts/boost] update dependencies to config/checks, review b2-options.cmake files

    * [boost-*] regenerate ports

    * [boost-locale] fix patch

    * update versions

    * [boost-serialization] fix checks

    * update version

    * [boost-*] better fixes related to the config checks

    * update version

    * [boost-cobalt] fix build

    * update versions

    * [liblas] Boost v1.84.0 requires C++11

    * [pcl] fix Unix build

    * add versions

    * [vcpkg-cmake-get-vars] add CMAKE_<LANG>_COMPILER_VERSION

    * [boost-cobalt] detect compiler

    * [coin] force C++11

    * [json5-parser] force C++11

    * add versions

    * [boost-cobalt] exclude iOS and Android platforms due to C++ Concepts library is not supported

    * [gtsam] force C++11

    * [kenlm] force C++11

    * [quickfast] force C++11

    * [liblas] force C++11

    * update versions

    * [boost] re-generate port

    * update version

    * [kenlm] revert changes

    * [boost-cobalt] exclude OSX

    * update versions

    * [plc] remove useless patch after merge

    * update versions after merge

    ---------

    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/boost-accumulators/portfile.cmake            |   4 +-
 ports/boost-accumulators/vcpkg.json                |  44 +--
 ports/boost-algorithm/portfile.cmake               |   4 +-
 ports/boost-algorithm/vcpkg.json                   |  38 +--
 ports/boost-align/portfile.cmake                   |   4 +-
 ports/boost-align/vcpkg.json                       |  12 +-
 ports/boost-any/portfile.cmake                     |   4 +-
 ports/boost-any/vcpkg.json                         |  24 +-
 ports/boost-array/portfile.cmake                   |   4 +-
 ports/boost-array/vcpkg.json                       |  14 +-
 ports/boost-asio/portfile.cmake                    |   4 +-
 ports/boost-asio/vcpkg.json                        |  60 +---
 ports/boost-assert/portfile.cmake                  |   4 +-
 ports/boost-assert/vcpkg.json                      |   6 +-
 ports/boost-assign/portfile.cmake                  |   4 +-
 ports/boost-assign/vcpkg.json                      |  26 +-
 ports/boost-atomic/portfile.cmake                  |  16 +-
 ports/boost-atomic/vcpkg.json                      |  26 +-
 ports/boost-beast/portfile.cmake                   |   4 +-
 ports/boost-beast/vcpkg.json                       |  46 +--
 ports/boost-bimap/portfile.cmake                   |   4 +-
 ports/boost-bimap/vcpkg.json                       |  30 +-
 ports/boost-bind/portfile.cmake                    |   4 +-
 ports/boost-bind/vcpkg.json                        |   8 +-
 ports/boost-build/portfile.cmake                   |   6 +-
 ports/boost-build/vcpkg.json                       |   4 +-
 ports/boost-callable-traits/portfile.cmake         |   4 +-
 ports/boost-callable-traits/vcpkg.json             |   8 +-
 ports/boost-chrono/portfile.cmake                  |   4 +-
 ports/boost-chrono/vcpkg.json                      |  38 +--
 ports/boost-circular-buffer/portfile.cmake         |   4 +-
 ports/boost-circular-buffer/vcpkg.json             |  20 +-
 ports/boost-cobalt/b2-options.cmake                |  24 ++
 ports/boost-cobalt/portfile.cmake                  |  22 ++
 ports/boost-cobalt/vcpkg.json                      |  81 +++++
 ports/boost-compat/portfile.cmake                  |   4 +-
 ports/boost-compat/vcpkg.json                      |  10 +-
 ports/boost-compatibility/portfile.cmake           |   4 +-
 ports/boost-compatibility/vcpkg.json               |   8 +-
 ports/boost-compute/portfile.cmake                 |   4 +-
 ports/boost-compute/vcpkg.json                     |  58 ++--
 ports/boost-concept-check/portfile.cmake           |   4 +-
 ports/boost-concept-check/vcpkg.json               |  12 +-
 ports/boost-config/portfile.cmake                  |   4 +-
 ports/boost-config/vcpkg.json                      |   4 +-
 ports/boost-container-hash/portfile.cmake          |   4 +-
 ports/boost-container-hash/vcpkg.json              |  14 +-
 ports/boost-container/portfile.cmake               |   4 +-
 ports/boost-container/vcpkg.json                   |  18 +-
 ports/boost-context/b2-options.cmake.in            |   1 -
 ports/boost-context/portfile.cmake                 |   4 +-
 ports/boost-context/vcpkg.json                     |  22 +-
 ports/boost-contract/portfile.cmake                |   4 +-
 ports/boost-contract/vcpkg.json                    |  40 +--
 ports/boost-conversion/portfile.cmake              |   4 +-
 ports/boost-conversion/vcpkg.json                  |  24 +-
 ports/boost-convert/portfile.cmake                 |   4 +-
 ports/boost-convert/vcpkg.json                     |  26 +-
 ports/boost-core/portfile.cmake                    |   4 +-
 ports/boost-core/vcpkg.json                        |  12 +-
 ports/boost-coroutine/portfile.cmake               |   4 +-
 ports/boost-coroutine/vcpkg.json                   |  28 +-
 ports/boost-coroutine2/portfile.cmake              |   4 +-
 ports/boost-coroutine2/vcpkg.json                  |  10 +-
 ports/boost-crc/portfile.cmake                     |   4 +-
 ports/boost-crc/vcpkg.json                         |  12 +-
 ports/boost-date-time/portfile.cmake               |   4 +-
 ports/boost-date-time/vcpkg.json                   |  38 +--
 ports/boost-describe/portfile.cmake                |   4 +-
 ports/boost-describe/vcpkg.json                    |  10 +-
 ports/boost-detail/portfile.cmake                  |   4 +-
 ports/boost-detail/vcpkg.json                      |  14 +-
 ports/boost-dll/portfile.cmake                     |   4 +-
 ports/boost-dll/vcpkg.json                         |  36 +--
 ports/boost-dynamic-bitset/portfile.cmake          |   4 +-
 ports/boost-dynamic-bitset/vcpkg.json              |  20 +-
 ports/boost-endian/portfile.cmake                  |   4 +-
 ports/boost-endian/vcpkg.json                      |  18 +-
 ports/boost-exception/portfile.cmake               |   4 +-
 ports/boost-exception/vcpkg.json                   |  22 +-
 ports/boost-fiber/portfile.cmake                   |   4 +-
 ports/boost-fiber/vcpkg.json                       |  29 +-
 ports/boost-filesystem/portfile.cmake              |   4 +-
 ports/boost-filesystem/vcpkg.json                  |  36 +--
 ports/boost-flyweight/portfile.cmake               |   4 +-
 ports/boost-flyweight/vcpkg.json                   |  30 +-
 ports/boost-foreach/portfile.cmake                 |   4 +-
 ports/boost-foreach/vcpkg.json                     |  16 +-
 ports/boost-format/portfile.cmake                  |   4 +-
 ports/boost-format/vcpkg.json                      |  18 +-
 ports/boost-function-types/portfile.cmake          |   4 +-
 ports/boost-function-types/vcpkg.json              |  16 +-
 ports/boost-function/portfile.cmake                |   4 +-
 ports/boost-function/vcpkg.json                    |  22 +-
 ports/boost-functional/portfile.cmake              |   4 +-
 ports/boost-functional/vcpkg.json                  |  22 +-
 ports/boost-fusion/portfile.cmake                  |   4 +-
 ports/boost-fusion/vcpkg.json                      |  28 +-
 ports/boost-geometry/portfile.cmake                |   4 +-
 ports/boost-geometry/vcpkg.json                    |  64 ++--
 ports/boost-gil/portfile.cmake                     |   4 +-
 ports/boost-gil/vcpkg.json                         |  26 +-
 ports/boost-graph-parallel/portfile.cmake          |   4 +-
 ports/boost-graph-parallel/vcpkg.json              |  60 ++--
 ports/boost-graph/portfile.cmake                   |   4 +-
 ports/boost-graph/vcpkg.json                       |  90 +++---
 ports/boost-hana/portfile.cmake                    |   4 +-
 ports/boost-hana/vcpkg.json                        |  14 +-
 ports/boost-heap/portfile.cmake                    |   4 +-
 ports/boost-heap/vcpkg.json                        |  28 +-
 ports/boost-histogram/portfile.cmake               |   4 +-
 ports/boost-histogram/vcpkg.json                   |  18 +-
 ports/boost-hof/portfile.cmake                     |   4 +-
 ports/boost-hof/vcpkg.json                         |   8 +-
 ports/boost-icl/portfile.cmake                     |   4 +-
 ports/boost-icl/vcpkg.json                         |  34 +--
 ports/boost-integer/portfile.cmake                 |   4 +-
 ports/boost-integer/vcpkg.json                     |  16 +-
 ports/boost-interprocess/portfile.cmake            |   4 +-
 ports/boost-interprocess/vcpkg.json                |  24 +-
 ports/boost-interval/portfile.cmake                |   4 +-
 ports/boost-interval/vcpkg.json                    |  10 +-
 ports/boost-intrusive/portfile.cmake               |   4 +-
 ports/boost-intrusive/vcpkg.json                   |  14 +-
 ports/boost-io/portfile.cmake                      |   4 +-
 ports/boost-io/vcpkg.json                          |   6 +-
 ports/boost-iostreams/portfile.cmake               |   4 +-
 ports/boost-iostreams/vcpkg.json                   |  45 ++-
 ports/boost-iterator/portfile.cmake                |   4 +-
 ports/boost-iterator/vcpkg.json                    |  34 +--
 ...se-of-intrinsics-on-windows-ARM-platforms.patch |  44 ---
 ...lace-_M_ARM64-with-_M_ARM-for-32-bit-path.patch |  25 --
 ports/boost-json/b2-options.cmake                  |   3 -
 ports/boost-json/portfile.cmake                    |  12 +-
 ports/boost-json/vcpkg.json                        |  28 +-
 ports/boost-lambda/portfile.cmake                  |   4 +-
 ports/boost-lambda/vcpkg.json                      |  24 +-
 ports/boost-lambda2/portfile.cmake                 |   4 +-
 ports/boost-lambda2/vcpkg.json                     |   8 +-
 ports/boost-leaf/portfile.cmake                    |   4 +-
 ports/boost-leaf/vcpkg.json                        |   8 +-
 ports/boost-lexical-cast/portfile.cmake            |   4 +-
 ports/boost-lexical-cast/vcpkg.json                |  34 +--
 ports/boost-local-function/portfile.cmake          |   4 +-
 ports/boost-local-function/vcpkg.json              |  18 +-
 .../0001-fix-build-error-on-MSVC.patch             |  25 --
 ports/boost-locale/fix-dependencies.patch          |  39 +--
 ports/boost-locale/portfile.cmake                  |  12 +-
 ports/boost-locale/vcpkg.json                      |  22 +-
 ports/boost-lockfree/portfile.cmake                |   4 +-
 ports/boost-lockfree/vcpkg.json                    |  34 +--
 ports/boost-log/portfile.cmake                     |   6 +-
 ports/boost-log/vcpkg.json                         | 102 +++----
 ports/boost-logic/portfile.cmake                   |   4 +-
 ports/boost-logic/vcpkg.json                       |   8 +-
 ports/boost-math/001-remove-checks.patch           |  23 --
 ports/boost-math/b2-options.cmake                  |   3 -
 ports/boost-math/portfile.cmake                    |  15 +-
 ports/boost-math/vcpkg.json                        |  28 +-
 ports/boost-metaparse/portfile.cmake               |   4 +-
 ports/boost-metaparse/vcpkg.json                   |  16 +-
 .../boost-modular-build.cmake                      |   4 +-
 ports/boost-modular-build-helper/vcpkg.json        |   5 +-
 ports/boost-move/portfile.cmake                    |   4 +-
 ports/boost-move/vcpkg.json                        |   6 +-
 ports/boost-mp11/portfile.cmake                    |   4 +-
 ports/boost-mp11/vcpkg.json                        |   8 +-
 ports/boost-mpi/fix-build-with-msvc.patch          |  30 --
 ports/boost-mpi/portfile.cmake                     |   5 +-
 ports/boost-mpi/vcpkg.json                         |  44 +--
 ports/boost-mpl/portfile.cmake                     |   4 +-
 ports/boost-mpl/vcpkg.json                         |  18 +-
 ports/boost-msm/portfile.cmake                     |   4 +-
 ports/boost-msm/vcpkg.json                         |  38 +--
 ports/boost-multi-array/portfile.cmake             |   4 +-
 ports/boost-multi-array/vcpkg.json                 |  24 +-
 ports/boost-multi-index/portfile.cmake             |   4 +-
 ports/boost-multi-index/vcpkg.json                 |  36 +--
 ports/boost-multiprecision/portfile.cmake          |   4 +-
 ports/boost-multiprecision/vcpkg.json              |  22 +-
 ports/boost-mysql/portfile.cmake                   |   4 +-
 ports/boost-mysql/vcpkg.json                       |  26 +-
 ports/boost-nowide/b2-options.cmake                |   3 -
 ports/boost-nowide/portfile.cmake                  |   9 +-
 ports/boost-nowide/vcpkg.json                      |  12 +-
 ports/boost-numeric-conversion/portfile.cmake      |   4 +-
 ports/boost-numeric-conversion/vcpkg.json          |  18 +-
 ports/boost-odeint/portfile.cmake                  |   4 +-
 ports/boost-odeint/vcpkg.json                      |  46 +--
 ports/boost-optional/portfile.cmake                |   4 +-
 ports/boost-optional/vcpkg.json                    |  24 +-
 ports/boost-outcome/portfile.cmake                 |   4 +-
 ports/boost-outcome/vcpkg.json                     |  12 +-
 ports/boost-parameter-python/portfile.cmake        |   4 +-
 ports/boost-parameter-python/vcpkg.json            |  16 +-
 ports/boost-parameter/portfile.cmake               |   4 +-
 ports/boost-parameter/vcpkg.json                   |  24 +-
 ports/boost-pfr/portfile.cmake                     |   4 +-
 ports/boost-pfr/vcpkg.json                         |   8 +-
 ports/boost-phoenix/fix-duplicate-symbols.patch    |  13 -
 ports/boost-phoenix/portfile.cmake                 |   5 +-
 ports/boost-phoenix/vcpkg.json                     |  32 +-
 ports/boost-poly-collection/portfile.cmake         |   4 +-
 ports/boost-poly-collection/vcpkg.json             |  20 +-
 ports/boost-polygon/portfile.cmake                 |   4 +-
 ports/boost-polygon/vcpkg.json                     |   6 +-
 ports/boost-pool/portfile.cmake                    |   4 +-
 ports/boost-pool/vcpkg.json                        |  16 +-
 ports/boost-predef/portfile.cmake                  |   4 +-
 ports/boost-predef/vcpkg.json                      |   8 +-
 ports/boost-preprocessor/portfile.cmake            |   4 +-
 ports/boost-preprocessor/vcpkg.json                |   8 +-
 ports/boost-process/portfile.cmake                 |   4 +-
 ports/boost-process/vcpkg.json                     |  42 +--
 ports/boost-program-options/portfile.cmake         |   4 +-
 ports/boost-program-options/vcpkg.json             |  34 +--
 ports/boost-property-map-parallel/portfile.cmake   |   4 +-
 ports/boost-property-map-parallel/vcpkg.json       |  30 +-
 ports/boost-property-map/portfile.cmake            |   4 +-
 ports/boost-property-map/vcpkg.json                |  34 +--
 ports/boost-property-tree/portfile.cmake           |   4 +-
 ports/boost-property-tree/vcpkg.json               |  36 +--
 ports/boost-proto/portfile.cmake                   |   4 +-
 ports/boost-proto/vcpkg.json                       |  24 +-
 ports/boost-ptr-container/portfile.cmake           |   4 +-
 ports/boost-ptr-container/vcpkg.json               |  30 +-
 ports/boost-python/portfile.cmake                  |   4 +-
 ports/boost-python/vcpkg.json                      |  50 +--
 ports/boost-qvm/portfile.cmake                     |   4 +-
 ports/boost-qvm/vcpkg.json                         |   8 +-
 ports/boost-random/portfile.cmake                  |   4 +-
 ports/boost-random/vcpkg.json                      |  34 +--
 ports/boost-range/portfile.cmake                   |   4 +-
 ports/boost-range/vcpkg.json                       |  38 +--
 ports/boost-ratio/portfile.cmake                   |   4 +-
 ports/boost-ratio/vcpkg.json                       |  30 +-
 ports/boost-rational/portfile.cmake                |   4 +-
 ports/boost-rational/vcpkg.json                    |  20 +-
 ports/boost-redis/portfile.cmake                   |  12 +
 ports/boost-redis/vcpkg.json                       |  42 +++
 ports/boost-regex/b2-options.cmake                 |   3 -
 ports/boost-regex/portfile.cmake                   |   4 +-
 ports/boost-regex/vcpkg.json                       |  32 +-
 ports/boost-safe-numerics/portfile.cmake           |   4 +-
 ports/boost-safe-numerics/vcpkg.json               |  16 +-
 ports/boost-scope-exit/portfile.cmake              |   4 +-
 ports/boost-scope-exit/vcpkg.json                  |  14 +-
 ports/boost-serialization/portfile.cmake           |   9 +-
 ports/boost-serialization/vcpkg.json               |  62 ++--
 ports/boost-signals2/portfile.cmake                |   4 +-
 ports/boost-signals2/vcpkg.json                    |  34 +--
 ports/boost-smart-ptr/portfile.cmake               |   4 +-
 ports/boost-smart-ptr/vcpkg.json                   |  18 +-
 ports/boost-sort/portfile.cmake                    |   4 +-
 ports/boost-sort/vcpkg.json                        |  14 +-
 ports/boost-spirit/portfile.cmake                  |   4 +-
 ports/boost-spirit/vcpkg.json                      |  62 ++--
 ports/boost-stacktrace/portfile.cmake              |   9 +-
 ports/boost-stacktrace/vcpkg.json                  |  30 +-
 ports/boost-statechart/portfile.cmake              |   4 +-
 ports/boost-statechart/vcpkg.json                  |  28 +-
 ports/boost-static-assert/portfile.cmake           |   4 +-
 ports/boost-static-assert/vcpkg.json               |   6 +-
 ports/boost-static-string/portfile.cmake           |   4 +-
 ports/boost-static-string/vcpkg.json               |  18 +-
 ports/boost-stl-interfaces/portfile.cmake          |   4 +-
 ports/boost-stl-interfaces/vcpkg.json              |  10 +-
 ports/boost-system/portfile.cmake                  |   4 +-
 ports/boost-system/vcpkg.json                      |  18 +-
 ports/boost-test/portfile.cmake                    |   4 +-
 ports/boost-test/vcpkg.json                        |  44 +--
 ports/boost-thread/portfile.cmake                  |   4 +-
 ports/boost-thread/vcpkg.json                      |  74 ++---
 ports/boost-throw-exception/portfile.cmake         |   4 +-
 ports/boost-throw-exception/vcpkg.json             |   8 +-
 ports/boost-timer/portfile.cmake                   |   4 +-
 ports/boost-timer/vcpkg.json                       |  14 +-
 ports/boost-tokenizer/portfile.cmake               |   4 +-
 ports/boost-tokenizer/vcpkg.json                   |  16 +-
 ports/boost-tti/portfile.cmake                     |   4 +-
 ports/boost-tti/vcpkg.json                         |  14 +-
 ports/boost-tuple/portfile.cmake                   |   4 +-
 ports/boost-tuple/vcpkg.json                       |  12 +-
 ports/boost-type-erasure/portfile.cmake            |   4 +-
 ports/boost-type-erasure/vcpkg.json                |  36 +--
 ports/boost-type-index/portfile.cmake              |   4 +-
 ports/boost-type-index/vcpkg.json                  |  24 +-
 ports/boost-type-traits/portfile.cmake             |   4 +-
 ports/boost-type-traits/vcpkg.json                 |   8 +-
 ports/boost-typeof/portfile.cmake                  |   4 +-
 ports/boost-typeof/vcpkg.json                      |  14 +-
 ports/boost-ublas/portfile.cmake                   |   4 +-
 ports/boost-ublas/vcpkg.json                       |  28 +-
 ports/boost-uninstall/vcpkg.json                   |   2 +-
 ports/boost-units/portfile.cmake                   |   4 +-
 ports/boost-units/vcpkg.json                       |  28 +-
 .../0001-unordered-fix-copy-assign.patch           |  16 -
 ports/boost-unordered/portfile.cmake               |   5 +-
 ports/boost-unordered/vcpkg.json                   |  38 +--
 ports/boost-url/portfile.cmake                     |   8 +-
 ports/boost-url/vcpkg.json                         |  30 +-
 ports/boost-utility/portfile.cmake                 |   4 +-
 ports/boost-utility/vcpkg.json                     |  18 +-
 ports/boost-uuid/portfile.cmake                    |   4 +-
 ports/boost-uuid/vcpkg.json                        |  32 +-
 ports/boost-variant/portfile.cmake                 |   4 +-
 ports/boost-variant/vcpkg.json                     |  38 +--
 ports/boost-variant2/portfile.cmake                |   4 +-
 ports/boost-variant2/vcpkg.json                    |  10 +-
 ports/boost-vcpkg-helpers/portfile.cmake           |   1 -
 ports/boost-vcpkg-helpers/vcpkg.json               |   4 +-
 ports/boost-vmd/portfile.cmake                     |   4 +-
 ports/boost-vmd/vcpkg.json                         |  10 +-
 ports/boost-wave/portfile.cmake                    |   4 +-
 ports/boost-wave/vcpkg.json                        |  46 +--
 ports/boost-winapi/portfile.cmake                  |   4 +-
 ports/boost-winapi/vcpkg.json                      |   8 +-
 ports/boost-xpressive/portfile.cmake               |   4 +-
 ports/boost-xpressive/vcpkg.json                   |  48 +--
 ports/boost-yap/portfile.cmake                     |   4 +-
 ports/boost-yap/vcpkg.json                         |  14 +-
 ports/boost/vcpkg.json                             | 308 ++++++++++---------
 ports/coin/portfile.cmake                          |   1 +
 ports/coin/vcpkg.json                              |   2 +-
 ports/gtsam/portfile.cmake                         |   1 +
 ports/gtsam/vcpkg.json                             |   1 +
 ports/json5-parser/portfile.cmake                  |   2 +
 ports/json5-parser/vcpkg.json                      |   2 +-
 ports/liblas/force-cpp11.patch                     |  27 ++
 ports/liblas/portfile.cmake                        |   1 +
 ports/liblas/vcpkg.json                            |   2 +-
 ports/quickfast/CMakeLists.txt                     |   2 +
 ports/quickfast/vcpkg.json                         |   2 +-
 .../cmake_get_vars/CMakeLists.txt                  |   2 +
 ports/vcpkg-cmake-get-vars/vcpkg.json              |   2 +-
 scripts/boost/generate-ports.ps1                   |  89 +++---
 scripts/boost/post-build-stubs/atomic.cmake        |   2 +
 scripts/boost/post-source-stubs/atomic.cmake       |  12 +-
 scripts/boost/post-source-stubs/cobalt.cmake       |   5 +
 scripts/boost/post-source-stubs/locale.cmake       |   4 +-
 scripts/boost/post-source-stubs/log.cmake          |   2 +-
 scripts/boost/post-source-stubs/math.cmake         |   5 +
 .../boost/post-source-stubs/serialization.cmake    |   5 +
 scripts/boost/post-source-stubs/stacktrace.cmake   |   5 +
 scripts/boost/post-source-stubs/url.cmake          |   4 +-
 versions/b-/boost-accumulators.json                |   5 +
 versions/b-/boost-algorithm.json                   |   5 +
 versions/b-/boost-align.json                       |   5 +
 versions/b-/boost-any.json                         |   5 +
 versions/b-/boost-array.json                       |   5 +
 versions/b-/boost-asio.json                        |   5 +
 versions/b-/boost-assert.json                      |   5 +
 versions/b-/boost-assign.json                      |   5 +
 versions/b-/boost-atomic.json                      |   5 +
 versions/b-/boost-beast.json                       |   5 +
 versions/b-/boost-bimap.json                       |   5 +
 versions/b-/boost-bind.json                        |   5 +
 versions/b-/boost-build.json                       |   5 +
 versions/b-/boost-callable-traits.json             |   5 +
 versions/b-/boost-chrono.json                      |   5 +
 versions/b-/boost-circular-buffer.json             |   5 +
 versions/b-/boost-cobalt.json                      |   9 +
 versions/b-/boost-compat.json                      |   5 +
 versions/b-/boost-compatibility.json               |   5 +
 versions/b-/boost-compute.json                     |   5 +
 versions/b-/boost-concept-check.json               |   5 +
 versions/b-/boost-config.json                      |   5 +
 versions/b-/boost-container-hash.json              |   5 +
 versions/b-/boost-container.json                   |   5 +
 versions/b-/boost-context.json                     |   5 +
 versions/b-/boost-contract.json                    |   5 +
 versions/b-/boost-conversion.json                  |   5 +
 versions/b-/boost-convert.json                     |   5 +
 versions/b-/boost-core.json                        |   5 +
 versions/b-/boost-coroutine.json                   |   5 +
 versions/b-/boost-coroutine2.json                  |   5 +
 versions/b-/boost-crc.json                         |   5 +
 versions/b-/boost-date-time.json                   |   5 +
 versions/b-/boost-describe.json                    |   5 +
 versions/b-/boost-detail.json                      |   5 +
 versions/b-/boost-dll.json                         |   5 +
 versions/b-/boost-dynamic-bitset.json              |   5 +
 versions/b-/boost-endian.json                      |   5 +
 versions/b-/boost-exception.json                   |   5 +
 versions/b-/boost-fiber.json                       |   5 +
 versions/b-/boost-filesystem.json                  |   5 +
 versions/b-/boost-flyweight.json                   |   5 +
 versions/b-/boost-foreach.json                     |   5 +
 versions/b-/boost-format.json                      |   5 +
 versions/b-/boost-function-types.json              |   5 +
 versions/b-/boost-function.json                    |   5 +
 versions/b-/boost-functional.json                  |   5 +
 versions/b-/boost-fusion.json                      |   5 +
 versions/b-/boost-geometry.json                    |   5 +
 versions/b-/boost-gil.json                         |   5 +
 versions/b-/boost-graph-parallel.json              |   5 +
 versions/b-/boost-graph.json                       |   5 +
 versions/b-/boost-hana.json                        |   5 +
 versions/b-/boost-heap.json                        |   5 +
 versions/b-/boost-histogram.json                   |   5 +
 versions/b-/boost-hof.json                         |   5 +
 versions/b-/boost-icl.json                         |   5 +
 versions/b-/boost-integer.json                     |   5 +
 versions/b-/boost-interprocess.json                |   5 +
 versions/b-/boost-interval.json                    |   5 +
 versions/b-/boost-intrusive.json                   |   5 +
 versions/b-/boost-io.json                          |   5 +
 versions/b-/boost-iostreams.json                   |   5 +
 versions/b-/boost-iterator.json                    |   5 +
 versions/b-/boost-json.json                        |   5 +
 versions/b-/boost-lambda.json                      |   5 +
 versions/b-/boost-lambda2.json                     |   5 +
 versions/b-/boost-leaf.json                        |   5 +
 versions/b-/boost-lexical-cast.json                |   5 +
 versions/b-/boost-local-function.json              |   5 +
 versions/b-/boost-locale.json                      |   5 +
 versions/b-/boost-lockfree.json                    |   5 +
 versions/b-/boost-log.json                         |   5 +
 versions/b-/boost-logic.json                       |   5 +
 versions/b-/boost-math.json                        |   5 +
 versions/b-/boost-metaparse.json                   |   5 +
 versions/b-/boost-modular-build-helper.json        |   5 +
 versions/b-/boost-move.json                        |   5 +
 versions/b-/boost-mp11.json                        |   5 +
 versions/b-/boost-mpi.json                         |   5 +
 versions/b-/boost-mpl.json                         |   5 +
 versions/b-/boost-msm.json                         |   5 +
 versions/b-/boost-multi-array.json                 |   5 +
 versions/b-/boost-multi-index.json                 |   5 +
 versions/b-/boost-multiprecision.json              |   5 +
 versions/b-/boost-mysql.json                       |   5 +
 versions/b-/boost-nowide.json                      |   5 +
 versions/b-/boost-numeric-conversion.json          |   5 +
 versions/b-/boost-odeint.json                      |   5 +
 versions/b-/boost-optional.json                    |   5 +
 versions/b-/boost-outcome.json                     |   5 +
 versions/b-/boost-parameter-python.json            |   5 +
 versions/b-/boost-parameter.json                   |   5 +
 versions/b-/boost-pfr.json                         |   5 +
 versions/b-/boost-phoenix.json                     |   5 +
 versions/b-/boost-poly-collection.json             |   5 +
 versions/b-/boost-polygon.json                     |   5 +
 versions/b-/boost-pool.json                        |   5 +
 versions/b-/boost-predef.json                      |   5 +
 versions/b-/boost-preprocessor.json                |   5 +
 versions/b-/boost-process.json                     |   5 +
 versions/b-/boost-program-options.json             |   5 +
 versions/b-/boost-property-map-parallel.json       |   5 +
 versions/b-/boost-property-map.json                |   5 +
 versions/b-/boost-property-tree.json               |   5 +
 versions/b-/boost-proto.json                       |   5 +
 versions/b-/boost-ptr-container.json               |   5 +
 versions/b-/boost-python.json                      |   5 +
 versions/b-/boost-qvm.json                         |   5 +
 versions/b-/boost-random.json                      |   5 +
 versions/b-/boost-range.json                       |   5 +
 versions/b-/boost-ratio.json                       |   5 +
 versions/b-/boost-rational.json                    |   5 +
 versions/b-/boost-redis.json                       |   9 +
 versions/b-/boost-regex.json                       |   5 +
 versions/b-/boost-safe-numerics.json               |   5 +
 versions/b-/boost-scope-exit.json                  |   5 +
 versions/b-/boost-serialization.json               |   5 +
 versions/b-/boost-signals2.json                    |   5 +
 versions/b-/boost-smart-ptr.json                   |   5 +
 versions/b-/boost-sort.json                        |   5 +
 versions/b-/boost-spirit.json                      |   5 +
 versions/b-/boost-stacktrace.json                  |   5 +
 versions/b-/boost-statechart.json                  |   5 +
 versions/b-/boost-static-assert.json               |   5 +
 versions/b-/boost-static-string.json               |   5 +
 versions/b-/boost-stl-interfaces.json              |   5 +
 versions/b-/boost-system.json                      |   5 +
 versions/b-/boost-test.json                        |   5 +
 versions/b-/boost-thread.json                      |   5 +
 versions/b-/boost-throw-exception.json             |   5 +
 versions/b-/boost-timer.json                       |   5 +
 versions/b-/boost-tokenizer.json                   |   5 +
 versions/b-/boost-tti.json                         |   5 +
 versions/b-/boost-tuple.json                       |   5 +
 versions/b-/boost-type-erasure.json                |   5 +
 versions/b-/boost-type-index.json                  |   5 +
 versions/b-/boost-type-traits.json                 |   5 +
 versions/b-/boost-typeof.json                      |   5 +
 versions/b-/boost-ublas.json                       |   5 +
 versions/b-/boost-uninstall.json                   |   5 +
 versions/b-/boost-units.json                       |   5 +
 versions/b-/boost-unordered.json                   |   5 +
 versions/b-/boost-url.json                         |   5 +
 versions/b-/boost-utility.json                     |   5 +
 versions/b-/boost-uuid.json                        |   5 +
 versions/b-/boost-variant.json                     |   5 +
 versions/b-/boost-variant2.json                    |   5 +
 versions/b-/boost-vcpkg-helpers.json               |   5 +
 versions/b-/boost-vmd.json                         |   5 +
 versions/b-/boost-wave.json                        |   5 +
 versions/b-/boost-winapi.json                      |   5 +
 versions/b-/boost-xpressive.json                   |   5 +
 versions/b-/boost-yap.json                         |   5 +
 versions/b-/boost.json                             |   5 +
 versions/baseline.json                             | 334 +++++++++++----------
 versions/c-/coin.json                              |   5 +
 versions/g-/gtsam.json                             |   5 +
 versions/j-/json5-parser.json                      |   5 +
 versions/l-/liblas.json                            |   5 +
 versions/q-/quickfast.json                         |   5 +
 versions/v-/vcpkg-cmake-get-vars.json              |   5 +
 507 files changed, 3588 insertions(+), 2887 deletions(-)

2024-09-22 13:17:11,793 - 147 - INFO - run: git add .
2024-09-22 13:17:11,814 - 147 - INFO - run: git commit -m [boost] Update to v1.84.0 (#35693) --author Yury Bura <yurybura@gmail.com>
[main 17644b1ee] [boost] Update to v1.84.0 (#35693)
 Author: Yury Bura <yurybura@gmail.com>
 6 files changed, 338 insertions(+)
 create mode 100644 ports/vcpkg-cmake-get-vars/cmake_get_vars/CMakeLists.txt
 create mode 100644 ports/vcpkg-cmake-get-vars/portfile.cmake
 create mode 100644 ports/vcpkg-cmake-get-vars/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-cmake-get-vars/vcpkg.json
 create mode 100644 ports/vcpkg-cmake-get-vars/vcpkg_cmake_get_vars.cmake
 create mode 100644 versions/v-/vcpkg-cmake-get-vars.json
2024-09-22 13:17:11,910 - 360 - WARNING - copy downloads/vcpkg/ports/openssl -> ./ports/openssl
2024-09-22 13:17:11,915 - 369 - WARNING - copy downloads/vcpkg/versions/o-/openssl.json -> ./versions/o-/openssl.json
2024-09-22 13:17:11,916 - 382 - INFO - openssl
commit 49e1e8f77565d452569f39e538b90cb9768e8b11
Author: Osyotr <Osyotr@users.noreply.github.com>
Date:   2024-09-10 23:45:18 +0300

    [openssl] Add upstream patch to fix build with old versions of perl (#40881)

 ports/openssl/portfile.cmake | 7 +++++++
 ports/openssl/vcpkg.json     | 1 +
 versions/baseline.json       | 2 +-
 versions/o-/openssl.json     | 5 +++++
 4 files changed, 14 insertions(+), 1 deletion(-)

2024-09-22 13:17:11,916 - 147 - INFO - run: git add .
2024-09-22 13:17:11,937 - 147 - INFO - run: git commit -m [openssl] Add upstream patch to fix build with old versions of perl (#40881) --author Osyotr <Osyotr@users.noreply.github.com>
[main 3138dc9c7] [openssl] Add upstream patch to fix build with old versions of perl (#40881)
 Author: Osyotr <Osyotr@users.noreply.github.com>
 21 files changed, 1441 insertions(+)
 create mode 100644 ports/openssl/asm-armcap.patch
 create mode 100644 ports/openssl/cmake-config.patch
 create mode 100644 ports/openssl/command-line-length.patch
 create mode 100644 ports/openssl/install-pc-files.cmake
 create mode 100644 ports/openssl/openssl.pc.in
 create mode 100644 ports/openssl/portfile.cmake
 create mode 100644 ports/openssl/script-prefix.patch
 create mode 100644 ports/openssl/unix/android-cc.patch
 create mode 100644 ports/openssl/unix/configure
 create mode 100644 ports/openssl/unix/move-openssldir.patch
 create mode 100644 ports/openssl/unix/no-empty-dirs.patch
 create mode 100644 ports/openssl/unix/no-static-libs-for-shared.patch
 create mode 100644 ports/openssl/unix/portfile.cmake
 create mode 100644 ports/openssl/unix/remove-deps.cmake
 create mode 100644 ports/openssl/usage
 create mode 100644 ports/openssl/vcpkg-cmake-wrapper.cmake.in
 create mode 100644 ports/openssl/vcpkg.json
 create mode 100644 ports/openssl/windows/install-layout.patch
 create mode 100644 ports/openssl/windows/install-pdbs.patch
 create mode 100644 ports/openssl/windows/portfile.cmake
 create mode 100644 versions/o-/openssl.json
PS D:\sources\MediaPorts\vcpkg-media-registry>
PS D:\sources\MediaPorts\vcpkg-media-registry> python pick_port.py --pick-port=boost
2024-09-22 13:17:23,378 - 91 - INFO - parse_cli_args
2024-09-22 13:17:23,379 - 396 - INFO - CliArgs(msft_vcpkg_root_dir='downloads/vcpkg', msft_vcpkg_url='https://github.com/microsoft/vcpkg.git', msft_vcpkg_branch='master', msft_vcpkg_baseline='98aa6396292d57e737a6ef999d4225ca488859d5', my_vcpkg_branch='main', pick_port='boost')
2024-09-22 13:17:23,379 - 287 - INFO - update_msft
2024-09-22 13:17:23,380 - 147 - INFO - run: git fetch
2024-09-22 13:17:24,248 - 147 - INFO - run: git rev-parse --abbrev-ref HEAD
2024-09-22 13:17:24,264 - 147 - INFO - run: git reset --hard 98aa6396292d57e737a6ef999d4225ca488859d5
HEAD is now at 98aa63962 [fast-double-parser] update to 0.8.0 (#40975)
2024-09-22 13:17:24,381 - 196 - WARNING - boost has 183 necessary ports: ["boost", "boost-accumulators", "boost-algorithm", "boost-align", "boost-any", "boost-array", "boost-asio", "boost-assert", "boost-assign", "boost-atomic", "boost-beast", "boost-bimap", "boost-bind", "boost-callable-traits", "boost-charconv", "boost-chrono", "boost-circular-buffer", "boost-cmake", "boost-cobalt", "boost-compat", "boost-compatibility", "boost-compute", "boost-concept-check", "boost-config", "boost-container", "boost-container-hash", "boost-context", "boost-contract", "boost-conversion", "boost-convert", "boost-core", "boost-coroutine", "boost-coroutine2", "boost-crc", "boost-date-time", "boost-describe", "boost-detail", "boost-dll", "boost-dynamic-bitset", "boost-endian", "boost-exception", "boost-fiber", "boost-filesystem", "boost-flyweight", "boost-foreach", "boost-format", "boost-function", "boost-function-types", "boost-functional", "boost-fusion", "boost-geometry", "boost-gil", "boost-graph", "boost-graph-parallel", "boost-hana", "boost-headers", "boost-heap", "boost-histogram", "boost-hof", "boost-icl", "boost-integer", "boost-interprocess", "boost-interval", "boost-intrusive", "boost-io", "boost-iostreams", "boost-iterator", "boost-json", "boost-lambda", "boost-lambda2", "boost-leaf", "boost-lexical-cast", "boost-local-function", "boost-locale", "boost-lockfree", "boost-log", "boost-logic", "boost-math", "boost-metaparse", "boost-move", "boost-mp11", "boost-mpi", "boost-mpl", "boost-msm", "boost-multi-array", "boost-multi-index", "boost-multiprecision", "boost-mysql", "boost-nowide", "boost-numeric-conversion", "boost-odeint", "boost-optional", "boost-outcome", "boost-parameter", "boost-parameter-python", "boost-pfr", "boost-phoenix", "boost-poly-collection", "boost-polygon", "boost-pool", "boost-predef", "boost-preprocessor", "boost-process", "boost-program-options", "boost-property-map", "boost-property-map-parallel", "boost-property-tree", "boost-proto", "boost-ptr-container", "boost-python", "boost-qvm", "boost-random", "boost-range", "boost-ratio", "boost-rational", "boost-redis", "boost-regex", "boost-safe-numerics", "boost-scope", "boost-scope-exit", "boost-serialization", "boost-signals2", "boost-smart-ptr", "boost-sort", "boost-spirit", "boost-stacktrace", "boost-statechart", "boost-static-assert", "boost-static-string", "boost-stl-interfaces", "boost-system", "boost-test", "boost-thread", "boost-throw-exception", "boost-timer", "boost-tokenizer", "boost-tti", "boost-tuple", "boost-type-erasure", "boost-type-index", "boost-type-traits", "boost-typeof", "boost-ublas", "boost-uninstall", "boost-units", "boost-unordered", "boost-url", "boost-utility", "boost-uuid", "boost-variant", "boost-variant2", "boost-vmd", "boost-wave", "boost-winapi", "boost-xpressive", "boost-yap", "bzip2", "expat", "gettext", "gettext-libintl", "icu", "libbacktrace", "libffi", "libiconv", "liblzma", "libuuid", "mpi", "msmpi", "openmpi", "openssl", "pkgconf", "python3", "sqlite3", "vcpkg-boost", "vcpkg-cmake", "vcpkg-cmake-config", "vcpkg-cmake-get-vars", "vcpkg-get-python", "vcpkg-msbuild", "vcpkg-pkgconfig-get-modules", "vcpkg-tool-meson", "zlib", "zstd"]
2024-09-22 13:18:44,728 - 147 - INFO - run: git checkout main
Already on 'main'
Your branch is ahead of 'origin/main' by 7 commits.
  (use "git push" to publish your local commits)
2024-09-22 13:18:44,784 - 360 - WARNING - copy downloads/vcpkg/ports/mpi -> ./ports/mpi
2024-09-22 13:18:44,786 - 369 - WARNING - copy downloads/vcpkg/versions/m-/mpi.json -> ./versions/m-/mpi.json
2024-09-22 13:18:44,787 - 382 - INFO - mpi
commit 75536e7c6186d3ab3a958e8f334591f40870bf45
Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
Date:   2022-05-26 20:05:01 +0000

    [mpi/msmpi] Add cmake wrapper to fix bug getting MPI_${LANG}_ADDITIONAL_INCLUDE_DIRS when calling FindMPI.cmake on Windows (#24746)

    * [mpi] Add cmake wrapper to fix bug getting MPI_${LANG}_ADDITIONAL_INCLUDE_DIRS when calling FindMPI.cmake

    * version

    * Move wrapper to msmpi, only copy the wrapper in the meta port installation

    * version

    * typo

    * version

    * Apply suggestion

    * version

    * move unset before _find_package

    * version

    * Add double quotes

    * version

    * Fix

    * version

    * Don't double quote list!

    * version

    * Apply suggestion

    * version

 ports/mpi/portfile.cmake      |  4 ++++
 ports/mpi/vcpkg.json          |  3 ++-
 ports/msmpi/mpi-wrapper.cmake |  9 +++++++++
 ports/msmpi/portfile.cmake    | 37 ++++++++++++++++++++-----------------
 ports/msmpi/vcpkg.json        |  2 +-
 versions/baseline.json        |  4 ++--
 versions/m-/mpi.json          |  5 +++++
 versions/m-/msmpi.json        |  5 +++++
 8 files changed, 48 insertions(+), 21 deletions(-)

2024-09-22 13:18:44,787 - 147 - INFO - run: git add .
2024-09-22 13:18:44,808 - 147 - INFO - run: git commit -m [mpi/msmpi] Add cmake wrapper to fix bug getting MPI_${LANG}_ADDITIONAL_INCLUDE_DIRS when calling FindMPI.cmake on Windows (#24746) --author Jack路Boos 路Yu <47264268+JackBoosY@users.noreply.github.com>
[main be35a5a57] [mpi/msmpi] Add cmake wrapper to fix bug getting MPI_${LANG}_ADDITIONAL_INCLUDE_DIRS when calling FindMPI.cmake on Windows (#24746)
 Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
 3 files changed, 52 insertions(+)
 create mode 100644 ports/mpi/portfile.cmake
 create mode 100644 ports/mpi/vcpkg.json
 create mode 100644 versions/m-/mpi.json
2024-09-22 13:18:44,918 - 360 - WARNING - copy downloads/vcpkg/ports/bzip2 -> ./ports/bzip2
2024-09-22 13:18:44,926 - 369 - WARNING - copy downloads/vcpkg/versions/b-/bzip2.json -> ./versions/b-/bzip2.json
2024-09-22 13:18:44,926 - 382 - INFO - bzip2
commit 5b11232d00476c66724c81adfe5e3777a9aec38f
Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
Date:   2023-04-13 18:13:15 +0200

    [many-ports] Don't use deprecated functions (autogenerated) (#26981)

    * [libuvc,qt5-virtualkeyboard] remove duplicated dependency entry

    * [many-ports] don't use deprecated functions (autogenerated)

    * atkmm: Fix license.
    gperftools: Reformat vcpkg_check_features call.
    gsl: Fix license.
    libpff: Fix license.
    pangomm: Fix license.
    qtbase: Revert, only comment changes.
    type-lite: Reformat vcpkg_check_features and actually use the feature options.

    ---------

    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/absent/vcpkg.json                      |   4 +-
 ports/activemq-cpp/portfile.cmake            |   4 +-
 ports/activemq-cpp/vcpkg.json                |   2 +-
 ports/alac-decoder/vcpkg.json                |   4 +-
 ports/alac/vcpkg.json                        |   4 +-
 ports/aliyun-oss-c-sdk/vcpkg.json            |   4 +-
 ports/angelscript/portfile.cmake             |   4 +-
 ports/angelscript/vcpkg.json                 |   1 +
 ports/argagg/vcpkg.json                      |   4 +-
 ports/asiosdk/portfile.cmake                 |   6 +-
 ports/asiosdk/vcpkg.json                     |   2 +-
 ports/asynch/vcpkg.json                      |   4 +-
 ports/atkmm/portfile.cmake                   |   4 +-
 ports/atkmm/vcpkg.json                       |   3 +-
 ports/atlmfc/vcpkg.json                      |   4 +-
 ports/aurora/vcpkg.json                      |   4 +-
 ports/autobahn/vcpkg.json                    |   4 +-
 ports/azure-kinect-sensor-sdk/portfile.cmake |   4 +-
 ports/azure-kinect-sensor-sdk/vcpkg.json     |   2 +-
 ports/azure-storage-cpp/vcpkg.json           |   4 +-
 ports/beast/vcpkg.json                       |   4 +-
 ports/binn/vcpkg.json                        |   4 +-
 ports/brigand/vcpkg.json                     |   4 +-
 ports/butteraugli/vcpkg.json                 |   4 +-
 ports/bzip2/portfile.cmake                   |   4 +-
 ports/bzip2/vcpkg.json                       |   2 +-
 ports/calceph/portfile.cmake                 |   4 +-
 ports/calceph/vcpkg.json                     |   1 +
 ports/catch-classic/vcpkg.json               |   4 +-
 ports/ccfits/portfile.cmake                  |   4 +-
 ports/ccfits/vcpkg.json                      |   2 +-
 ports/cctz/vcpkg.json                        |   4 +-
 ports/cgicc/vcpkg.json                       |   4 +-
 ports/chaiscript/vcpkg.json                  |   4 +-
 ports/chartdir/portfile.cmake                |  18 +-
 ports/chartdir/vcpkg.json                    |   2 +-
 ports/chipmunk/vcpkg.json                    |   4 +-
 ports/chmlib/portfile.cmake                  |   4 +-
 ports/chmlib/vcpkg.json                      |   2 +-
 ports/clara/vcpkg.json                       |   4 +-
 ports/cmcstl2/vcpkg.json                     |   4 +-
 ports/cmocka/vcpkg.json                      |   4 +-
 ports/cnl/vcpkg.json                         |   4 +-
 ports/coin/vcpkg.json                        |   4 +-
 ports/constexpr-contracts/vcpkg.json         |   4 +-
 ports/cpp-netlib/vcpkg.json                  |   4 +-
 ports/cpp-taskflow/vcpkg.json                |   4 +-
 ports/cppunit/portfile.cmake                 |   4 +-
 ports/cppunit/vcpkg.json                     |   2 +-
 ports/cr/vcpkg.json                          |   4 +-
 ports/cspice/portfile.cmake                  |   4 +-
 ports/cspice/vcpkg.json                      |   2 +-
 ports/ctbignum/vcpkg.json                    |   4 +-
 ports/ctp/portfile.cmake                     |  16 +-
 ports/ctp/vcpkg.json                         |   2 +-
 ports/cute-headers/vcpkg.json                |   4 +-
 ports/darknet/vcpkg.json                     |   2 +-
 ports/dbow2/vcpkg.json                       |   4 +-
 ports/debug-assert/vcpkg.json                |   4 +-
 ports/decimal-for-cpp/vcpkg.json             |   3 +-
 ports/directxsdk/portfile.cmake              |   4 +-
 ports/directxsdk/vcpkg.json                  |   2 +-
 ports/dirent/vcpkg.json                      |   4 +-
 ports/discord-rpc/vcpkg.json                 |   4 +-
 ports/discount/vcpkg.json                    |   4 +-
 ports/discreture/vcpkg.json                  |   4 +-
 ports/docopt/vcpkg.json                      |   4 +-
 ports/double-conversion/portfile.cmake       |   2 +-
 ports/double-conversion/vcpkg.json           |   1 +
 ports/duktape/vcpkg.json                     |   4 +-
 ports/dx/vcpkg.json                          |   4 +-
 ports/dxsdk-d3dx/portfile.cmake              |   4 +-
 ports/dxsdk-d3dx/vcpkg.json                  |   2 +-
 ports/easycl/vcpkg.json                      |   4 +-
 ports/eathread/portfile.cmake                |   7 +-
 ports/eathread/vcpkg.json                    |  12 +-
 ports/ecos/portfile.cmake                    |   7 +-
 ports/ecos/vcpkg.json                        |  16 +-
 ports/entityx/portfile.cmake                 |   5 +-
 ports/entityx/vcpkg.json                     |  12 +-
 ports/fadbad/portfile.cmake                  |   4 +-
 ports/fadbad/vcpkg.json                      |   4 +-
 ports/fastfeat/portfile.cmake                |   5 +-
 ports/fastfeat/vcpkg.json                    |  10 +-
 ports/fastlz/portfile.cmake                  |   5 +-
 ports/fastlz/vcpkg.json                      |   9 +-
 ports/fdlibm/portfile.cmake                  |   5 +-
 ports/fdlibm/vcpkg.json                      |  12 +-
 ports/fftw3/portfile.cmake                   |   4 +-
 ports/fftw3/vcpkg.json                       |   2 +-
 ports/flashlight-cpu/portfile.cmake          |   7 +-
 ports/flashlight-cpu/vcpkg.json              |  12 +-
 ports/flashlight-cuda/portfile.cmake         |   7 +-
 ports/flashlight-cuda/vcpkg.json             |  12 +-
 ports/flint/portfile.cmake                   |   4 +-
 ports/flint/vcpkg.json                       |   2 +-
 ports/fmem/portfile.cmake                    |   5 +-
 ports/fmem/vcpkg.json                        |  10 +-
 ports/foonathan-memory/portfile.cmake        |  11 +-
 ports/foonathan-memory/vcpkg.json            |  14 +-
 ports/fp16/portfile.cmake                    |   5 +-
 ports/fp16/vcpkg.json                        |   7 +-
 ports/freeopcua/portfile.cmake               |   7 +-
 ports/freeopcua/vcpkg.json                   |  14 +-
 ports/freexl/portfile.cmake                  |   4 +-
 ports/freexl/vcpkg.json                      |   2 +-
 ports/functions-framework-cpp/portfile.cmake |   7 +-
 ports/functions-framework-cpp/vcpkg.json     |  12 +-
 ports/fxdiv/portfile.cmake                   |   5 +-
 ports/fxdiv/vcpkg.json                       |  11 +-
 ports/g2o/portfile.cmake                     |   7 +-
 ports/g2o/vcpkg.json                         |  14 +-
 ports/gamma/portfile.cmake                   |   5 +-
 ports/gamma/vcpkg.json                       |   8 +-
 ports/gasol/portfile.cmake                   |   5 +-
 ports/gasol/vcpkg.json                       |  10 +-
 ports/gaussianlib/vcpkg.json                 |   4 +-
 ports/genann/portfile.cmake                  |   5 +-
 ports/genann/vcpkg.json                      |  12 +-
 ports/getopt/vcpkg.json                      |   4 +-
 ports/gettimeofday/portfile.cmake            |   5 +-
 ports/gettimeofday/vcpkg.json                |  12 +-
 ports/gflags/portfile.cmake                  |   7 +-
 ports/gflags/vcpkg.json                      |  16 +-
 ports/gl2ps/portfile.cmake                   |   5 +-
 ports/gl2ps/vcpkg.json                       |   8 +-
 ports/glew/portfile.cmake                    |   6 +-
 ports/glew/vcpkg.json                        |   3 +-
 ports/gli/portfile.cmake                     |   7 +-
 ports/gli/vcpkg.json                         |  11 +-
 ports/globjects/portfile.cmake               |   7 +-
 ports/globjects/vcpkg.json                   |  14 +-
 ports/gloo/portfile.cmake                    |   7 +-
 ports/gloo/vcpkg.json                        |  13 +-
 ports/glui/portfile.cmake                    |   7 +-
 ports/glui/vcpkg.json                        |  14 +-
 ports/gmime/portfile.cmake                   |  11 +-
 ports/gmime/vcpkg.json                       |   6 +-
 ports/gobject-introspection/portfile.cmake   |   4 +-
 ports/gobject-introspection/vcpkg.json       |   2 +-
 ports/gperf/portfile.cmake                   |   4 +-
 ports/gperf/vcpkg.json                       |   2 +-
 ports/gperftools/portfile.cmake              |   5 +-
 ports/gperftools/vcpkg.json                  |   2 +-
 ports/graphicsmagick/portfile.cmake          |   7 +-
 ports/graphicsmagick/vcpkg.json              |  10 +-
 ports/gsl/portfile.cmake                     |   4 +-
 ports/gsl/vcpkg.json                         |   4 +-
 ports/gtkmm/portfile.cmake                   |   4 +-
 ports/gtkmm/vcpkg.json                       |   1 +
 ports/gzip-hpp/vcpkg.json                    |   4 +-
 ports/h5py-lzf/portfile.cmake                |   7 +-
 ports/h5py-lzf/vcpkg.json                    |  14 +-
 ports/hayai/portfile.cmake                   |   9 +-
 ports/hayai/vcpkg.json                       |  16 +-
 ports/healpix/vcpkg.json                     |   4 +-
 ports/http-parser/portfile.cmake             |   7 +-
 ports/http-parser/vcpkg.json                 |  16 +-
 ports/hungarian/portfile.cmake               |  11 +-
 ports/hungarian/vcpkg.json                   |  14 +-
 ports/igloo/vcpkg.json                       |   4 +-
 ports/ijg-libjpeg/portfile.cmake             |   4 +-
 ports/ijg-libjpeg/vcpkg.json                 |   1 +
 ports/iniparser/portfile.cmake               |   7 +-
 ports/iniparser/vcpkg.json                   |  14 +-
 ports/intelrdfpmathlib/portfile.cmake        |   4 +-
 ports/intelrdfpmathlib/vcpkg.json            |   2 +-
 ports/io2d/portfile.cmake                    |   7 +-
 ports/io2d/vcpkg.json                        |  10 +-
 ports/irrlicht/vcpkg.json                    |   4 +-
 ports/irrxml/vcpkg.json                      |   3 +-
 ports/itpp/portfile.cmake                    |   5 +-
 ports/itpp/vcpkg.json                        |  10 +-
 ports/jbig2dec/portfile.cmake                |   5 +-
 ports/jbig2dec/vcpkg.json                    |  12 +-
 ports/jbigkit/portfile.cmake                 |  11 +-
 ports/jbigkit/vcpkg.json                     |  12 +-
 ports/jinja2cpplight/portfile.cmake          |   5 +-
 ports/jinja2cpplight/vcpkg.json              |  12 +-
 ports/josuttis-jthread/vcpkg.json            |   4 +-
 ports/jsmn/vcpkg.json                        |   4 +-
 ports/json-spirit/portfile.cmake             |   5 +-
 ports/json-spirit/vcpkg.json                 |  10 +-
 ports/json11/portfile.cmake                  |   5 +-
 ports/json11/vcpkg.json                      |  12 +-
 ports/json5-parser/portfile.cmake            |   7 +-
 ports/json5-parser/vcpkg.json                |  14 +-
 ports/kenlm/portfile.cmake                   |   7 +-
 ports/kenlm/vcpkg.json                       |   8 +-
 ports/kuku/portfile.cmake                    |   7 +-
 ports/kuku/vcpkg.json                        |  16 +-
 ports/kvasir-mpl/portfile.cmake              |   9 +-
 ports/kvasir-mpl/vcpkg.json                  |  14 +-
 ports/lapack/portfile.cmake                  |   2 +-
 ports/lapack/vcpkg.json                      |   5 +
 ports/leaf/vcpkg.json                        |   4 +-
 ports/lemon/vcpkg.json                       |   4 +-
 ports/lest/vcpkg.json                        |   4 +-
 ports/levmar/portfile.cmake                  |   9 +-
 ports/levmar/vcpkg.json                      |  10 +-
 ports/libaaplus/portfile.cmake               |   6 +-
 ports/libaaplus/vcpkg.json                   |   1 +
 ports/libaiff/portfile.cmake                 |   5 +-
 ports/libaiff/vcpkg.json                     |  12 +-
 ports/libcds/portfile.cmake                  |   7 +-
 ports/libcds/vcpkg.json                      |  12 +-
 ports/libcerf/portfile.cmake                 |   4 +-
 ports/libcerf/vcpkg.json                     |   2 +-
 ports/libconfig/portfile.cmake               |  10 +-
 ports/libconfig/vcpkg.json                   |  16 +-
 ports/libconfuse/vcpkg.json                  |   4 +-
 ports/libdisasm/vcpkg.json                   |   4 +-
 ports/libebur128/vcpkg.json                  |   4 +-
 ports/libftdi/vcpkg.json                     |   4 +-
 ports/libftdi1/portfile.cmake                |   6 +-
 ports/libftdi1/vcpkg.json                    |   2 +-
 ports/libgta/vcpkg.json                      |   4 +-
 ports/libguarded/vcpkg.json                  |   4 +-
 ports/libgwenhywfar/portfile.cmake           |   6 +-
 ports/libgwenhywfar/vcpkg.json               |   2 +-
 ports/libgxps/portfile.cmake                 |   6 +-
 ports/libgxps/vcpkg.json                     |   2 +-
 ports/liblas/portfile.cmake                  |   4 +-
 ports/liblas/vcpkg.json                      |   2 +-
 ports/liblemon/vcpkg.json                    |   4 +-
 ports/liblo/vcpkg.json                       |   4 +-
 ports/libmad/vcpkg.json                      |   4 +-
 ports/libmagic/vcpkg.json                    |   4 +-
 ports/libmaxminddb/vcpkg.json                |   4 +-
 ports/libmicrohttpd/portfile.cmake           |   4 +-
 ports/libmicrohttpd/vcpkg.json               |   1 +
 ports/libmodman/portfile.cmake               |   6 +-
 ports/libmodman/vcpkg.json                   |   4 +-
 ports/libmount/portfile.cmake                |   6 +-
 ports/libmount/vcpkg.json                    |   2 +-
 ports/libmspack/vcpkg.json                   |   4 +-
 ports/libodb-pgsql/portfile.cmake            |   4 +-
 ports/libodb-pgsql/vcpkg.json                |   2 +-
 ports/libopensp/portfile.cmake               |   6 +-
 ports/libopensp/vcpkg.json                   |   2 +-
 ports/libopusenc/vcpkg.json                  |   4 +-
 ports/libosip2/portfile.cmake                |   4 +-
 ports/libosip2/vcpkg.json                    |   2 +-
 ports/libosmscout/portfile.cmake             |   4 +-
 ports/libosmscout/vcpkg.json                 |   4 +-
 ports/libp7client/vcpkg.json                 |   4 +-
 ports/libpff/portfile.cmake                  |   6 +-
 ports/libpff/vcpkg.json                      |   3 +-
 ports/libpopt/vcpkg.json                     |   4 +-
 ports/libprotobuf-mutator/vcpkg.json         |   4 +-
 ports/librsvg/portfile.cmake                 |   4 +-
 ports/librsvg/vcpkg.json                     |   2 +-
 ports/librttopo/portfile.cmake               |   4 +-
 ports/librttopo/vcpkg.json                   |   2 +-
 ports/libspatialite/portfile.cmake           |   4 +-
 ports/libspatialite/vcpkg.json               |   2 +-
 ports/libstemmer/vcpkg.json                  |   4 +-
 ports/libstk/vcpkg.json                      |   4 +-
 ports/libtomcrypt/vcpkg.json                 |   4 +-
 ports/libtommath/vcpkg.json                  |   4 +-
 ports/libudns/vcpkg.json                     |   4 +-
 ports/libuvc/vcpkg.json                      |   3 +-
 ports/libvmdk/vcpkg.json                     |   4 +-
 ports/libxmlpp/portfile.cmake                |   4 +-
 ports/libxmlpp/vcpkg.json                    |   2 +-
 ports/libyaml/vcpkg.json                     |   4 +-
 ports/linalg/vcpkg.json                      |   4 +-
 ports/lpeg/vcpkg.json                        |   4 +-
 ports/lua/portfile.cmake                     |   4 +-
 ports/lua/vcpkg.json                         |   2 +-
 ports/luafilesystem/vcpkg.json               |   4 +-
 ports/lzfse/vcpkg.json                       |   4 +-
 ports/lzo/vcpkg.json                         |   4 +-
 ports/lzokay/vcpkg.json                      |   4 +-
 ports/magic-get/vcpkg.json                   |   4 +-
 ports/mapbox-variant/vcpkg.json              |   4 +-
 ports/mathc/vcpkg.json                       |   4 +-
 ports/matplotlib-cpp/vcpkg.json              |   4 +-
 ports/mcpp/vcpkg.json                        |   4 +-
 ports/mecab/vcpkg.json                       |   4 +-
 ports/memorymodule/vcpkg.json                |   4 +-
 ports/mikktspace/vcpkg.json                  |   4 +-
 ports/miniupnpc/vcpkg.json                   |   4 +-
 ports/moos-essential/vcpkg.json              |   4 +-
 ports/moos-ui/vcpkg.json                     |   4 +-
 ports/morton-nd/vcpkg.json                   |   4 +-
 ports/mpark-variant/vcpkg.json               |   4 +-
 ports/mpc/portfile.cmake                     |   4 +-
 ports/mpc/vcpkg.json                         |   2 +-
 ports/mpi/vcpkg.json                         |   4 +-
 ports/msinttypes/vcpkg.json                  |   4 +-
 ports/mstch/vcpkg.json                       |   4 +-
 ports/nana/vcpkg.json                        |   4 +-
 ports/nano-signal-slot/vcpkg.json            |   4 +-
 ports/nanoprintf/vcpkg.json                  |   4 +-
 ports/nanort/vcpkg.json                      |   4 +-
 ports/netcdf-cxx4/vcpkg.json                 |   4 +-
 ports/networkdirect-sdk/portfile.cmake       |   4 +-
 ports/networkdirect-sdk/vcpkg.json           |   2 +-
 ports/nmap/portfile.cmake                    |   4 +-
 ports/nmap/vcpkg.json                        |   2 +-
 ports/nngpp/vcpkg.json                       |   4 +-
 ports/nonius/vcpkg.json                      |   4 +-
 ports/nowide/portfile.cmake                  |   4 +-
 ports/nowide/vcpkg.json                      |   1 +
 ports/nspr/portfile.cmake                    |   6 +-
 ports/nspr/vcpkg.json                        |   2 +-
 ports/nss/portfile.cmake                     |   6 +-
 ports/nss/vcpkg.json                         |   1 +
 ports/nt-wrapper/vcpkg.json                  |   4 +-
 ports/observer-ptr-lite/vcpkg.json           |   4 +-
 ports/opencsg/vcpkg.json                     |   4 +-
 ports/opencv2/vcpkg.json                     |   2 +-
 ports/opencv3/vcpkg.json                     |   2 +-
 ports/opencv4/vcpkg.json                     |   2 +-
 ports/openigtlink/vcpkg.json                 |   4 +-
 ports/openldap/portfile.cmake                |   4 +-
 ports/openldap/vcpkg.json                    |   1 +
 ports/openmpi/portfile.cmake                 |   4 +-
 ports/openmpi/vcpkg.json                     |   2 +-
 ports/optional-bare/vcpkg.json               |   4 +-
 ports/p-ranav-csv/vcpkg.json                 |   4 +-
 ports/p-ranav-csv2/vcpkg.json                |   4 +-
 ports/pangomm/portfile.cmake                 |   4 +-
 ports/pangomm/vcpkg.json                     |   3 +-
 ports/parallelstl/vcpkg.json                 |   4 +-
 ports/parquet/vcpkg.json                     |   4 +-
 ports/pbc/portfile.cmake                     |   6 +-
 ports/pbc/vcpkg.json                         |   2 +-
 ports/pcapplusplus/vcpkg.json                |   3 +-
 ports/pcg/vcpkg.json                         |   4 +-
 ports/pdal-c/vcpkg.json                      |   3 +-
 ports/pdcurses/vcpkg.json                    |   4 +-
 ports/pdqsort/vcpkg.json                     |   4 +-
 ports/pegtl-2/vcpkg.json                     |   4 +-
 ports/pfultz2-linq/vcpkg.json                |   4 +-
 ports/picojson/vcpkg.json                    |   4 +-
 ports/picosha2/vcpkg.json                    |   4 +-
 ports/plf-list/vcpkg.json                    |   4 +-
 ports/plf-nanotimer/vcpkg.json               |   4 +-
 ports/plf-stack/vcpkg.json                   |   4 +-
 ports/plib/portfile.cmake                    |   4 +-
 ports/plib/vcpkg.json                        |   2 +-
 ports/plustache/vcpkg.json                   |   4 +-
 ports/pngpp/portfile.cmake                   |   4 +-
 ports/pngpp/vcpkg.json                       |   2 +-
 ports/pngwriter/vcpkg.json                   |   4 +-
 ports/polyclipping/vcpkg.json                |   4 +-
 ports/ponder/vcpkg.json                      |   4 +-
 ports/ppconsul/vcpkg.json                    |   4 +-
 ports/ppmagic/vcpkg.json                     |   4 +-
 ports/pprint/vcpkg.json                      |   4 +-
 ports/pqp/vcpkg.json                         |   4 +-
 ports/psimd/vcpkg.json                       |   4 +-
 ports/pthread/vcpkg.json                     |   4 +-
 ports/python2/portfile.cmake                 |   4 +-
 ports/python2/vcpkg.json                     |   2 +-
 ports/qt5-canvas3d/vcpkg.json                |   4 +-
 ports/qt5-virtualkeyboard/vcpkg.json         |   2 +-
 ports/quaternions/vcpkg.json                 |   4 +-
 ports/rabit/vcpkg.json                       |   4 +-
 ports/ragel/vcpkg.json                       |   4 +-
 ports/range-v3-vs2015/vcpkg.json             |   4 +-
 ports/rapidxml-ns/vcpkg.json                 |   4 +-
 ports/rapidxml/vcpkg.json                    |   4 +-
 ports/rappture/portfile.cmake                |   4 +-
 ports/rappture/vcpkg.json                    |   2 +-
 ports/readline/vcpkg.json                    |   4 +-
 ports/refprop-headers/vcpkg.json             |   4 +-
 ports/riffcpp/vcpkg.json                     |   4 +-
 ports/rply/vcpkg.json                        |   4 +-
 ports/sais/vcpkg.json                        |   4 +-
 ports/sajson/vcpkg.json                      |   4 +-
 ports/scintilla/portfile.cmake               |   6 +-
 ports/scintilla/vcpkg.json                   |   2 +-
 ports/scylla-wrapper/vcpkg.json              |   4 +-
 ports/sdl1-net/vcpkg.json                    |   4 +-
 ports/sdl2-gfx/vcpkg.json                    |   4 +-
 ports/septag-sx/vcpkg.json                   |   4 +-
 ports/seqan/portfile.cmake                   |   4 +-
 ports/seqan/vcpkg.json                       |   4 +-
 ports/serd/vcpkg.json                        |   4 +-
 ports/sf2cute/vcpkg.json                     |   4 +-
 ports/shapelib/portfile.cmake                |   4 +-
 ports/shapelib/vcpkg.json                    |   2 +-
 ports/shiftmedia-libgnutls/portfile.cmake    |   6 +-
 ports/shiftmedia-libgnutls/vcpkg.json        |   1 +
 ports/shiva-sfml/vcpkg.json                  |   4 +-
 ports/shogun/vcpkg.json                      |   4 +-
 ports/signalrclient/vcpkg.json               |   4 +-
 ports/sigslot/vcpkg.json                     |   4 +-
 ports/simple-fft/vcpkg.json                  |   4 +-
 ports/sltbench/vcpkg.json                    |   4 +-
 ports/smpeg2/vcpkg.json                      |   4 +-
 ports/sndfile/vcpkg.json                     |   4 +-
 ports/snowhouse/vcpkg.json                   |   4 +-
 ports/sokol/vcpkg.json                       |   4 +-
 ports/sord/vcpkg.json                        |   4 +-
 ports/spaceland/vcpkg.json                   |   4 +-
 ports/sparsepp/vcpkg.json                    |   4 +-
 ports/speexdsp/portfile.cmake                |   6 +-
 ports/speexdsp/vcpkg.json                    |   1 +
 ports/spirit-po/vcpkg.json                   |   4 +-
 ports/sprout/vcpkg.json                      |   4 +-
 ports/spscqueue/vcpkg.json                   |   4 +-
 ports/sqlite-modern-cpp/vcpkg.json           |   4 +-
 ports/sratom/vcpkg.json                      |   4 +-
 ports/starlink-ast/portfile.cmake            |   4 +-
 ports/starlink-ast/vcpkg.json                |   2 +-
 ports/status-value-lite/portfile.cmake       |   2 +-
 ports/status-value-lite/vcpkg.json           |   4 +-
 ports/stormlib/vcpkg.json                    |   4 +-
 ports/strict-variant/vcpkg.json              |   4 +-
 ports/strtk/vcpkg.json                       |   4 +-
 ports/systemc/vcpkg.json                     |   4 +-
 ports/szip/portfile.cmake                    |   6 +-
 ports/szip/vcpkg.json                        |   2 +-
 ports/tacopie/vcpkg.json                     |   4 +-
 ports/taocpp-json/vcpkg.json                 |   4 +-
 ports/tap-windows6/vcpkg.json                |   4 +-
 ports/telnetpp/vcpkg.json                    |   4 +-
 ports/tgc/vcpkg.json                         |   4 +-
 ports/threadpool/vcpkg.json                  |   4 +-
 ports/tiny-aes-c/vcpkg.json                  |   4 +-
 ports/tiny-bignum-c/vcpkg.json               |   4 +-
 ports/tiny-dnn/vcpkg.json                    |   4 +-
 ports/tiny-regex-c/vcpkg.json                |   4 +-
 ports/tinycthread/vcpkg.json                 |   4 +-
 ports/tinyexpr/vcpkg.json                    |   4 +-
 ports/tinynpy/vcpkg.json                     |   4 +-
 ports/tinythread/vcpkg.json                  |   4 +-
 ports/tinytoml/vcpkg.json                    |   4 +-
 ports/tinyxml/vcpkg.json                     |   4 +-
 ports/tl-function-ref/vcpkg.json             |   4 +-
 ports/tlx/vcpkg.json                         |   4 +-
 ports/treehopper/vcpkg.json                  |   4 +-
 ports/tsl-hopscotch-map/vcpkg.json           |   4 +-
 ports/tsl-ordered-map/vcpkg.json             |   4 +-
 ports/tsl-sparse-map/vcpkg.json              |   4 +-
 ports/type-lite/portfile.cmake               |  12 +-
 ports/type-lite/vcpkg.json                   |   4 +-
 ports/unqlite/vcpkg.json                     |   4 +-
 ports/unrar/portfile.cmake                   |   6 +-
 ports/unrar/vcpkg.json                       |   2 +-
 ports/utfz/vcpkg.json                        |   4 +-
 ports/visit-struct/vcpkg.json                |   4 +-
 ports/vlfeat/vcpkg.json                      |   4 +-
 ports/vs-yasm/vcpkg.json                     |   4 +-
 ports/webview2/portfile.cmake                |   6 +-
 ports/webview2/vcpkg.json                    |   1 +
 ports/wepoll/vcpkg.json                      |   4 +-
 ports/wg21-sg14/vcpkg.json                   |   4 +-
 ports/winpcap/portfile.cmake                 |   6 +-
 ports/winpcap/vcpkg.json                     |   2 +-
 ports/winsparkle/portfile.cmake              |   4 +-
 ports/winsparkle/vcpkg.json                  |   2 +-
 ports/wordnet/vcpkg.json                     |   4 +-
 ports/x-plane/portfile.cmake                 |   4 +-
 ports/x-plane/vcpkg.json                     |   2 +-
 ports/xframe/vcpkg.json                      |   4 +-
 ports/xproperty/vcpkg.json                   |   4 +-
 ports/xqilla/portfile.cmake                  |   4 +-
 ports/xqilla/vcpkg.json                      |   2 +-
 ports/xtensor-fftw/vcpkg.json                |   4 +-
 ports/yajl/vcpkg.json                        |   4 +-
 ports/yomm2/vcpkg.json                       |   4 +-
 ports/z85/vcpkg.json                         |   4 +-
 ports/zookeeper/portfile.cmake               |   4 +-
 ports/zookeeper/vcpkg.json                   |   1 +
 ports/zyre/vcpkg.json                        |   4 +-
 versions/a-/absent.json                      |   5 +
 versions/a-/activemq-cpp.json                |   5 +
 versions/a-/alac-decoder.json                |   5 +
 versions/a-/alac.json                        |   5 +
 versions/a-/aliyun-oss-c-sdk.json            |   5 +
 versions/a-/angelscript.json                 |   5 +
 versions/a-/argagg.json                      |   5 +
 versions/a-/asiosdk.json                     |   5 +
 versions/a-/asynch.json                      |   5 +
 versions/a-/atkmm.json                       |   5 +
 versions/a-/atlmfc.json                      |   5 +
 versions/a-/aurora.json                      |   5 +
 versions/a-/autobahn.json                    |   5 +
 versions/a-/azure-kinect-sensor-sdk.json     |   5 +
 versions/a-/azure-storage-cpp.json           |   5 +
 versions/b-/beast.json                       |   5 +
 versions/b-/binn.json                        |   5 +
 versions/b-/brigand.json                     |   5 +
 versions/b-/butteraugli.json                 |   5 +
 versions/b-/bzip2.json                       |   5 +
 versions/baseline.json                       | 690 +++++++++++++--------------
 versions/c-/calceph.json                     |   5 +
 versions/c-/catch-classic.json               |   5 +
 versions/c-/ccfits.json                      |   5 +
 versions/c-/cctz.json                        |   5 +
 versions/c-/cgicc.json                       |   5 +
 versions/c-/chaiscript.json                  |   5 +
 versions/c-/chartdir.json                    |   5 +
 versions/c-/chipmunk.json                    |   5 +
 versions/c-/chmlib.json                      |   5 +
 versions/c-/clara.json                       |   5 +
 versions/c-/cmcstl2.json                     |   5 +
 versions/c-/cmocka.json                      |   5 +
 versions/c-/cnl.json                         |   5 +
 versions/c-/coin.json                        |   5 +
 versions/c-/constexpr-contracts.json         |   5 +
 versions/c-/cpp-netlib.json                  |   5 +
 versions/c-/cpp-taskflow.json                |   5 +
 versions/c-/cppunit.json                     |   5 +
 versions/c-/cr.json                          |   5 +
 versions/c-/cspice.json                      |   5 +
 versions/c-/ctbignum.json                    |   5 +
 versions/c-/ctp.json                         |   5 +
 versions/c-/cute-headers.json                |   5 +
 versions/d-/darknet.json                     |   5 +
 versions/d-/dbow2.json                       |   5 +
 versions/d-/debug-assert.json                |   5 +
 versions/d-/decimal-for-cpp.json             |   5 +
 versions/d-/directxsdk.json                  |   5 +
 versions/d-/dirent.json                      |   5 +
 versions/d-/discord-rpc.json                 |   5 +
 versions/d-/discount.json                    |   5 +
 versions/d-/discreture.json                  |   5 +
 versions/d-/docopt.json                      |   5 +
 versions/d-/double-conversion.json           |   5 +
 versions/d-/duktape.json                     |   5 +
 versions/d-/dx.json                          |   5 +
 versions/d-/dxsdk-d3dx.json                  |   5 +
 versions/e-/easycl.json                      |   5 +
 versions/e-/eathread.json                    |   5 +
 versions/e-/ecos.json                        |   5 +
 versions/e-/entityx.json                     |   5 +
 versions/f-/fadbad.json                      |   5 +
 versions/f-/fastfeat.json                    |   5 +
 versions/f-/fastlz.json                      |   5 +
 versions/f-/fdlibm.json                      |   5 +
 versions/f-/fftw3.json                       |   5 +
 versions/f-/flashlight-cpu.json              |   5 +
 versions/f-/flashlight-cuda.json             |   5 +
 versions/f-/flint.json                       |   5 +
 versions/f-/fmem.json                        |   5 +
 versions/f-/foonathan-memory.json            |   5 +
 versions/f-/fp16.json                        |   5 +
 versions/f-/freeopcua.json                   |   5 +
 versions/f-/freexl.json                      |   5 +
 versions/f-/functions-framework-cpp.json     |   5 +
 versions/f-/fxdiv.json                       |   5 +
 versions/g-/g2o.json                         |   5 +
 versions/g-/gamma.json                       |   5 +
 versions/g-/gasol.json                       |   5 +
 versions/g-/gaussianlib.json                 |   5 +
 versions/g-/genann.json                      |   5 +
 versions/g-/getopt.json                      |   5 +
 versions/g-/gettimeofday.json                |   5 +
 versions/g-/gflags.json                      |   5 +
 versions/g-/gl2ps.json                       |   5 +
 versions/g-/glew.json                        |   5 +
 versions/g-/gli.json                         |   5 +
 versions/g-/globjects.json                   |   5 +
 versions/g-/gloo.json                        |   5 +
 versions/g-/glui.json                        |   5 +
 versions/g-/gmime.json                       |   5 +
 versions/g-/gobject-introspection.json       |   5 +
 versions/g-/gperf.json                       |   5 +
 versions/g-/gperftools.json                  |   5 +
 versions/g-/graphicsmagick.json              |   5 +
 versions/g-/gsl.json                         |   5 +
 versions/g-/gtkmm.json                       |   5 +
 versions/g-/gzip-hpp.json                    |   5 +
 versions/h-/h5py-lzf.json                    |   5 +
 versions/h-/hayai.json                       |   5 +
 versions/h-/healpix.json                     |   5 +
 versions/h-/http-parser.json                 |   5 +
 versions/h-/hungarian.json                   |   5 +
 versions/i-/igloo.json                       |   5 +
 versions/i-/ijg-libjpeg.json                 |   5 +
 versions/i-/iniparser.json                   |   5 +
 versions/i-/intelrdfpmathlib.json            |   5 +
 versions/i-/io2d.json                        |   5 +
 versions/i-/irrlicht.json                    |   5 +
 versions/i-/irrxml.json                      |   5 +
 versions/i-/itpp.json                        |   5 +
 versions/j-/jbig2dec.json                    |   5 +
 versions/j-/jbigkit.json                     |   5 +
 versions/j-/jinja2cpplight.json              |   5 +
 versions/j-/josuttis-jthread.json            |   5 +
 versions/j-/jsmn.json                        |   5 +
 versions/j-/json-spirit.json                 |   5 +
 versions/j-/json11.json                      |   5 +
 versions/j-/json5-parser.json                |   5 +
 versions/k-/kenlm.json                       |   5 +
 versions/k-/kuku.json                        |   5 +
 versions/k-/kvasir-mpl.json                  |   5 +
 versions/l-/lapack.json                      |   5 +
 versions/l-/leaf.json                        |   5 +
 versions/l-/lemon.json                       |   5 +
 versions/l-/lest.json                        |   5 +
 versions/l-/levmar.json                      |   5 +
 versions/l-/libaaplus.json                   |   5 +
 versions/l-/libaiff.json                     |   5 +
 versions/l-/libcds.json                      |   5 +
 versions/l-/libcerf.json                     |   5 +
 versions/l-/libconfig.json                   |   5 +
 versions/l-/libconfuse.json                  |   5 +
 versions/l-/libdisasm.json                   |   5 +
 versions/l-/libebur128.json                  |   5 +
 versions/l-/libftdi.json                     |   5 +
 versions/l-/libftdi1.json                    |   5 +
 versions/l-/libgta.json                      |   5 +
 versions/l-/libguarded.json                  |   5 +
 versions/l-/libgwenhywfar.json               |   5 +
 versions/l-/libgxps.json                     |   5 +
 versions/l-/liblas.json                      |   5 +
 versions/l-/liblemon.json                    |   5 +
 versions/l-/liblo.json                       |   5 +
 versions/l-/libmad.json                      |   5 +
 versions/l-/libmagic.json                    |   5 +
 versions/l-/libmaxminddb.json                |   5 +
 versions/l-/libmicrohttpd.json               |   5 +
 versions/l-/libmodman.json                   |   5 +
 versions/l-/libmount.json                    |   5 +
 versions/l-/libmspack.json                   |   5 +
 versions/l-/libodb-pgsql.json                |   5 +
 versions/l-/libopensp.json                   |   5 +
 versions/l-/libopusenc.json                  |   5 +
 versions/l-/libosip2.json                    |   5 +
 versions/l-/libosmscout.json                 |   5 +
 versions/l-/libp7client.json                 |   5 +
 versions/l-/libpff.json                      |   5 +
 versions/l-/libpopt.json                     |   5 +
 versions/l-/libprotobuf-mutator.json         |   5 +
 versions/l-/librsvg.json                     |   5 +
 versions/l-/librttopo.json                   |   5 +
 versions/l-/libspatialite.json               |   5 +
 versions/l-/libstemmer.json                  |   5 +
 versions/l-/libstk.json                      |   5 +
 versions/l-/libtomcrypt.json                 |   5 +
 versions/l-/libtommath.json                  |   5 +
 versions/l-/libudns.json                     |   5 +
 versions/l-/libuvc.json                      |   5 +
 versions/l-/libvmdk.json                     |   5 +
 versions/l-/libxmlpp.json                    |   5 +
 versions/l-/libyaml.json                     |   5 +
 versions/l-/linalg.json                      |   5 +
 versions/l-/lpeg.json                        |   5 +
 versions/l-/lua.json                         |   5 +
 versions/l-/luafilesystem.json               |   5 +
 versions/l-/lzfse.json                       |   5 +
 versions/l-/lzo.json                         |   5 +
 versions/l-/lzokay.json                      |   5 +
 versions/m-/magic-get.json                   |   5 +
 versions/m-/mapbox-variant.json              |   5 +
 versions/m-/mathc.json                       |   5 +
 versions/m-/matplotlib-cpp.json              |   5 +
 versions/m-/mcpp.json                        |   5 +
 versions/m-/mecab.json                       |   5 +
 versions/m-/memorymodule.json                |   5 +
 versions/m-/mikktspace.json                  |   5 +
 versions/m-/miniupnpc.json                   |   5 +
 versions/m-/moos-essential.json              |   5 +
 versions/m-/moos-ui.json                     |   5 +
 versions/m-/morton-nd.json                   |   5 +
 versions/m-/mpark-variant.json               |   5 +
 versions/m-/mpc.json                         |   5 +
 versions/m-/mpi.json                         |   5 +
 versions/m-/msinttypes.json                  |   5 +
 versions/m-/mstch.json                       |   5 +
 versions/n-/nana.json                        |   5 +
 versions/n-/nano-signal-slot.json            |   5 +
 versions/n-/nanoprintf.json                  |   5 +
 versions/n-/nanort.json                      |   5 +
 versions/n-/netcdf-cxx4.json                 |   5 +
 versions/n-/networkdirect-sdk.json           |   5 +
 versions/n-/nmap.json                        |   5 +
 versions/n-/nngpp.json                       |   5 +
 versions/n-/nonius.json                      |   5 +
 versions/n-/nowide.json                      |   5 +
 versions/n-/nspr.json                        |   5 +
 versions/n-/nss.json                         |   5 +
 versions/n-/nt-wrapper.json                  |   5 +
 versions/o-/observer-ptr-lite.json           |   5 +
 versions/o-/opencsg.json                     |   5 +
 versions/o-/opencv2.json                     |   5 +
 versions/o-/opencv3.json                     |   5 +
 versions/o-/opencv4.json                     |   5 +
 versions/o-/openigtlink.json                 |   5 +
 versions/o-/openldap.json                    |   5 +
 versions/o-/openmpi.json                     |   5 +
 versions/o-/optional-bare.json               |   5 +
 versions/p-/p-ranav-csv.json                 |   5 +
 versions/p-/p-ranav-csv2.json                |   5 +
 versions/p-/pangomm.json                     |   5 +
 versions/p-/parallelstl.json                 |   5 +
 versions/p-/parquet.json                     |   5 +
 versions/p-/pbc.json                         |   5 +
 versions/p-/pcapplusplus.json                |   5 +
 versions/p-/pcg.json                         |   5 +
 versions/p-/pdal-c.json                      |   5 +
 versions/p-/pdcurses.json                    |   5 +
 versions/p-/pdqsort.json                     |   5 +
 versions/p-/pegtl-2.json                     |   5 +
 versions/p-/pfultz2-linq.json                |   5 +
 versions/p-/picojson.json                    |   5 +
 versions/p-/picosha2.json                    |   5 +
 versions/p-/plf-list.json                    |   5 +
 versions/p-/plf-nanotimer.json               |   5 +
 versions/p-/plf-stack.json                   |   5 +
 versions/p-/plib.json                        |   5 +
 versions/p-/plustache.json                   |   5 +
 versions/p-/pngpp.json                       |   5 +
 versions/p-/pngwriter.json                   |   5 +
 versions/p-/polyclipping.json                |   5 +
 versions/p-/ponder.json                      |   5 +
 versions/p-/ppconsul.json                    |   5 +
 versions/p-/ppmagic.json                     |   5 +
 versions/p-/pprint.json                      |   5 +
 versions/p-/pqp.json                         |   5 +
 versions/p-/psimd.json                       |   5 +
 versions/p-/pthread.json                     |   5 +
 versions/p-/python2.json                     |   5 +
 versions/q-/qt5-canvas3d.json                |   5 +
 versions/q-/qt5-virtualkeyboard.json         |   5 +
 versions/q-/quaternions.json                 |   5 +
 versions/r-/rabit.json                       |   5 +
 versions/r-/ragel.json                       |   5 +
 versions/r-/range-v3-vs2015.json             |   5 +
 versions/r-/rapidxml-ns.json                 |   5 +
 versions/r-/rapidxml.json                    |   5 +
 versions/r-/rappture.json                    |   5 +
 versions/r-/readline.json                    |   5 +
 versions/r-/refprop-headers.json             |   5 +
 versions/r-/riffcpp.json                     |   5 +
 versions/r-/rply.json                        |   5 +
 versions/s-/sais.json                        |   5 +
 versions/s-/sajson.json                      |   5 +
 versions/s-/scintilla.json                   |   5 +
 versions/s-/scylla-wrapper.json              |   5 +
 versions/s-/sdl1-net.json                    |   5 +
 versions/s-/sdl2-gfx.json                    |   5 +
 versions/s-/septag-sx.json                   |   5 +
 versions/s-/seqan.json                       |   5 +
 versions/s-/serd.json                        |   5 +
 versions/s-/sf2cute.json                     |   5 +
 versions/s-/shapelib.json                    |   5 +
 versions/s-/shiftmedia-libgnutls.json        |   5 +
 versions/s-/shiva-sfml.json                  |   5 +
 versions/s-/shogun.json                      |   5 +
 versions/s-/signalrclient.json               |   5 +
 versions/s-/sigslot.json                     |   5 +
 versions/s-/simple-fft.json                  |   5 +
 versions/s-/sltbench.json                    |   5 +
 versions/s-/smpeg2.json                      |   5 +
 versions/s-/sndfile.json                     |   5 +
 versions/s-/snowhouse.json                   |   5 +
 versions/s-/sokol.json                       |   5 +
 versions/s-/sord.json                        |   5 +
 versions/s-/spaceland.json                   |   5 +
 versions/s-/sparsepp.json                    |   5 +
 versions/s-/speexdsp.json                    |   5 +
 versions/s-/spirit-po.json                   |   5 +
 versions/s-/sprout.json                      |   5 +
 versions/s-/spscqueue.json                   |   5 +
 versions/s-/sqlite-modern-cpp.json           |   5 +
 versions/s-/sratom.json                      |   5 +
 versions/s-/starlink-ast.json                |   5 +
 versions/s-/status-value-lite.json           |   5 +
 versions/s-/stormlib.json                    |   5 +
 versions/s-/strict-variant.json              |   5 +
 versions/s-/strtk.json                       |   5 +
 versions/s-/systemc.json                     |   5 +
 versions/s-/szip.json                        |   5 +
 versions/t-/tacopie.json                     |   5 +
 versions/t-/taocpp-json.json                 |   5 +
 versions/t-/tap-windows6.json                |   5 +
 versions/t-/telnetpp.json                    |   5 +
 versions/t-/tgc.json                         |   5 +
 versions/t-/threadpool.json                  |   5 +
 versions/t-/tiny-aes-c.json                  |   5 +
 versions/t-/tiny-bignum-c.json               |   5 +
 versions/t-/tiny-dnn.json                    |   5 +
 versions/t-/tiny-regex-c.json                |   5 +
 versions/t-/tinycthread.json                 |   5 +
 versions/t-/tinyexpr.json                    |   5 +
 versions/t-/tinynpy.json                     |   5 +
 versions/t-/tinythread.json                  |   5 +
 versions/t-/tinytoml.json                    |   5 +
 versions/t-/tinyxml.json                     |   5 +
 versions/t-/tl-function-ref.json             |   5 +
 versions/t-/tlx.json                         |   5 +
 versions/t-/treehopper.json                  |   5 +
 versions/t-/tsl-hopscotch-map.json           |   5 +
 versions/t-/tsl-ordered-map.json             |   5 +
 versions/t-/tsl-sparse-map.json              |   5 +
 versions/t-/type-lite.json                   |   5 +
 versions/u-/unqlite.json                     |   5 +
 versions/u-/unrar.json                       |   5 +
 versions/u-/utfz.json                        |   5 +
 versions/v-/visit-struct.json                |   5 +
 versions/v-/vlfeat.json                      |   5 +
 versions/v-/vs-yasm.json                     |   5 +
 versions/w-/webview2.json                    |   5 +
 versions/w-/wepoll.json                      |   5 +
 versions/w-/wg21-sg14.json                   |   5 +
 versions/w-/winpcap.json                     |   5 +
 versions/w-/winsparkle.json                  |   5 +
 versions/w-/wordnet.json                     |   5 +
 versions/x-/x-plane.json                     |   5 +
 versions/x-/xframe.json                      |   5 +
 versions/x-/xproperty.json                   |   5 +
 versions/x-/xqilla.json                      |   5 +
 versions/x-/xtensor-fftw.json                |   5 +
 versions/y-/yajl.json                        |   5 +
 versions/y-/yomm2.json                       |   5 +
 versions/z-/z85.json                         |   5 +
 versions/z-/zookeeper.json                   |   5 +
 versions/z-/zyre.json                        |   5 +
 816 files changed, 3382 insertions(+), 1325 deletions(-)

2024-09-22 13:18:44,930 - 147 - INFO - run: git add .
2024-09-22 13:18:44,954 - 147 - INFO - run: git commit -m [many-ports] Don't use deprecated functions (autogenerated) (#26981) --author autoantwort <41973254+autoantwort@users.noreply.github.com>
[main 5e93446e0] [many-ports] Don't use deprecated functions (autogenerated) (#26981)
 Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
 7 files changed, 259 insertions(+)
 create mode 100644 ports/bzip2/CMakeLists.txt
 create mode 100644 ports/bzip2/bzip2.pc.in
 create mode 100644 ports/bzip2/fix-import-export-macros.patch
 create mode 100644 ports/bzip2/portfile.cmake
 create mode 100644 ports/bzip2/usage
 create mode 100644 ports/bzip2/vcpkg.json
 create mode 100644 versions/b-/bzip2.json
2024-09-22 13:18:45,022 - 360 - WARNING - copy downloads/vcpkg/ports/libuuid -> ./ports/libuuid
2024-09-22 13:18:45,025 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libuuid.json -> ./versions/l-/libuuid.json
2024-09-22 13:18:45,026 - 382 - INFO - libuuid
commit 854c5cab1a1325fc1d87db3809265c90df26c678
Author: Marc <31337222+marcbull@users.noreply.github.com>
Date:   2023-07-11 21:35:06 +0200

    [libuuid] add license id and use vcpkg_install_copyright() (#32504)

    * [libuuid] add license id and use vcpkg_install_copyright()

    * Update version database

 ports/libuuid/portfile.cmake | 4 +---
 ports/libuuid/vcpkg.json     | 3 ++-
 versions/baseline.json       | 2 +-
 versions/l-/libuuid.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:18:45,026 - 147 - INFO - run: git add .
2024-09-22 13:18:45,046 - 147 - INFO - run: git commit -m [libuuid] add license id and use vcpkg_install_copyright() (#32504) --author Marc <31337222+marcbull@users.noreply.github.com>
[main 3cc45a1f4] [libuuid] add license id and use vcpkg_install_copyright() (#32504)
 Author: Marc <31337222+marcbull@users.noreply.github.com>
 6 files changed, 213 insertions(+)
 create mode 100644 ports/libuuid/CMakeLists.txt
 create mode 100644 ports/libuuid/config.linux.h
 create mode 100644 ports/libuuid/portfile.cmake
 create mode 100644 ports/libuuid/unofficial-libuuid-config.cmake.in
 create mode 100644 ports/libuuid/vcpkg.json
 create mode 100644 versions/l-/libuuid.json
2024-09-22 13:18:45,109 - 360 - WARNING - copy downloads/vcpkg/ports/python3 -> ./ports/python3
2024-09-22 13:18:45,119 - 369 - WARNING - copy downloads/vcpkg/versions/p-/python3.json -> ./versions/p-/python3.json
2024-09-22 13:18:45,119 - 382 - INFO - python3
commit 27276976cabb284d855893d641a64c0304e87ffa
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2023-08-09 19:29:22 +0200

    [3fd|python3] switch to vcpkg-msbuild (#33026)

    * [python3] switch to vcpkg-msbuild

    * v db

    * update 3fd to use vcpkg-msbuild as a sanity check

    * Fix windows cross builds

    * v db

    * arm needs another patch

    * v db

    * 3fd uwp msbuild_install

    * v db

 ports/3fd/portfile.cmake                        | 26 ++++++------
 ports/3fd/vcpkg.json                            |  9 ++++-
 ports/python3/0015-dont-use-WINDOWS-def.patch   | 13 ++++++
 ports/python3/0016-fix-win-cross.patch          | 34 ++++++++++++++++
 ports/python3/openssl.props.in                  |  9 +++++
 ports/python3/portfile.cmake                    | 53 +++++++++++++++----------
 ports/python3/python_vcpkg.props.in             | 21 +++++++---
 ports/python3/vcpkg.json                        |  6 +++
 ports/vcpkg-msbuild/vcpkg.json                  |  2 +-
 ports/vcpkg-msbuild/vcpkg_msbuild_install.cmake | 31 ++++++++++++++-
 versions/3-/3fd.json                            |  5 +++
 versions/baseline.json                          |  6 +--
 versions/p-/python3.json                        |  5 +++
 versions/v-/vcpkg-msbuild.json                  |  5 +++
 14 files changed, 176 insertions(+), 49 deletions(-)

2024-09-22 13:18:45,120 - 147 - INFO - run: git add .
2024-09-22 13:18:45,141 - 147 - INFO - run: git commit -m [3fd|python3] switch to vcpkg-msbuild (#33026) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main 07511277b] [3fd|python3] switch to vcpkg-msbuild (#33026)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 27 files changed, 2109 insertions(+)
 create mode 100644 ports/python3/0001-only-build-required-projects.patch
 create mode 100644 ports/python3/0002-static-library.patch
 create mode 100644 ports/python3/0003-use-vcpkg-zlib.patch
 create mode 100644 ports/python3/0004-devendor-external-dependencies.patch
 create mode 100644 ports/python3/0005-dont-copy-vcruntime.patch
 create mode 100644 ports/python3/0006-restore-support-for-windows-7.patch
 create mode 100644 ports/python3/0007-workaround-windows-11-sdk-rc-compiler-error.patch
 create mode 100644 ports/python3/0008-python.pc.patch
 create mode 100644 ports/python3/0010-dont-skip-rpath.patch
 create mode 100644 ports/python3/0011-gcc-ldflags-fix.patch
 create mode 100644 ports/python3/0012-force-disable-modules.patch
 create mode 100644 ports/python3/0014-fix-get-python-inc-output.patch
 create mode 100644 ports/python3/0015-dont-use-WINDOWS-def.patch
 create mode 100644 ports/python3/0016-fix-win-cross.patch
 create mode 100644 ports/python3/0016-undup-ffi-symbols.patch
 create mode 100644 ports/python3/0017-fix-win.patch
 create mode 100644 ports/python3/0018-fix-sysconfig-include.patch
 create mode 100644 ports/python3/openssl.props.in
 create mode 100644 ports/python3/portfile.cmake
 create mode 100644 ports/python3/python_vcpkg.props.in
 create mode 100644 ports/python3/usage
 create mode 100644 ports/python3/usage.unix
 create mode 100644 ports/python3/usage.win
 create mode 100644 ports/python3/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/python3/vcpkg-port-config.cmake
 create mode 100644 ports/python3/vcpkg.json
 create mode 100644 versions/p-/python3.json
2024-09-22 13:18:45,203 - 360 - WARNING - copy downloads/vcpkg/ports/openmpi -> ./ports/openmpi
2024-09-22 13:18:45,204 - 369 - WARNING - copy downloads/vcpkg/versions/o-/openmpi.json -> ./versions/o-/openmpi.json
2024-09-22 13:18:45,204 - 382 - INFO - openmpi
commit 9b9ec90df40cdd3877b43c11f15a9967231794b0
Author: 脫mar H枚gni Gu冒marsson <ohg@skaginn3x.com>
Date:   2023-12-18 21:17:23 +0000

    [Openmpi] configuration error (#35706)

 ports/openmpi/portfile.cmake | 1 +
 ports/openmpi/vcpkg.json     | 1 +
 versions/baseline.json       | 2 +-
 versions/o-/openmpi.json     | 5 +++++
 4 files changed, 8 insertions(+), 1 deletion(-)

2024-09-22 13:18:45,204 - 147 - INFO - run: git add .
2024-09-22 13:18:45,226 - 147 - INFO - run: git commit -m [Openmpi] configuration error (#35706) --author 脫mar H枚gni Gu冒marsson <ohg@skaginn3x.com>
[main 4d0efde0c] [Openmpi] configuration error (#35706)
 Author: 脫mar H枚gni Gu冒marsson <ohg@skaginn3x.com>
 4 files changed, 406 insertions(+)
 create mode 100644 ports/openmpi/keep_isystem.patch
 create mode 100644 ports/openmpi/portfile.cmake
 create mode 100644 ports/openmpi/vcpkg.json
 create mode 100644 versions/o-/openmpi.json
2024-09-22 13:18:45,291 - 360 - WARNING - copy downloads/vcpkg/ports/libbacktrace -> ./ports/libbacktrace
2024-09-22 13:18:45,292 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libbacktrace.json -> ./versions/l-/libbacktrace.json
2024-09-22 13:18:45,293 - 382 - INFO - libbacktrace
commit bbbdfc30f71dce37029a2c78ff55367b35ff4001
Author: Bruce Mitchener <bruce.mitchener@gmail.com>
Date:   2024-01-20 02:56:53 +0700

    [libbacktrace] Update to commit from 2023-11-30. (#36238)

 ports/libbacktrace/portfile.cmake | 4 ++--
 ports/libbacktrace/vcpkg.json     | 3 +--
 versions/baseline.json            | 4 ++--
 versions/l-/libbacktrace.json     | 5 +++++
 4 files changed, 10 insertions(+), 6 deletions(-)

2024-09-22 13:18:45,293 - 147 - INFO - run: git add .
2024-09-22 13:18:45,314 - 147 - INFO - run: git commit -m [libbacktrace] Update to commit from 2023-11-30. (#36238) --author Bruce Mitchener <bruce.mitchener@gmail.com>
[main 70c3c976d] [libbacktrace] Update to commit from 2023-11-30. (#36238)
 Author: Bruce Mitchener <bruce.mitchener@gmail.com>
 3 files changed, 45 insertions(+)
 create mode 100644 ports/libbacktrace/portfile.cmake
 create mode 100644 ports/libbacktrace/vcpkg.json
 create mode 100644 versions/l-/libbacktrace.json
2024-09-22 13:18:45,393 - 360 - WARNING - copy downloads/vcpkg/ports/boost-accumulators -> ./ports/boost-accumulators
2024-09-22 13:18:45,394 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-accumulators.json -> ./versions/b-/boost-accumulators.json
2024-09-22 13:18:45,396 - 382 - INFO - boost-accumulators
commit 8ccb84df727bdf83045e53c319af05c554838b80
Author: Yury Bura <yurybura@gmail.com>
Date:   2024-01-22 19:56:30 +0100

    [boost] Update to v1.84.0 (#35693)

    * [scripts] update Boost ports generation script, fixes #35187

    * [boost] remove obsolete patches and re-generate ports

    * update versions

    * [boost] remove redundant vcpkg_minimum_required

    * update versions

    * [scripts/boost] update dependencies to config/checks, review b2-options.cmake files

    * [boost-*] regenerate ports

    * [boost-locale] fix patch

    * update versions

    * [boost-serialization] fix checks

    * update version

    * [boost-*] better fixes related to the config checks

    * update version

    * [boost-cobalt] fix build

    * update versions

    * [liblas] Boost v1.84.0 requires C++11

    * [pcl] fix Unix build

    * add versions

    * [vcpkg-cmake-get-vars] add CMAKE_<LANG>_COMPILER_VERSION

    * [boost-cobalt] detect compiler

    * [coin] force C++11

    * [json5-parser] force C++11

    * add versions

    * [boost-cobalt] exclude iOS and Android platforms due to C++ Concepts library is not supported

    * [gtsam] force C++11

    * [kenlm] force C++11

    * [quickfast] force C++11

    * [liblas] force C++11

    * update versions

    * [boost] re-generate port

    * update version

    * [kenlm] revert changes

    * [boost-cobalt] exclude OSX

    * update versions

    * [plc] remove useless patch after merge

    * update versions after merge

    ---------

    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/boost-accumulators/portfile.cmake            |   4 +-
 ports/boost-accumulators/vcpkg.json                |  44 +--
 ports/boost-algorithm/portfile.cmake               |   4 +-
 ports/boost-algorithm/vcpkg.json                   |  38 +--
 ports/boost-align/portfile.cmake                   |   4 +-
 ports/boost-align/vcpkg.json                       |  12 +-
 ports/boost-any/portfile.cmake                     |   4 +-
 ports/boost-any/vcpkg.json                         |  24 +-
 ports/boost-array/portfile.cmake                   |   4 +-
 ports/boost-array/vcpkg.json                       |  14 +-
 ports/boost-asio/portfile.cmake                    |   4 +-
 ports/boost-asio/vcpkg.json                        |  60 +---
 ports/boost-assert/portfile.cmake                  |   4 +-
 ports/boost-assert/vcpkg.json                      |   6 +-
 ports/boost-assign/portfile.cmake                  |   4 +-
 ports/boost-assign/vcpkg.json                      |  26 +-
 ports/boost-atomic/portfile.cmake                  |  16 +-
 ports/boost-atomic/vcpkg.json                      |  26 +-
 ports/boost-beast/portfile.cmake                   |   4 +-
 ports/boost-beast/vcpkg.json                       |  46 +--
 ports/boost-bimap/portfile.cmake                   |   4 +-
 ports/boost-bimap/vcpkg.json                       |  30 +-
 ports/boost-bind/portfile.cmake                    |   4 +-
 ports/boost-bind/vcpkg.json                        |   8 +-
 ports/boost-build/portfile.cmake                   |   6 +-
 ports/boost-build/vcpkg.json                       |   4 +-
 ports/boost-callable-traits/portfile.cmake         |   4 +-
 ports/boost-callable-traits/vcpkg.json             |   8 +-
 ports/boost-chrono/portfile.cmake                  |   4 +-
 ports/boost-chrono/vcpkg.json                      |  38 +--
 ports/boost-circular-buffer/portfile.cmake         |   4 +-
 ports/boost-circular-buffer/vcpkg.json             |  20 +-
 ports/boost-cobalt/b2-options.cmake                |  24 ++
 ports/boost-cobalt/portfile.cmake                  |  22 ++
 ports/boost-cobalt/vcpkg.json                      |  81 +++++
 ports/boost-compat/portfile.cmake                  |   4 +-
 ports/boost-compat/vcpkg.json                      |  10 +-
 ports/boost-compatibility/portfile.cmake           |   4 +-
 ports/boost-compatibility/vcpkg.json               |   8 +-
 ports/boost-compute/portfile.cmake                 |   4 +-
 ports/boost-compute/vcpkg.json                     |  58 ++--
 ports/boost-concept-check/portfile.cmake           |   4 +-
 ports/boost-concept-check/vcpkg.json               |  12 +-
 ports/boost-config/portfile.cmake                  |   4 +-
 ports/boost-config/vcpkg.json                      |   4 +-
 ports/boost-container-hash/portfile.cmake          |   4 +-
 ports/boost-container-hash/vcpkg.json              |  14 +-
 ports/boost-container/portfile.cmake               |   4 +-
 ports/boost-container/vcpkg.json                   |  18 +-
 ports/boost-context/b2-options.cmake.in            |   1 -
 ports/boost-context/portfile.cmake                 |   4 +-
 ports/boost-context/vcpkg.json                     |  22 +-
 ports/boost-contract/portfile.cmake                |   4 +-
 ports/boost-contract/vcpkg.json                    |  40 +--
 ports/boost-conversion/portfile.cmake              |   4 +-
 ports/boost-conversion/vcpkg.json                  |  24 +-
 ports/boost-convert/portfile.cmake                 |   4 +-
 ports/boost-convert/vcpkg.json                     |  26 +-
 ports/boost-core/portfile.cmake                    |   4 +-
 ports/boost-core/vcpkg.json                        |  12 +-
 ports/boost-coroutine/portfile.cmake               |   4 +-
 ports/boost-coroutine/vcpkg.json                   |  28 +-
 ports/boost-coroutine2/portfile.cmake              |   4 +-
 ports/boost-coroutine2/vcpkg.json                  |  10 +-
 ports/boost-crc/portfile.cmake                     |   4 +-
 ports/boost-crc/vcpkg.json                         |  12 +-
 ports/boost-date-time/portfile.cmake               |   4 +-
 ports/boost-date-time/vcpkg.json                   |  38 +--
 ports/boost-describe/portfile.cmake                |   4 +-
 ports/boost-describe/vcpkg.json                    |  10 +-
 ports/boost-detail/portfile.cmake                  |   4 +-
 ports/boost-detail/vcpkg.json                      |  14 +-
 ports/boost-dll/portfile.cmake                     |   4 +-
 ports/boost-dll/vcpkg.json                         |  36 +--
 ports/boost-dynamic-bitset/portfile.cmake          |   4 +-
 ports/boost-dynamic-bitset/vcpkg.json              |  20 +-
 ports/boost-endian/portfile.cmake                  |   4 +-
 ports/boost-endian/vcpkg.json                      |  18 +-
 ports/boost-exception/portfile.cmake               |   4 +-
 ports/boost-exception/vcpkg.json                   |  22 +-
 ports/boost-fiber/portfile.cmake                   |   4 +-
 ports/boost-fiber/vcpkg.json                       |  29 +-
 ports/boost-filesystem/portfile.cmake              |   4 +-
 ports/boost-filesystem/vcpkg.json                  |  36 +--
 ports/boost-flyweight/portfile.cmake               |   4 +-
 ports/boost-flyweight/vcpkg.json                   |  30 +-
 ports/boost-foreach/portfile.cmake                 |   4 +-
 ports/boost-foreach/vcpkg.json                     |  16 +-
 ports/boost-format/portfile.cmake                  |   4 +-
 ports/boost-format/vcpkg.json                      |  18 +-
 ports/boost-function-types/portfile.cmake          |   4 +-
 ports/boost-function-types/vcpkg.json              |  16 +-
 ports/boost-function/portfile.cmake                |   4 +-
 ports/boost-function/vcpkg.json                    |  22 +-
 ports/boost-functional/portfile.cmake              |   4 +-
 ports/boost-functional/vcpkg.json                  |  22 +-
 ports/boost-fusion/portfile.cmake                  |   4 +-
 ports/boost-fusion/vcpkg.json                      |  28 +-
 ports/boost-geometry/portfile.cmake                |   4 +-
 ports/boost-geometry/vcpkg.json                    |  64 ++--
 ports/boost-gil/portfile.cmake                     |   4 +-
 ports/boost-gil/vcpkg.json                         |  26 +-
 ports/boost-graph-parallel/portfile.cmake          |   4 +-
 ports/boost-graph-parallel/vcpkg.json              |  60 ++--
 ports/boost-graph/portfile.cmake                   |   4 +-
 ports/boost-graph/vcpkg.json                       |  90 +++---
 ports/boost-hana/portfile.cmake                    |   4 +-
 ports/boost-hana/vcpkg.json                        |  14 +-
 ports/boost-heap/portfile.cmake                    |   4 +-
 ports/boost-heap/vcpkg.json                        |  28 +-
 ports/boost-histogram/portfile.cmake               |   4 +-
 ports/boost-histogram/vcpkg.json                   |  18 +-
 ports/boost-hof/portfile.cmake                     |   4 +-
 ports/boost-hof/vcpkg.json                         |   8 +-
 ports/boost-icl/portfile.cmake                     |   4 +-
 ports/boost-icl/vcpkg.json                         |  34 +--
 ports/boost-integer/portfile.cmake                 |   4 +-
 ports/boost-integer/vcpkg.json                     |  16 +-
 ports/boost-interprocess/portfile.cmake            |   4 +-
 ports/boost-interprocess/vcpkg.json                |  24 +-
 ports/boost-interval/portfile.cmake                |   4 +-
 ports/boost-interval/vcpkg.json                    |  10 +-
 ports/boost-intrusive/portfile.cmake               |   4 +-
 ports/boost-intrusive/vcpkg.json                   |  14 +-
 ports/boost-io/portfile.cmake                      |   4 +-
 ports/boost-io/vcpkg.json                          |   6 +-
 ports/boost-iostreams/portfile.cmake               |   4 +-
 ports/boost-iostreams/vcpkg.json                   |  45 ++-
 ports/boost-iterator/portfile.cmake                |   4 +-
 ports/boost-iterator/vcpkg.json                    |  34 +--
 ...se-of-intrinsics-on-windows-ARM-platforms.patch |  44 ---
 ...lace-_M_ARM64-with-_M_ARM-for-32-bit-path.patch |  25 --
 ports/boost-json/b2-options.cmake                  |   3 -
 ports/boost-json/portfile.cmake                    |  12 +-
 ports/boost-json/vcpkg.json                        |  28 +-
 ports/boost-lambda/portfile.cmake                  |   4 +-
 ports/boost-lambda/vcpkg.json                      |  24 +-
 ports/boost-lambda2/portfile.cmake                 |   4 +-
 ports/boost-lambda2/vcpkg.json                     |   8 +-
 ports/boost-leaf/portfile.cmake                    |   4 +-
 ports/boost-leaf/vcpkg.json                        |   8 +-
 ports/boost-lexical-cast/portfile.cmake            |   4 +-
 ports/boost-lexical-cast/vcpkg.json                |  34 +--
 ports/boost-local-function/portfile.cmake          |   4 +-
 ports/boost-local-function/vcpkg.json              |  18 +-
 .../0001-fix-build-error-on-MSVC.patch             |  25 --
 ports/boost-locale/fix-dependencies.patch          |  39 +--
 ports/boost-locale/portfile.cmake                  |  12 +-
 ports/boost-locale/vcpkg.json                      |  22 +-
 ports/boost-lockfree/portfile.cmake                |   4 +-
 ports/boost-lockfree/vcpkg.json                    |  34 +--
 ports/boost-log/portfile.cmake                     |   6 +-
 ports/boost-log/vcpkg.json                         | 102 +++----
 ports/boost-logic/portfile.cmake                   |   4 +-
 ports/boost-logic/vcpkg.json                       |   8 +-
 ports/boost-math/001-remove-checks.patch           |  23 --
 ports/boost-math/b2-options.cmake                  |   3 -
 ports/boost-math/portfile.cmake                    |  15 +-
 ports/boost-math/vcpkg.json                        |  28 +-
 ports/boost-metaparse/portfile.cmake               |   4 +-
 ports/boost-metaparse/vcpkg.json                   |  16 +-
 .../boost-modular-build.cmake                      |   4 +-
 ports/boost-modular-build-helper/vcpkg.json        |   5 +-
 ports/boost-move/portfile.cmake                    |   4 +-
 ports/boost-move/vcpkg.json                        |   6 +-
 ports/boost-mp11/portfile.cmake                    |   4 +-
 ports/boost-mp11/vcpkg.json                        |   8 +-
 ports/boost-mpi/fix-build-with-msvc.patch          |  30 --
 ports/boost-mpi/portfile.cmake                     |   5 +-
 ports/boost-mpi/vcpkg.json                         |  44 +--
 ports/boost-mpl/portfile.cmake                     |   4 +-
 ports/boost-mpl/vcpkg.json                         |  18 +-
 ports/boost-msm/portfile.cmake                     |   4 +-
 ports/boost-msm/vcpkg.json                         |  38 +--
 ports/boost-multi-array/portfile.cmake             |   4 +-
 ports/boost-multi-array/vcpkg.json                 |  24 +-
 ports/boost-multi-index/portfile.cmake             |   4 +-
 ports/boost-multi-index/vcpkg.json                 |  36 +--
 ports/boost-multiprecision/portfile.cmake          |   4 +-
 ports/boost-multiprecision/vcpkg.json              |  22 +-
 ports/boost-mysql/portfile.cmake                   |   4 +-
 ports/boost-mysql/vcpkg.json                       |  26 +-
 ports/boost-nowide/b2-options.cmake                |   3 -
 ports/boost-nowide/portfile.cmake                  |   9 +-
 ports/boost-nowide/vcpkg.json                      |  12 +-
 ports/boost-numeric-conversion/portfile.cmake      |   4 +-
 ports/boost-numeric-conversion/vcpkg.json          |  18 +-
 ports/boost-odeint/portfile.cmake                  |   4 +-
 ports/boost-odeint/vcpkg.json                      |  46 +--
 ports/boost-optional/portfile.cmake                |   4 +-
 ports/boost-optional/vcpkg.json                    |  24 +-
 ports/boost-outcome/portfile.cmake                 |   4 +-
 ports/boost-outcome/vcpkg.json                     |  12 +-
 ports/boost-parameter-python/portfile.cmake        |   4 +-
 ports/boost-parameter-python/vcpkg.json            |  16 +-
 ports/boost-parameter/portfile.cmake               |   4 +-
 ports/boost-parameter/vcpkg.json                   |  24 +-
 ports/boost-pfr/portfile.cmake                     |   4 +-
 ports/boost-pfr/vcpkg.json                         |   8 +-
 ports/boost-phoenix/fix-duplicate-symbols.patch    |  13 -
 ports/boost-phoenix/portfile.cmake                 |   5 +-
 ports/boost-phoenix/vcpkg.json                     |  32 +-
 ports/boost-poly-collection/portfile.cmake         |   4 +-
 ports/boost-poly-collection/vcpkg.json             |  20 +-
 ports/boost-polygon/portfile.cmake                 |   4 +-
 ports/boost-polygon/vcpkg.json                     |   6 +-
 ports/boost-pool/portfile.cmake                    |   4 +-
 ports/boost-pool/vcpkg.json                        |  16 +-
 ports/boost-predef/portfile.cmake                  |   4 +-
 ports/boost-predef/vcpkg.json                      |   8 +-
 ports/boost-preprocessor/portfile.cmake            |   4 +-
 ports/boost-preprocessor/vcpkg.json                |   8 +-
 ports/boost-process/portfile.cmake                 |   4 +-
 ports/boost-process/vcpkg.json                     |  42 +--
 ports/boost-program-options/portfile.cmake         |   4 +-
 ports/boost-program-options/vcpkg.json             |  34 +--
 ports/boost-property-map-parallel/portfile.cmake   |   4 +-
 ports/boost-property-map-parallel/vcpkg.json       |  30 +-
 ports/boost-property-map/portfile.cmake            |   4 +-
 ports/boost-property-map/vcpkg.json                |  34 +--
 ports/boost-property-tree/portfile.cmake           |   4 +-
 ports/boost-property-tree/vcpkg.json               |  36 +--
 ports/boost-proto/portfile.cmake                   |   4 +-
 ports/boost-proto/vcpkg.json                       |  24 +-
 ports/boost-ptr-container/portfile.cmake           |   4 +-
 ports/boost-ptr-container/vcpkg.json               |  30 +-
 ports/boost-python/portfile.cmake                  |   4 +-
 ports/boost-python/vcpkg.json                      |  50 +--
 ports/boost-qvm/portfile.cmake                     |   4 +-
 ports/boost-qvm/vcpkg.json                         |   8 +-
 ports/boost-random/portfile.cmake                  |   4 +-
 ports/boost-random/vcpkg.json                      |  34 +--
 ports/boost-range/portfile.cmake                   |   4 +-
 ports/boost-range/vcpkg.json                       |  38 +--
 ports/boost-ratio/portfile.cmake                   |   4 +-
 ports/boost-ratio/vcpkg.json                       |  30 +-
 ports/boost-rational/portfile.cmake                |   4 +-
 ports/boost-rational/vcpkg.json                    |  20 +-
 ports/boost-redis/portfile.cmake                   |  12 +
 ports/boost-redis/vcpkg.json                       |  42 +++
 ports/boost-regex/b2-options.cmake                 |   3 -
 ports/boost-regex/portfile.cmake                   |   4 +-
 ports/boost-regex/vcpkg.json                       |  32 +-
 ports/boost-safe-numerics/portfile.cmake           |   4 +-
 ports/boost-safe-numerics/vcpkg.json               |  16 +-
 ports/boost-scope-exit/portfile.cmake              |   4 +-
 ports/boost-scope-exit/vcpkg.json                  |  14 +-
 ports/boost-serialization/portfile.cmake           |   9 +-
 ports/boost-serialization/vcpkg.json               |  62 ++--
 ports/boost-signals2/portfile.cmake                |   4 +-
 ports/boost-signals2/vcpkg.json                    |  34 +--
 ports/boost-smart-ptr/portfile.cmake               |   4 +-
 ports/boost-smart-ptr/vcpkg.json                   |  18 +-
 ports/boost-sort/portfile.cmake                    |   4 +-
 ports/boost-sort/vcpkg.json                        |  14 +-
 ports/boost-spirit/portfile.cmake                  |   4 +-
 ports/boost-spirit/vcpkg.json                      |  62 ++--
 ports/boost-stacktrace/portfile.cmake              |   9 +-
 ports/boost-stacktrace/vcpkg.json                  |  30 +-
 ports/boost-statechart/portfile.cmake              |   4 +-
 ports/boost-statechart/vcpkg.json                  |  28 +-
 ports/boost-static-assert/portfile.cmake           |   4 +-
 ports/boost-static-assert/vcpkg.json               |   6 +-
 ports/boost-static-string/portfile.cmake           |   4 +-
 ports/boost-static-string/vcpkg.json               |  18 +-
 ports/boost-stl-interfaces/portfile.cmake          |   4 +-
 ports/boost-stl-interfaces/vcpkg.json              |  10 +-
 ports/boost-system/portfile.cmake                  |   4 +-
 ports/boost-system/vcpkg.json                      |  18 +-
 ports/boost-test/portfile.cmake                    |   4 +-
 ports/boost-test/vcpkg.json                        |  44 +--
 ports/boost-thread/portfile.cmake                  |   4 +-
 ports/boost-thread/vcpkg.json                      |  74 ++---
 ports/boost-throw-exception/portfile.cmake         |   4 +-
 ports/boost-throw-exception/vcpkg.json             |   8 +-
 ports/boost-timer/portfile.cmake                   |   4 +-
 ports/boost-timer/vcpkg.json                       |  14 +-
 ports/boost-tokenizer/portfile.cmake               |   4 +-
 ports/boost-tokenizer/vcpkg.json                   |  16 +-
 ports/boost-tti/portfile.cmake                     |   4 +-
 ports/boost-tti/vcpkg.json                         |  14 +-
 ports/boost-tuple/portfile.cmake                   |   4 +-
 ports/boost-tuple/vcpkg.json                       |  12 +-
 ports/boost-type-erasure/portfile.cmake            |   4 +-
 ports/boost-type-erasure/vcpkg.json                |  36 +--
 ports/boost-type-index/portfile.cmake              |   4 +-
 ports/boost-type-index/vcpkg.json                  |  24 +-
 ports/boost-type-traits/portfile.cmake             |   4 +-
 ports/boost-type-traits/vcpkg.json                 |   8 +-
 ports/boost-typeof/portfile.cmake                  |   4 +-
 ports/boost-typeof/vcpkg.json                      |  14 +-
 ports/boost-ublas/portfile.cmake                   |   4 +-
 ports/boost-ublas/vcpkg.json                       |  28 +-
 ports/boost-uninstall/vcpkg.json                   |   2 +-
 ports/boost-units/portfile.cmake                   |   4 +-
 ports/boost-units/vcpkg.json                       |  28 +-
 .../0001-unordered-fix-copy-assign.patch           |  16 -
 ports/boost-unordered/portfile.cmake               |   5 +-
 ports/boost-unordered/vcpkg.json                   |  38 +--
 ports/boost-url/portfile.cmake                     |   8 +-
 ports/boost-url/vcpkg.json                         |  30 +-
 ports/boost-utility/portfile.cmake                 |   4 +-
 ports/boost-utility/vcpkg.json                     |  18 +-
 ports/boost-uuid/portfile.cmake                    |   4 +-
 ports/boost-uuid/vcpkg.json                        |  32 +-
 ports/boost-variant/portfile.cmake                 |   4 +-
 ports/boost-variant/vcpkg.json                     |  38 +--
 ports/boost-variant2/portfile.cmake                |   4 +-
 ports/boost-variant2/vcpkg.json                    |  10 +-
 ports/boost-vcpkg-helpers/portfile.cmake           |   1 -
 ports/boost-vcpkg-helpers/vcpkg.json               |   4 +-
 ports/boost-vmd/portfile.cmake                     |   4 +-
 ports/boost-vmd/vcpkg.json                         |  10 +-
 ports/boost-wave/portfile.cmake                    |   4 +-
 ports/boost-wave/vcpkg.json                        |  46 +--
 ports/boost-winapi/portfile.cmake                  |   4 +-
 ports/boost-winapi/vcpkg.json                      |   8 +-
 ports/boost-xpressive/portfile.cmake               |   4 +-
 ports/boost-xpressive/vcpkg.json                   |  48 +--
 ports/boost-yap/portfile.cmake                     |   4 +-
 ports/boost-yap/vcpkg.json                         |  14 +-
 ports/boost/vcpkg.json                             | 308 ++++++++++---------
 ports/coin/portfile.cmake                          |   1 +
 ports/coin/vcpkg.json                              |   2 +-
 ports/gtsam/portfile.cmake                         |   1 +
 ports/gtsam/vcpkg.json                             |   1 +
 ports/json5-parser/portfile.cmake                  |   2 +
 ports/json5-parser/vcpkg.json                      |   2 +-
 ports/liblas/force-cpp11.patch                     |  27 ++
 ports/liblas/portfile.cmake                        |   1 +
 ports/liblas/vcpkg.json                            |   2 +-
 ports/quickfast/CMakeLists.txt                     |   2 +
 ports/quickfast/vcpkg.json                         |   2 +-
 .../cmake_get_vars/CMakeLists.txt                  |   2 +
 ports/vcpkg-cmake-get-vars/vcpkg.json              |   2 +-
 scripts/boost/generate-ports.ps1                   |  89 +++---
 scripts/boost/post-build-stubs/atomic.cmake        |   2 +
 scripts/boost/post-source-stubs/atomic.cmake       |  12 +-
 scripts/boost/post-source-stubs/cobalt.cmake       |   5 +
 scripts/boost/post-source-stubs/locale.cmake       |   4 +-
 scripts/boost/post-source-stubs/log.cmake          |   2 +-
 scripts/boost/post-source-stubs/math.cmake         |   5 +
 .../boost/post-source-stubs/serialization.cmake    |   5 +
 scripts/boost/post-source-stubs/stacktrace.cmake   |   5 +
 scripts/boost/post-source-stubs/url.cmake          |   4 +-
 versions/b-/boost-accumulators.json                |   5 +
 versions/b-/boost-algorithm.json                   |   5 +
 versions/b-/boost-align.json                       |   5 +
 versions/b-/boost-any.json                         |   5 +
 versions/b-/boost-array.json                       |   5 +
 versions/b-/boost-asio.json                        |   5 +
 versions/b-/boost-assert.json                      |   5 +
 versions/b-/boost-assign.json                      |   5 +
 versions/b-/boost-atomic.json                      |   5 +
 versions/b-/boost-beast.json                       |   5 +
 versions/b-/boost-bimap.json                       |   5 +
 versions/b-/boost-bind.json                        |   5 +
 versions/b-/boost-build.json                       |   5 +
 versions/b-/boost-callable-traits.json             |   5 +
 versions/b-/boost-chrono.json                      |   5 +
 versions/b-/boost-circular-buffer.json             |   5 +
 versions/b-/boost-cobalt.json                      |   9 +
 versions/b-/boost-compat.json                      |   5 +
 versions/b-/boost-compatibility.json               |   5 +
 versions/b-/boost-compute.json                     |   5 +
 versions/b-/boost-concept-check.json               |   5 +
 versions/b-/boost-config.json                      |   5 +
 versions/b-/boost-container-hash.json              |   5 +
 versions/b-/boost-container.json                   |   5 +
 versions/b-/boost-context.json                     |   5 +
 versions/b-/boost-contract.json                    |   5 +
 versions/b-/boost-conversion.json                  |   5 +
 versions/b-/boost-convert.json                     |   5 +
 versions/b-/boost-core.json                        |   5 +
 versions/b-/boost-coroutine.json                   |   5 +
 versions/b-/boost-coroutine2.json                  |   5 +
 versions/b-/boost-crc.json                         |   5 +
 versions/b-/boost-date-time.json                   |   5 +
 versions/b-/boost-describe.json                    |   5 +
 versions/b-/boost-detail.json                      |   5 +
 versions/b-/boost-dll.json                         |   5 +
 versions/b-/boost-dynamic-bitset.json              |   5 +
 versions/b-/boost-endian.json                      |   5 +
 versions/b-/boost-exception.json                   |   5 +
 versions/b-/boost-fiber.json                       |   5 +
 versions/b-/boost-filesystem.json                  |   5 +
 versions/b-/boost-flyweight.json                   |   5 +
 versions/b-/boost-foreach.json                     |   5 +
 versions/b-/boost-format.json                      |   5 +
 versions/b-/boost-function-types.json              |   5 +
 versions/b-/boost-function.json                    |   5 +
 versions/b-/boost-functional.json                  |   5 +
 versions/b-/boost-fusion.json                      |   5 +
 versions/b-/boost-geometry.json                    |   5 +
 versions/b-/boost-gil.json                         |   5 +
 versions/b-/boost-graph-parallel.json              |   5 +
 versions/b-/boost-graph.json                       |   5 +
 versions/b-/boost-hana.json                        |   5 +
 versions/b-/boost-heap.json                        |   5 +
 versions/b-/boost-histogram.json                   |   5 +
 versions/b-/boost-hof.json                         |   5 +
 versions/b-/boost-icl.json                         |   5 +
 versions/b-/boost-integer.json                     |   5 +
 versions/b-/boost-interprocess.json                |   5 +
 versions/b-/boost-interval.json                    |   5 +
 versions/b-/boost-intrusive.json                   |   5 +
 versions/b-/boost-io.json                          |   5 +
 versions/b-/boost-iostreams.json                   |   5 +
 versions/b-/boost-iterator.json                    |   5 +
 versions/b-/boost-json.json                        |   5 +
 versions/b-/boost-lambda.json                      |   5 +
 versions/b-/boost-lambda2.json                     |   5 +
 versions/b-/boost-leaf.json                        |   5 +
 versions/b-/boost-lexical-cast.json                |   5 +
 versions/b-/boost-local-function.json              |   5 +
 versions/b-/boost-locale.json                      |   5 +
 versions/b-/boost-lockfree.json                    |   5 +
 versions/b-/boost-log.json                         |   5 +
 versions/b-/boost-logic.json                       |   5 +
 versions/b-/boost-math.json                        |   5 +
 versions/b-/boost-metaparse.json                   |   5 +
 versions/b-/boost-modular-build-helper.json        |   5 +
 versions/b-/boost-move.json                        |   5 +
 versions/b-/boost-mp11.json                        |   5 +
 versions/b-/boost-mpi.json                         |   5 +
 versions/b-/boost-mpl.json                         |   5 +
 versions/b-/boost-msm.json                         |   5 +
 versions/b-/boost-multi-array.json                 |   5 +
 versions/b-/boost-multi-index.json                 |   5 +
 versions/b-/boost-multiprecision.json              |   5 +
 versions/b-/boost-mysql.json                       |   5 +
 versions/b-/boost-nowide.json                      |   5 +
 versions/b-/boost-numeric-conversion.json          |   5 +
 versions/b-/boost-odeint.json                      |   5 +
 versions/b-/boost-optional.json                    |   5 +
 versions/b-/boost-outcome.json                     |   5 +
 versions/b-/boost-parameter-python.json            |   5 +
 versions/b-/boost-parameter.json                   |   5 +
 versions/b-/boost-pfr.json                         |   5 +
 versions/b-/boost-phoenix.json                     |   5 +
 versions/b-/boost-poly-collection.json             |   5 +
 versions/b-/boost-polygon.json                     |   5 +
 versions/b-/boost-pool.json                        |   5 +
 versions/b-/boost-predef.json                      |   5 +
 versions/b-/boost-preprocessor.json                |   5 +
 versions/b-/boost-process.json                     |   5 +
 versions/b-/boost-program-options.json             |   5 +
 versions/b-/boost-property-map-parallel.json       |   5 +
 versions/b-/boost-property-map.json                |   5 +
 versions/b-/boost-property-tree.json               |   5 +
 versions/b-/boost-proto.json                       |   5 +
 versions/b-/boost-ptr-container.json               |   5 +
 versions/b-/boost-python.json                      |   5 +
 versions/b-/boost-qvm.json                         |   5 +
 versions/b-/boost-random.json                      |   5 +
 versions/b-/boost-range.json                       |   5 +
 versions/b-/boost-ratio.json                       |   5 +
 versions/b-/boost-rational.json                    |   5 +
 versions/b-/boost-redis.json                       |   9 +
 versions/b-/boost-regex.json                       |   5 +
 versions/b-/boost-safe-numerics.json               |   5 +
 versions/b-/boost-scope-exit.json                  |   5 +
 versions/b-/boost-serialization.json               |   5 +
 versions/b-/boost-signals2.json                    |   5 +
 versions/b-/boost-smart-ptr.json                   |   5 +
 versions/b-/boost-sort.json                        |   5 +
 versions/b-/boost-spirit.json                      |   5 +
 versions/b-/boost-stacktrace.json                  |   5 +
 versions/b-/boost-statechart.json                  |   5 +
 versions/b-/boost-static-assert.json               |   5 +
 versions/b-/boost-static-string.json               |   5 +
 versions/b-/boost-stl-interfaces.json              |   5 +
 versions/b-/boost-system.json                      |   5 +
 versions/b-/boost-test.json                        |   5 +
 versions/b-/boost-thread.json                      |   5 +
 versions/b-/boost-throw-exception.json             |   5 +
 versions/b-/boost-timer.json                       |   5 +
 versions/b-/boost-tokenizer.json                   |   5 +
 versions/b-/boost-tti.json                         |   5 +
 versions/b-/boost-tuple.json                       |   5 +
 versions/b-/boost-type-erasure.json                |   5 +
 versions/b-/boost-type-index.json                  |   5 +
 versions/b-/boost-type-traits.json                 |   5 +
 versions/b-/boost-typeof.json                      |   5 +
 versions/b-/boost-ublas.json                       |   5 +
 versions/b-/boost-uninstall.json                   |   5 +
 versions/b-/boost-units.json                       |   5 +
 versions/b-/boost-unordered.json                   |   5 +
 versions/b-/boost-url.json                         |   5 +
 versions/b-/boost-utility.json                     |   5 +
 versions/b-/boost-uuid.json                        |   5 +
 versions/b-/boost-variant.json                     |   5 +
 versions/b-/boost-variant2.json                    |   5 +
 versions/b-/boost-vcpkg-helpers.json               |   5 +
 versions/b-/boost-vmd.json                         |   5 +
 versions/b-/boost-wave.json                        |   5 +
 versions/b-/boost-winapi.json                      |   5 +
 versions/b-/boost-xpressive.json                   |   5 +
 versions/b-/boost-yap.json                         |   5 +
 versions/b-/boost.json                             |   5 +
 versions/baseline.json                             | 334 +++++++++++----------
 versions/c-/coin.json                              |   5 +
 versions/g-/gtsam.json                             |   5 +
 versions/j-/json5-parser.json                      |   5 +
 versions/l-/liblas.json                            |   5 +
 versions/q-/quickfast.json                         |   5 +
 versions/v-/vcpkg-cmake-get-vars.json              |   5 +
 507 files changed, 3588 insertions(+), 2887 deletions(-)

2024-09-22 13:18:45,399 - 147 - INFO - run: git add .
2024-09-22 13:18:45,420 - 147 - INFO - run: git commit -m [boost] Update to v1.84.0 (#35693) --author Yury Bura <yurybura@gmail.com>
[main 3d8feb16d] [boost] Update to v1.84.0 (#35693)
 Author: Yury Bura <yurybura@gmail.com>
 3 files changed, 253 insertions(+)
 create mode 100644 ports/boost-accumulators/portfile.cmake
 create mode 100644 ports/boost-accumulators/vcpkg.json
 create mode 100644 versions/b-/boost-accumulators.json
2024-09-22 13:18:45,481 - 360 - WARNING - copy downloads/vcpkg/ports/zlib -> ./ports/zlib
2024-09-22 13:18:45,484 - 369 - WARNING - copy downloads/vcpkg/versions/z-/zlib.json -> ./versions/z-/zlib.json
2024-09-22 13:18:45,484 - 382 - INFO - zlib
commit 7233110263ec34c316fd12d0a91c11d1ca9f860b
Author: Carsten Grimm <97085459+carsten-grimm-at-ipolog@users.noreply.github.com>
Date:   2024-01-30 21:58:10 +0100

    [zlib] update to 1.3.1 (#36395)

    * [zlib] update to version 1.3.1

    * [zlib] adapt patches

    * [zlib] regenerate version info

    * [zlib] remove version workaround

    * [zlib] regenerate version info

    * CI

 ...patch => 0002-build-static-or-shared-not-both.patch} | 17 +++++++++--------
 ports/zlib/0002-skip-building-examples.patch            | 17 -----------------
 ...w-fixes.patch => 0003-android-and-mingw-fixes.patch} |  9 ++++-----
 ports/zlib/portfile.cmake                               | 10 ++++------
 ports/zlib/vcpkg.json                                   |  2 +-
 versions/baseline.json                                  |  2 +-
 versions/z-/zlib.json                                   |  5 +++++
 7 files changed, 24 insertions(+), 38 deletions(-)

2024-09-22 13:18:45,484 - 147 - INFO - run: git add .
2024-09-22 13:18:45,504 - 147 - INFO - run: git commit -m [zlib] update to 1.3.1 (#36395) --author Carsten Grimm <97085459+carsten-grimm-at-ipolog@users.noreply.github.com>
[main 0b1254597] [zlib] update to 1.3.1 (#36395)
 Author: Carsten Grimm <97085459+carsten-grimm-at-ipolog@users.noreply.github.com>
 8 files changed, 328 insertions(+)
 create mode 100644 ports/zlib/0001-Prevent-invalid-inclusions-when-HAVE_-is-set-to-0.patch
 create mode 100644 ports/zlib/0002-build-static-or-shared-not-both.patch
 create mode 100644 ports/zlib/0003-android-and-mingw-fixes.patch
 create mode 100644 ports/zlib/portfile.cmake
 create mode 100644 ports/zlib/usage
 create mode 100644 ports/zlib/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/zlib/vcpkg.json
 create mode 100644 versions/z-/zlib.json
2024-09-22 13:18:45,569 - 360 - WARNING - copy downloads/vcpkg/ports/libffi -> ./ports/libffi
2024-09-22 13:18:45,570 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libffi.json -> ./versions/l-/libffi.json
2024-09-22 13:18:45,571 - 382 - INFO - libffi
commit 77fbdaf616ad0df6f3bdf0f619f77b922d95580e
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-02-27 09:37:57 +0100

    [libffi] Update to 3.4.6, enable wasm32 (#36876)

 ports/libffi/fix_undefind_func.patch | 28 ----------------------------
 ports/libffi/portfile.cmake          | 18 +++++++++++-------
 ports/libffi/vcpkg.json              |  3 +--
 versions/baseline.json               |  4 ++--
 versions/l-/libffi.json              |  5 +++++
 5 files changed, 19 insertions(+), 39 deletions(-)

2024-09-22 13:18:45,572 - 147 - INFO - run: git add .
2024-09-22 13:18:45,592 - 147 - INFO - run: git commit -m [libffi] Update to 3.4.6, enable wasm32 (#36876) --author Kai Pastor <dg0yt@darc.de>
[main 87a794ac4] [libffi] Update to 3.4.6, enable wasm32 (#36876)
 Author: Kai Pastor <dg0yt@darc.de>
 7 files changed, 298 insertions(+)
 create mode 100644 ports/libffi/dll-bindir.diff
 create mode 100644 ports/libffi/libffiConfig.cmake
 create mode 100644 ports/libffi/portfile.cmake
 create mode 100644 ports/libffi/unofficial-libffi-config.cmake
 create mode 100644 ports/libffi/usage
 create mode 100644 ports/libffi/vcpkg.json
 create mode 100644 versions/l-/libffi.json
2024-09-22 13:18:45,654 - 360 - WARNING - copy downloads/vcpkg/ports/zstd -> ./ports/zstd
2024-09-22 13:18:45,657 - 369 - WARNING - copy downloads/vcpkg/versions/z-/zstd.json -> ./versions/z-/zstd.json
2024-09-22 13:18:45,658 - 382 - INFO - zstd
commit 2f3fccd1e781933e5bbf02c07f4aa3dc36d02e2e
Author: Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
Date:   2024-04-15 20:39:47 +0300

    [zstd] Update to version 1.5.6. (#38080)

    - [X] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [X] SHA512s are updated for each updated download.
    - [ ] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [ ] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [ ] Any patches that are no longer applied are deleted from the port's
    directory.
    - [X] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [X] Only one version is added to each modified port's versions file.

    ---------

    Co-authored-by: Jim wang (BEYONDSOFT CONSULTING INC) <v-wangjim@microsoft.com>

 ports/zstd/fix-windows-rc-compile.patch | 13 +++++++++++++
 ports/zstd/portfile.cmake               |  3 ++-
 ports/zstd/usage                        |  6 +++---
 ports/zstd/vcpkg.json                   |  3 +--
 versions/baseline.json                  |  4 ++--
 versions/z-/zstd.json                   |  5 +++++
 6 files changed, 26 insertions(+), 8 deletions(-)

2024-09-22 13:18:45,658 - 147 - INFO - run: git add .
2024-09-22 13:18:45,679 - 147 - INFO - run: git commit -m [zstd] Update to version 1.5.6. (#38080) --author Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
[main 11a601899] [zstd] Update to version 1.5.6. (#38080)
 Author: Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
 7 files changed, 306 insertions(+)
 create mode 100644 ports/zstd/fix-emscripten-and-clang-cl.patch
 create mode 100644 ports/zstd/fix-windows-rc-compile.patch
 create mode 100644 ports/zstd/no-static-suffix.patch
 create mode 100644 ports/zstd/portfile.cmake
 create mode 100644 ports/zstd/usage
 create mode 100644 ports/zstd/vcpkg.json
 create mode 100644 versions/z-/zstd.json
2024-09-22 13:18:45,740 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-pkgconfig-get-modules -> ./ports/vcpkg-pkgconfig-get-modules
2024-09-22 13:18:45,741 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-pkgconfig-get-modules.json -> ./versions/v-/vcpkg-pkgconfig-get-modules.json
2024-09-22 13:18:45,742 - 382 - INFO - vcpkg-pkgconfig-get-modules
commit 04b0cf2b3fd1752d3c3db969cbc10ba0a4613cee
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-05-02 04:51:16 +0200

    [vcpkg-pkgconfig-get-modules] Turn into proper helper port (#37939)

    I wonder if LIBRARIES_DIRS should return a list of directories instead
    of a list of `-L...` flags.

    ---------

    Co-authored-by: Javier Matos <javiermatos@Javiers-Laptop.lan>
    Co-authored-by: Monica <liuyumei01@beyondsoft.com>

 ports/vcpkg-pkgconfig-get-modules/portfile.cmake           | 14 ++++----------
 ports/vcpkg-pkgconfig-get-modules/vcpkg.json               | 11 ++++-------
 .../x_vcpkg_pkgconfig_get_modules.cmake                    |  8 ++++++--
 versions/baseline.json                                     |  2 +-
 versions/v-/vcpkg-pkgconfig-get-modules.json               |  5 +++++
 5 files changed, 20 insertions(+), 20 deletions(-)

2024-09-22 13:18:45,742 - 147 - INFO - run: git add .
2024-09-22 13:18:45,763 - 147 - INFO - run: git commit -m [vcpkg-pkgconfig-get-modules] Turn into proper helper port (#37939) --author Kai Pastor <dg0yt@darc.de>
[main 491473731] [vcpkg-pkgconfig-get-modules] Turn into proper helper port (#37939)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 200 insertions(+)
 create mode 100644 ports/vcpkg-pkgconfig-get-modules/portfile.cmake
 create mode 100644 ports/vcpkg-pkgconfig-get-modules/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-pkgconfig-get-modules/vcpkg.json
 create mode 100644 ports/vcpkg-pkgconfig-get-modules/x_vcpkg_pkgconfig_get_modules.cmake
 create mode 100644 versions/v-/vcpkg-pkgconfig-get-modules.json
2024-09-22 13:18:45,827 - 360 - WARNING - copy downloads/vcpkg/ports/boost-interprocess -> ./ports/boost-interprocess
2024-09-22 13:18:45,829 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-interprocess.json -> ./versions/b-/boost-interprocess.json
2024-09-22 13:18:45,830 - 382 - INFO - boost-interprocess
commit ed472cd1bec629f326509be966939e012750816a
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-05-23 02:59:12 +0200

    [boost-interprocess] Fix link libs (#38815)

    Alternative to #38809: Some link libs are only used by tests, not by the
    lib.

    Portfile generated with #38814, therefore omitting change to
    `generate-ports.ps1`.

 ports/boost-interprocess/portfile.cmake        |  2 ++
 ports/boost-interprocess/unused-link-libs.diff | 17 +++++++++++++++++
 ports/boost-interprocess/vcpkg.json            |  3 ++-
 versions/b-/boost-interprocess.json            |  5 +++++
 versions/baseline.json                         |  2 +-
 5 files changed, 27 insertions(+), 2 deletions(-)

2024-09-22 13:18:45,830 - 147 - INFO - run: git add .
2024-09-22 13:18:45,851 - 147 - INFO - run: git commit -m [boost-interprocess] Fix link libs (#38815) --author Kai Pastor <dg0yt@darc.de>
[main 1b8d49eb5] [boost-interprocess] Fix link libs (#38815)
 Author: Kai Pastor <dg0yt@darc.de>
 4 files changed, 228 insertions(+)
 create mode 100644 ports/boost-interprocess/portfile.cmake
 create mode 100644 ports/boost-interprocess/unused-link-libs.diff
 create mode 100644 ports/boost-interprocess/vcpkg.json
 create mode 100644 versions/b-/boost-interprocess.json
2024-09-22 13:18:45,914 - 360 - WARNING - copy downloads/vcpkg/ports/boost-container -> ./ports/boost-container
2024-09-22 13:18:45,917 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-container.json -> ./versions/b-/boost-container.json
2024-09-22 13:18:45,917 - 382 - INFO - boost-container
commit b361950b5aaec61f9d1f48dcc2e36b7630e7437e
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-05-23 03:15:41 +0200

    [boost-container] Fix deps and emscripten (#38806)

    Fixes #38679. ([No longer uses
    Boost::static_assert.](https://www.boost.org/doc/libs/1_85_0/doc/html/container/release_notes.html#container.release_notes.release_notes_boost_1_85_00))
    Fixes #38469. (Needs threads, so [emscripten needs to use
    `-pthread`](https://emscripten.org/docs/porting/pthreads.html#compiling-with-pthreads-enabled).)
    Change homepage link to something more useful. The update to the
    generator script and the other ports will be in a separate PR.

 ports/boost-container/no-static-assert.diff | 12 ++++++++++++
 ports/boost-container/portfile.cmake        |  3 +++
 ports/boost-container/posix-threads.diff    | 21 +++++++++++++++++++++
 ports/boost-container/vcpkg.json            |  3 ++-
 scripts/boost/generate-ports.ps1            |  1 +
 versions/b-/boost-container.json            |  5 +++++
 versions/baseline.json                      |  2 +-
 7 files changed, 45 insertions(+), 2 deletions(-)

2024-09-22 13:18:45,917 - 147 - INFO - run: git add .
2024-09-22 13:18:45,938 - 147 - INFO - run: git commit -m [boost-container] Fix deps and emscripten (#38806) --author Kai Pastor <dg0yt@darc.de>
[main cdc6ee101] [boost-container] Fix deps and emscripten (#38806)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 230 insertions(+)
 create mode 100644 ports/boost-container/no-static-assert.diff
 create mode 100644 ports/boost-container/portfile.cmake
 create mode 100644 ports/boost-container/posix-threads.diff
 create mode 100644 ports/boost-container/vcpkg.json
 create mode 100644 versions/b-/boost-container.json
2024-09-22 13:18:46,016 - 360 - WARNING - copy downloads/vcpkg/ports/boost-algorithm -> ./ports/boost-algorithm
2024-09-22 13:18:46,017 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-algorithm.json -> ./versions/b-/boost-algorithm.json
2024-09-22 13:18:46,017 - 382 - INFO - boost-algorithm
commit 007aaced1a9d3245e28a2ba9395dca88ea890db1
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-05-28 00:41:34 +0200

    [vcpkg-scripts][boost] Improve generate-ports.ps1 (#38814)

    - Change homepage URLs to point to documentation instead of GH.
    - Allow encoding alternative propagation of `supports`/`platform` so
    that changes don't need to be selected manually.
    - Allow to suppress the generated dependency `platform` expression when
    a dependency is non-optional.
    (`boost-parameter` requires `boost-python`, and the dependency
    transitively determines the supported platforms of the dependent port.)
    - For port `boost`, generate `platform` expression from transitive
    `supports` limitations.
    (`boost-parameter` platform expression must account for `boost-python`.)
    This fixes port `boost` for uwp. And so it can now be directly
    referenced from `vcpkg-ci-boost` which is already enforced to `pass` in
    ci.baseline.txt. :tada:
     - Restores sorting of `$portData`.
     - Use the same tarball download area and naming as `vcpkg install`.

    This PR doesn't include the updates to `boost-container` (#38806),
    `bost-interprocess` (#38815) and boost-math (#38728)

 ports/boost-accumulators/vcpkg.json          |   3 +-
 ports/boost-algorithm/vcpkg.json             |   3 +-
 ports/boost-align/vcpkg.json                 |   3 +-
 ports/boost-any/vcpkg.json                   |   3 +-
 ports/boost-array/vcpkg.json                 |   3 +-
 ports/boost-asio/vcpkg.json                  |   3 +-
 ports/boost-assert/vcpkg.json                |   3 +-
 ports/boost-assign/vcpkg.json                |   3 +-
 ports/boost-atomic/vcpkg.json                |   3 +-
 ports/boost-beast/vcpkg.json                 |   3 +-
 ports/boost-bimap/vcpkg.json                 |   3 +-
 ports/boost-bind/vcpkg.json                  |   3 +-
 ports/boost-build/vcpkg.json                 |   1 +
 ports/boost-callable-traits/vcpkg.json       |   3 +-
 ports/boost-charconv/vcpkg.json              |   3 +-
 ports/boost-chrono/vcpkg.json                |   3 +-
 ports/boost-circular-buffer/vcpkg.json       |   3 +-
 ports/boost-cmake/vcpkg.json                 |   2 +
 ports/boost-cobalt/vcpkg.json                |   3 +-
 ports/boost-compat/vcpkg.json                |   3 +-
 ports/boost-compatibility/vcpkg.json         |   3 +-
 ports/boost-compute/vcpkg.json               |   3 +-
 ports/boost-concept-check/vcpkg.json         |   3 +-
 ports/boost-config/vcpkg.json                |   3 +-
 ports/boost-container-hash/vcpkg.json        |   3 +-
 ports/boost-context/vcpkg.json               |   3 +-
 ports/boost-contract/vcpkg.json              |   3 +-
 ports/boost-conversion/vcpkg.json            |   3 +-
 ports/boost-convert/vcpkg.json               |   3 +-
 ports/boost-core/vcpkg.json                  |   3 +-
 ports/boost-coroutine/vcpkg.json             |   3 +-
 ports/boost-coroutine2/vcpkg.json            |   3 +-
 ports/boost-crc/vcpkg.json                   |   3 +-
 ports/boost-date-time/vcpkg.json             |   3 +-
 ports/boost-describe/vcpkg.json              |   3 +-
 ports/boost-detail/vcpkg.json                |   3 +-
 ports/boost-dll/vcpkg.json                   |   3 +-
 ports/boost-dynamic-bitset/vcpkg.json        |   3 +-
 ports/boost-endian/vcpkg.json                |   3 +-
 ports/boost-exception/vcpkg.json             |   3 +-
 ports/boost-fiber/vcpkg.json                 |   3 +-
 ports/boost-filesystem/vcpkg.json            |   3 +-
 ports/boost-flyweight/vcpkg.json             |   3 +-
 ports/boost-foreach/vcpkg.json               |   3 +-
 ports/boost-format/vcpkg.json                |   3 +-
 ports/boost-function-types/vcpkg.json        |   3 +-
 ports/boost-function/vcpkg.json              |   3 +-
 ports/boost-functional/vcpkg.json            |   3 +-
 ports/boost-fusion/vcpkg.json                |   3 +-
 ports/boost-geometry/vcpkg.json              |   3 +-
 ports/boost-gil/vcpkg.json                   |   3 +-
 ports/boost-graph-parallel/vcpkg.json        |   3 +-
 ports/boost-graph/vcpkg.json                 |   3 +-
 ports/boost-hana/vcpkg.json                  |   3 +-
 ports/boost-headers/vcpkg.json               |   3 +-
 ports/boost-heap/vcpkg.json                  |   3 +-
 ports/boost-histogram/vcpkg.json             |   3 +-
 ports/boost-hof/vcpkg.json                   |   3 +-
 ports/boost-icl/vcpkg.json                   |   3 +-
 ports/boost-integer/vcpkg.json               |   3 +-
 ports/boost-interval/vcpkg.json              |   3 +-
 ports/boost-intrusive/vcpkg.json             |   3 +-
 ports/boost-io/vcpkg.json                    |   3 +-
 ports/boost-iostreams/vcpkg.json             |   3 +-
 ports/boost-iterator/vcpkg.json              |   3 +-
 ports/boost-json/vcpkg.json                  |   3 +-
 ports/boost-lambda/vcpkg.json                |   3 +-
 ports/boost-lambda2/vcpkg.json               |   3 +-
 ports/boost-leaf/vcpkg.json                  |   3 +-
 ports/boost-lexical-cast/vcpkg.json          |   3 +-
 ports/boost-local-function/vcpkg.json        |   3 +-
 ports/boost-locale/vcpkg.json                |   3 +-
 ports/boost-lockfree/vcpkg.json              |   3 +-
 ports/boost-log/vcpkg.json                   |   3 +-
 ports/boost-logic/vcpkg.json                 |   3 +-
 ports/boost-metaparse/vcpkg.json             |   3 +-
 ports/boost-move/vcpkg.json                  |   3 +-
 ports/boost-mp11/vcpkg.json                  |   3 +-
 ports/boost-mpi/vcpkg.json                   |   3 +-
 ports/boost-mpl/vcpkg.json                   |   3 +-
 ports/boost-msm/vcpkg.json                   |   3 +-
 ports/boost-multi-array/vcpkg.json           |   3 +-
 ports/boost-multi-index/vcpkg.json           |   3 +-
 ports/boost-multiprecision/vcpkg.json        |   3 +-
 ports/boost-mysql/vcpkg.json                 |   3 +-
 ports/boost-nowide/vcpkg.json                |   3 +-
 ports/boost-numeric-conversion/vcpkg.json    |   3 +-
 ports/boost-odeint/vcpkg.json                |   3 +-
 ports/boost-optional/vcpkg.json              |   3 +-
 ports/boost-outcome/vcpkg.json               |   3 +-
 ports/boost-parameter-python/vcpkg.json      |   4 +-
 ports/boost-parameter/vcpkg.json             |   3 +-
 ports/boost-pfr/vcpkg.json                   |   3 +-
 ports/boost-phoenix/vcpkg.json               |   3 +-
 ports/boost-poly-collection/vcpkg.json       |   3 +-
 ports/boost-polygon/vcpkg.json               |   3 +-
 ports/boost-pool/vcpkg.json                  |   3 +-
 ports/boost-predef/vcpkg.json                |   3 +-
 ports/boost-preprocessor/vcpkg.json          |   3 +-
 ports/boost-process/vcpkg.json               |   3 +-
 ports/boost-program-options/vcpkg.json       |   3 +-
 ports/boost-property-map-parallel/vcpkg.json |   3 +-
 ports/boost-property-map/vcpkg.json          |   3 +-
 ports/boost-property-tree/vcpkg.json         |   3 +-
 ports/boost-proto/vcpkg.json                 |   3 +-
 ports/boost-ptr-container/vcpkg.json         |   3 +-
 ports/boost-python/vcpkg.json                |   3 +-
 ports/boost-qvm/vcpkg.json                   |   3 +-
 ports/boost-random/vcpkg.json                |   3 +-
 ports/boost-range/vcpkg.json                 |   3 +-
 ports/boost-ratio/vcpkg.json                 |   3 +-
 ports/boost-rational/vcpkg.json              |   3 +-
 ports/boost-redis/vcpkg.json                 |   3 +-
 ports/boost-regex/vcpkg.json                 |   3 +-
 ports/boost-safe-numerics/vcpkg.json         |   3 +-
 ports/boost-scope-exit/vcpkg.json            |   3 +-
 ports/boost-scope/vcpkg.json                 |   3 +-
 ports/boost-serialization/vcpkg.json         |   3 +-
 ports/boost-signals2/vcpkg.json              |   3 +-
 ports/boost-smart-ptr/vcpkg.json             |   3 +-
 ports/boost-sort/vcpkg.json                  |   3 +-
 ports/boost-spirit/vcpkg.json                |   3 +-
 ports/boost-stacktrace/vcpkg.json            |   3 +-
 ports/boost-statechart/vcpkg.json            |   3 +-
 ports/boost-static-assert/vcpkg.json         |   3 +-
 ports/boost-static-string/vcpkg.json         |   3 +-
 ports/boost-stl-interfaces/vcpkg.json        |   3 +-
 ports/boost-system/vcpkg.json                |   3 +-
 ports/boost-test/vcpkg.json                  |   3 +-
 ports/boost-thread/vcpkg.json                |   3 +-
 ports/boost-throw-exception/vcpkg.json       |   3 +-
 ports/boost-timer/vcpkg.json                 |   3 +-
 ports/boost-tokenizer/vcpkg.json             |   3 +-
 ports/boost-tti/vcpkg.json                   |   3 +-
 ports/boost-tuple/vcpkg.json                 |   3 +-
 ports/boost-type-erasure/vcpkg.json          |   3 +-
 ports/boost-type-index/vcpkg.json            |   3 +-
 ports/boost-type-traits/vcpkg.json           |   3 +-
 ports/boost-typeof/vcpkg.json                |   3 +-
 ports/boost-ublas/vcpkg.json                 |   3 +-
 ports/boost-uninstall/vcpkg.json             |   1 +
 ports/boost-units/vcpkg.json                 |   3 +-
 ports/boost-unordered/vcpkg.json             |   3 +-
 ports/boost-url/vcpkg.json                   |   3 +-
 ports/boost-utility/vcpkg.json               |   3 +-
 ports/boost-uuid/vcpkg.json                  |   3 +-
 ports/boost-variant/vcpkg.json               |   3 +-
 ports/boost-variant2/vcpkg.json              |   3 +-
 ports/boost-vmd/vcpkg.json                   |   3 +-
 ports/boost-wave/vcpkg.json                  |   3 +-
 ports/boost-winapi/vcpkg.json                |   3 +-
 ports/boost-xpressive/vcpkg.json             |   3 +-
 ports/boost-yap/vcpkg.json                   |   3 +-
 ports/boost/vcpkg.json                       |   6 +-
 scripts/boost/generate-ports.ps1             |  69 ++++--
 scripts/test_ports/vcpkg-ci-boost/vcpkg.json |   5 +-
 versions/b-/boost-accumulators.json          |   5 +
 versions/b-/boost-algorithm.json             |   5 +
 versions/b-/boost-align.json                 |   5 +
 versions/b-/boost-any.json                   |   5 +
 versions/b-/boost-array.json                 |   5 +
 versions/b-/boost-asio.json                  |   5 +
 versions/b-/boost-assert.json                |   5 +
 versions/b-/boost-assign.json                |   5 +
 versions/b-/boost-atomic.json                |   5 +
 versions/b-/boost-beast.json                 |   5 +
 versions/b-/boost-bimap.json                 |   5 +
 versions/b-/boost-bind.json                  |   5 +
 versions/b-/boost-build.json                 |   5 +
 versions/b-/boost-callable-traits.json       |   5 +
 versions/b-/boost-charconv.json              |   5 +
 versions/b-/boost-chrono.json                |   5 +
 versions/b-/boost-circular-buffer.json       |   5 +
 versions/b-/boost-cmake.json                 |   5 +
 versions/b-/boost-cobalt.json                |   5 +
 versions/b-/boost-compat.json                |   5 +
 versions/b-/boost-compatibility.json         |   5 +
 versions/b-/boost-compute.json               |   5 +
 versions/b-/boost-concept-check.json         |   5 +
 versions/b-/boost-config.json                |   5 +
 versions/b-/boost-container-hash.json        |   5 +
 versions/b-/boost-context.json               |   5 +
 versions/b-/boost-contract.json              |   5 +
 versions/b-/boost-conversion.json            |   5 +
 versions/b-/boost-convert.json               |   5 +
 versions/b-/boost-core.json                  |   5 +
 versions/b-/boost-coroutine.json             |   5 +
 versions/b-/boost-coroutine2.json            |   5 +
 versions/b-/boost-crc.json                   |   5 +
 versions/b-/boost-date-time.json             |   5 +
 versions/b-/boost-describe.json              |   5 +
 versions/b-/boost-detail.json                |   5 +
 versions/b-/boost-dll.json                   |   5 +
 versions/b-/boost-dynamic-bitset.json        |   5 +
 versions/b-/boost-endian.json                |   5 +
 versions/b-/boost-exception.json             |   5 +
 versions/b-/boost-fiber.json                 |   5 +
 versions/b-/boost-filesystem.json            |   5 +
 versions/b-/boost-flyweight.json             |   5 +
 versions/b-/boost-foreach.json               |   5 +
 versions/b-/boost-format.json                |   5 +
 versions/b-/boost-function-types.json        |   5 +
 versions/b-/boost-function.json              |   5 +
 versions/b-/boost-functional.json            |   5 +
 versions/b-/boost-fusion.json                |   5 +
 versions/b-/boost-geometry.json              |   5 +
 versions/b-/boost-gil.json                   |   5 +
 versions/b-/boost-graph-parallel.json        |   5 +
 versions/b-/boost-graph.json                 |   5 +
 versions/b-/boost-hana.json                  |   5 +
 versions/b-/boost-headers.json               |   5 +
 versions/b-/boost-heap.json                  |   5 +
 versions/b-/boost-histogram.json             |   5 +
 versions/b-/boost-hof.json                   |   5 +
 versions/b-/boost-icl.json                   |   5 +
 versions/b-/boost-integer.json               |   5 +
 versions/b-/boost-interval.json              |   5 +
 versions/b-/boost-intrusive.json             |   5 +
 versions/b-/boost-io.json                    |   5 +
 versions/b-/boost-iostreams.json             |   5 +
 versions/b-/boost-iterator.json              |   5 +
 versions/b-/boost-json.json                  |   5 +
 versions/b-/boost-lambda.json                |   5 +
 versions/b-/boost-lambda2.json               |   5 +
 versions/b-/boost-leaf.json                  |   5 +
 versions/b-/boost-lexical-cast.json          |   5 +
 versions/b-/boost-local-function.json        |   5 +
 versions/b-/boost-locale.json                |   5 +
 versions/b-/boost-lockfree.json              |   5 +
 versions/b-/boost-log.json                   |   5 +
 versions/b-/boost-logic.json                 |   5 +
 versions/b-/boost-metaparse.json             |   5 +
 versions/b-/boost-move.json                  |   5 +
 versions/b-/boost-mp11.json                  |   5 +
 versions/b-/boost-mpi.json                   |   5 +
 versions/b-/boost-mpl.json                   |   5 +
 versions/b-/boost-msm.json                   |   5 +
 versions/b-/boost-multi-array.json           |   5 +
 versions/b-/boost-multi-index.json           |   5 +
 versions/b-/boost-multiprecision.json        |   5 +
 versions/b-/boost-mysql.json                 |   5 +
 versions/b-/boost-nowide.json                |   5 +
 versions/b-/boost-numeric-conversion.json    |   5 +
 versions/b-/boost-odeint.json                |   5 +
 versions/b-/boost-optional.json              |   5 +
 versions/b-/boost-outcome.json               |   5 +
 versions/b-/boost-parameter-python.json      |   5 +
 versions/b-/boost-parameter.json             |   5 +
 versions/b-/boost-pfr.json                   |   5 +
 versions/b-/boost-phoenix.json               |   5 +
 versions/b-/boost-poly-collection.json       |   5 +
 versions/b-/boost-polygon.json               |   5 +
 versions/b-/boost-pool.json                  |   5 +
 versions/b-/boost-predef.json                |   5 +
 versions/b-/boost-preprocessor.json          |   5 +
 versions/b-/boost-process.json               |   5 +
 versions/b-/boost-program-options.json       |   5 +
 versions/b-/boost-property-map-parallel.json |   5 +
 versions/b-/boost-property-map.json          |   5 +
 versions/b-/boost-property-tree.json         |   5 +
 versions/b-/boost-proto.json                 |   5 +
 versions/b-/boost-ptr-container.json         |   5 +
 versions/b-/boost-python.json                |   5 +
 versions/b-/boost-qvm.json                   |   5 +
 versions/b-/boost-random.json                |   5 +
 versions/b-/boost-range.json                 |   5 +
 versions/b-/boost-ratio.json                 |   5 +
 versions/b-/boost-rational.json              |   5 +
 versions/b-/boost-redis.json                 |   5 +
 versions/b-/boost-regex.json                 |   5 +
 versions/b-/boost-safe-numerics.json         |   5 +
 versions/b-/boost-scope-exit.json            |   5 +
 versions/b-/boost-scope.json                 |   5 +
 versions/b-/boost-serialization.json         |   5 +
 versions/b-/boost-signals2.json              |   5 +
 versions/b-/boost-smart-ptr.json             |   5 +
 versions/b-/boost-sort.json                  |   5 +
 versions/b-/boost-spirit.json                |   5 +
 versions/b-/boost-stacktrace.json            |   5 +
 versions/b-/boost-statechart.json            |   5 +
 versions/b-/boost-static-assert.json         |   5 +
 versions/b-/boost-static-string.json         |   5 +
 versions/b-/boost-stl-interfaces.json        |   5 +
 versions/b-/boost-system.json                |   5 +
 versions/b-/boost-test.json                  |   5 +
 versions/b-/boost-thread.json                |   5 +
 versions/b-/boost-throw-exception.json       |   5 +
 versions/b-/boost-timer.json                 |   5 +
 versions/b-/boost-tokenizer.json             |   5 +
 versions/b-/boost-tti.json                   |   5 +
 versions/b-/boost-tuple.json                 |   5 +
 versions/b-/boost-type-erasure.json          |   5 +
 versions/b-/boost-type-index.json            |   5 +
 versions/b-/boost-type-traits.json           |   5 +
 versions/b-/boost-typeof.json                |   5 +
 versions/b-/boost-ublas.json                 |   5 +
 versions/b-/boost-uninstall.json             |   5 +
 versions/b-/boost-units.json                 |   5 +
 versions/b-/boost-unordered.json             |   5 +
 versions/b-/boost-url.json                   |   5 +
 versions/b-/boost-utility.json               |   5 +
 versions/b-/boost-uuid.json                  |   5 +
 versions/b-/boost-variant.json               |   5 +
 versions/b-/boost-variant2.json              |   5 +
 versions/b-/boost-vmd.json                   |   5 +
 versions/b-/boost-wave.json                  |   5 +
 versions/b-/boost-winapi.json                |   5 +
 versions/b-/boost-xpressive.json             |   5 +
 versions/b-/boost-yap.json                   |   5 +
 versions/b-/boost.json                       |   5 +
 versions/baseline.json                       | 308 +++++++++++++--------------
 311 files changed, 1284 insertions(+), 329 deletions(-)

2024-09-22 13:18:46,019 - 147 - INFO - run: git add .
2024-09-22 13:18:46,041 - 147 - INFO - run: git commit -m [vcpkg-scripts][boost] Improve generate-ports.ps1 (#38814) --author Kai Pastor <dg0yt@darc.de>
[main 0c54ec89a] [vcpkg-scripts][boost] Improve generate-ports.ps1 (#38814)
 Author: Kai Pastor <dg0yt@darc.de>
 3 files changed, 241 insertions(+)
 create mode 100644 ports/boost-algorithm/portfile.cmake
 create mode 100644 ports/boost-algorithm/vcpkg.json
 create mode 100644 versions/b-/boost-algorithm.json
2024-09-22 13:18:46,111 - 360 - WARNING - copy downloads/vcpkg/ports/boost-asio -> ./ports/boost-asio
2024-09-22 13:18:46,112 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-asio.json -> ./versions/b-/boost-asio.json
2024-09-22 13:18:46,113 - 382 - INFO - boost-asio
commit a8954b904ad2a6939ecd8fc213e87702fa1243ea
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-05-29 10:57:56 +0200

    [boost] fix hashes (#38979)

    - I did not update generate, lets hope the next boost update comes
    before there are other big changes needed.

    Fixes https://github.com/microsoft/vcpkg/issues/38974

 ports/boost-asio/portfile.cmake            |  2 +-
 ports/boost-asio/vcpkg.json                |  2 +-
 ports/boost-beast/portfile.cmake           |  2 +-
 ports/boost-beast/vcpkg.json               |  2 +-
 ports/boost-bimap/portfile.cmake           |  2 +-
 ports/boost-bimap/vcpkg.json               |  2 +-
 ports/boost-cobalt/portfile.cmake          |  2 +-
 ports/boost-cobalt/vcpkg.json              |  2 +-
 ports/boost-compat/portfile.cmake          |  2 +-
 ports/boost-compat/vcpkg.json              |  2 +-
 ports/boost-core/portfile.cmake            |  2 +-
 ports/boost-core/vcpkg.json                |  2 +-
 ports/boost-describe/portfile.cmake        |  2 +-
 ports/boost-describe/vcpkg.json            |  2 +-
 ports/boost-filesystem/portfile.cmake      |  2 +-
 ports/boost-filesystem/vcpkg.json          |  2 +-
 ports/boost-geometry/portfile.cmake        |  2 +-
 ports/boost-geometry/vcpkg.json            |  2 +-
 ports/boost-intrusive/portfile.cmake       |  2 +-
 ports/boost-intrusive/vcpkg.json           |  2 +-
 ports/boost-json/portfile.cmake            |  2 +-
 ports/boost-json/vcpkg.json                |  2 +-
 ports/boost-locale/portfile.cmake          |  2 +-
 ports/boost-locale/vcpkg.json              |  2 +-
 ports/boost-log/portfile.cmake             |  2 +-
 ports/boost-log/vcpkg.json                 |  2 +-
 ports/boost-math/portfile.cmake            |  2 +-
 ports/boost-math/vcpkg.json                |  3 +-
 ports/boost-msm/portfile.cmake             |  2 +-
 ports/boost-msm/vcpkg.json                 |  6 +++-
 ports/boost-multi-index/portfile.cmake     |  2 +-
 ports/boost-multi-index/vcpkg.json         |  2 +-
 ports/boost-multiprecision/portfile.cmake  |  2 +-
 ports/boost-multiprecision/vcpkg.json      |  2 +-
 ports/boost-mysql/portfile.cmake           |  2 +-
 ports/boost-mysql/vcpkg.json               |  2 +-
 ports/boost-nowide/portfile.cmake          |  2 +-
 ports/boost-nowide/vcpkg.json              |  2 +-
 ports/boost-outcome/portfile.cmake         |  2 +-
 ports/boost-outcome/vcpkg.json             |  2 +-
 ports/boost-pfr/portfile.cmake             |  2 +-
 ports/boost-pfr/vcpkg.json                 |  2 +-
 ports/boost-process/portfile.cmake         |  2 +-
 ports/boost-process/vcpkg.json             |  2 +-
 ports/boost-program-options/portfile.cmake |  2 +-
 ports/boost-program-options/vcpkg.json     |  2 +-
 ports/boost-redis/portfile.cmake           |  2 +-
 ports/boost-redis/vcpkg.json               |  2 +-
 ports/boost-stacktrace/portfile.cmake      |  2 +-
 ports/boost-stacktrace/vcpkg.json          |  2 +-
 ports/boost-timer/portfile.cmake           |  2 +-
 ports/boost-timer/vcpkg.json               |  2 +-
 ports/boost-unordered/portfile.cmake       |  2 +-
 ports/boost-unordered/vcpkg.json           |  2 +-
 ports/boost-variant2/portfile.cmake        |  2 +-
 ports/boost-variant2/vcpkg.json            |  2 +-
 ports/boost-wave/portfile.cmake            |  2 +-
 ports/boost-wave/vcpkg.json                |  2 +-
 versions/b-/boost-asio.json                |  5 +++
 versions/b-/boost-beast.json               |  5 +++
 versions/b-/boost-bimap.json               |  5 +++
 versions/b-/boost-cobalt.json              |  5 +++
 versions/b-/boost-compat.json              |  5 +++
 versions/b-/boost-core.json                |  5 +++
 versions/b-/boost-describe.json            |  5 +++
 versions/b-/boost-filesystem.json          |  5 +++
 versions/b-/boost-geometry.json            |  5 +++
 versions/b-/boost-intrusive.json           |  5 +++
 versions/b-/boost-json.json                |  5 +++
 versions/b-/boost-locale.json              |  5 +++
 versions/b-/boost-log.json                 |  5 +++
 versions/b-/boost-math.json                |  5 +++
 versions/b-/boost-msm.json                 |  5 +++
 versions/b-/boost-multi-index.json         |  5 +++
 versions/b-/boost-multiprecision.json      |  5 +++
 versions/b-/boost-mysql.json               |  5 +++
 versions/b-/boost-nowide.json              |  5 +++
 versions/b-/boost-outcome.json             |  5 +++
 versions/b-/boost-pfr.json                 |  5 +++
 versions/b-/boost-process.json             |  5 +++
 versions/b-/boost-program-options.json     |  5 +++
 versions/b-/boost-redis.json               |  5 +++
 versions/b-/boost-stacktrace.json          |  5 +++
 versions/b-/boost-timer.json               |  5 +++
 versions/b-/boost-unordered.json           |  5 +++
 versions/b-/boost-variant2.json            |  5 +++
 versions/b-/boost-wave.json                |  5 +++
 versions/baseline.json                     | 58 +++++++++++++++---------------
 88 files changed, 237 insertions(+), 87 deletions(-)

2024-09-22 13:18:46,113 - 147 - INFO - run: git add .
2024-09-22 13:18:46,136 - 147 - INFO - run: git commit -m [boost] fix hashes (#38979) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main 1fc6f0e0b] [boost] fix hashes (#38979)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 5 files changed, 304 insertions(+)
 create mode 100644 ports/boost-asio/opt-dep.diff
 create mode 100644 ports/boost-asio/portfile.cmake
 create mode 100644 ports/boost-asio/vcpkg.json
 create mode 100644 ports/boost-asio/windows_alloca_header.patch
 create mode 100644 versions/b-/boost-asio.json
2024-09-22 13:18:46,197 - 360 - WARNING - copy downloads/vcpkg/ports/boost-math -> ./ports/boost-math
2024-09-22 13:18:46,200 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-math.json -> ./versions/b-/boost-math.json
2024-09-22 13:18:46,202 - 382 - INFO - boost-math
commit 0151c07c081dba20642f7a580c814afc629d1970
Author: Osyotr <Osyotr@users.noreply.github.com>
Date:   2024-05-30 19:53:46 +0300

    [boost-math] Fix build on x64-linux-dynamic, add feature legacy (#38728)

    Fixes #38725
    Fixes #38714
    Fixed https://github.com/microsoft/vcpkg/issues/38955

 ports/autodock-vina/CMakeLists.txt    |  3 ---
 ports/autodock-vina/vcpkg.json        |  2 +-
 ports/boost-math/build-old-libs.patch |  8 ++++++--
 ports/boost-math/features.cmake       | 10 ++++++++++
 ports/boost-math/portfile.cmake       |  1 +
 ports/boost-math/vcpkg.json           |  9 +++++++--
 ports/cctag/vcpkg.json                |  9 +++++++--
 ports/vcpkg-boost/boost-install.cmake |  2 +-
 ports/vcpkg-boost/vcpkg.json          |  2 +-
 scripts/boost/generate-ports.ps1      |  8 ++++++++
 versions/a-/autodock-vina.json        |  5 +++++
 versions/b-/boost-math.json           |  5 +++++
 versions/baseline.json                |  8 ++++----
 versions/c-/cctag.json                |  5 +++++
 versions/v-/vcpkg-boost.json          |  5 +++++
 15 files changed, 66 insertions(+), 16 deletions(-)

2024-09-22 13:18:46,202 - 147 - INFO - run: git add .
2024-09-22 13:18:46,222 - 147 - INFO - run: git commit -m [boost-math] Fix build on x64-linux-dynamic, add feature legacy (#38728) --author Osyotr <Osyotr@users.noreply.github.com>
[main 48e2f36db] [boost-math] Fix build on x64-linux-dynamic, add feature legacy (#38728)
 Author: Osyotr <Osyotr@users.noreply.github.com>
 6 files changed, 369 insertions(+)
 create mode 100644 ports/boost-math/build-old-libs.patch
 create mode 100644 ports/boost-math/features.cmake
 create mode 100644 ports/boost-math/opt-random.diff
 create mode 100644 ports/boost-math/portfile.cmake
 create mode 100644 ports/boost-math/vcpkg.json
 create mode 100644 versions/b-/boost-math.json
2024-09-22 13:18:46,327 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-get-python -> ./ports/vcpkg-get-python
2024-09-22 13:18:46,328 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-get-python.json -> ./versions/v-/vcpkg-get-python.json
2024-09-22 13:18:46,329 - 382 - INFO - vcpkg-get-python
commit 2324733d55baa3e784d8f77a8861982d40f1c35c
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-06-17 20:36:07 +0200

    [python3] add vcpkg_get_vcpkg_installed_python (#38929)

 ports/python3/portfile.cmake                   |  8 ++++-
 ports/python3/vcpkg-port-config.cmake          |  1 +
 ports/python3/vcpkg.json                       |  6 +++-
 ports/vcpkg-get-python/portfile.cmake          |  7 ++++
 ports/vcpkg-get-python/vcpkg-port-config.cmake | 46 ++++++++++++++++++++++++++
 ports/vcpkg-get-python/vcpkg.json              |  6 ++++
 versions/baseline.json                         |  6 +++-
 versions/p-/python3.json                       |  5 +++
 versions/v-/vcpkg-get-python.json              |  9 +++++
 9 files changed, 91 insertions(+), 3 deletions(-)

2024-09-22 13:18:46,329 - 147 - INFO - run: git add .
2024-09-22 13:18:46,350 - 147 - INFO - run: git commit -m [python3] add vcpkg_get_vcpkg_installed_python (#38929) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main 844240f81] [python3] add vcpkg_get_vcpkg_installed_python (#38929)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 4 files changed, 68 insertions(+)
 create mode 100644 ports/vcpkg-get-python/portfile.cmake
 create mode 100644 ports/vcpkg-get-python/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-get-python/vcpkg.json
 create mode 100644 versions/v-/vcpkg-get-python.json
2024-09-22 13:18:46,414 - 360 - WARNING - copy downloads/vcpkg/ports/liblzma -> ./ports/liblzma
2024-09-22 13:18:46,415 - 369 - WARNING - copy downloads/vcpkg/versions/l-/liblzma.json -> ./versions/l-/liblzma.json
2024-09-22 13:18:46,416 - 382 - INFO - liblzma
commit 9e80334e7ce1ed8f561ed0ff0890396954921dc5
Author: Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
Date:   2024-06-18 22:34:27 +0300

    [liblzma] Update to version 5.6.2. (#39024)

 ports/liblzma/add_support_ios.patch    | 20 --------------------
 ports/liblzma/build-tools.patch        | 19 +++++++++----------
 ports/liblzma/fix_config_include.patch | 12 ------------
 ports/liblzma/portfile.cmake           | 10 +++++-----
 ports/liblzma/vcpkg.json               |  5 ++---
 ports/liblzma/win_output_name.patch    | 10 ++++++----
 versions/baseline.json                 |  2 +-
 versions/l-/liblzma.json               |  5 +++++
 8 files changed, 28 insertions(+), 55 deletions(-)

2024-09-22 13:18:46,416 - 147 - INFO - run: git add .
2024-09-22 13:18:46,437 - 147 - INFO - run: git commit -m [liblzma] Update to version 5.6.2. (#39024) --author Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
[main 7e7c00376] [liblzma] Update to version 5.6.2. (#39024)
 Author: Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>
 7 files changed, 348 insertions(+)
 create mode 100644 ports/liblzma/build-tools.patch
 create mode 100644 ports/liblzma/portfile.cmake
 create mode 100644 ports/liblzma/usage
 create mode 100644 ports/liblzma/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/liblzma/vcpkg.json
 create mode 100644 ports/liblzma/win_output_name.patch
 create mode 100644 versions/l-/liblzma.json
2024-09-22 13:18:46,523 - 360 - WARNING - copy downloads/vcpkg/ports/gettext -> ./ports/gettext
2024-09-22 13:18:46,529 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gettext.json -> ./versions/g-/gettext.json
2024-09-22 13:18:46,530 - 382 - INFO - gettext
commit 6db51d86a9c2796581d74c9a7eb46e52ee8cb7eb
Author: gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
Date:   2024-06-20 07:07:05 +1000

    [vcpkg_replace_string] warn unchanged by call (#34719)

    If a call to `vcpkg_replace_string` makes no changes i.e doesn't
    effectively replace a string, A warning is logged.

    This should also help identify ports that no longer need these calls to
    fix things in `.pc` files etc.

 ports/activemq-cpp/portfile.cmake                  |   2 +-
 ports/activemq-cpp/vcpkg.json                      |   2 +-
 ports/apr/portfile.cmake                           |   8 +-
 ports/apr/vcpkg.json                               |   1 +
 ports/armadillo/portfile.cmake                     |   6 +-
 ports/armadillo/vcpkg.json                         |   1 +
 ports/assimp/portfile.cmake                        |   2 +-
 ports/assimp/vcpkg.json                            |   1 +
 ports/aws-sdk-cpp/portfile.cmake                   |   4 +-
 ports/aws-sdk-cpp/vcpkg.json                       |   2 +-
 ports/blitz/portfile.cmake                         |   8 +-
 ports/blitz/vcpkg.json                             |   2 +-
 ports/botan/portfile.cmake                         |   4 +-
 ports/botan/vcpkg.json                             |   1 +
 ports/ccfits/portfile.cmake                        |   2 +-
 ports/ccfits/vcpkg.json                            |   2 +-
 ports/cfitsio/portfile.cmake                       |   1 +
 ports/cfitsio/vcpkg.json                           |   2 +-
 ports/curl/portfile.cmake                          |   8 +-
 ports/curl/vcpkg.json                              |   2 +-
 ports/dcmtk/portfile.cmake                         |   8 +-
 ports/dcmtk/vcpkg.json                             |   2 +-
 ports/duktape/portfile.cmake                       |   6 +-
 ports/duktape/vcpkg.json                           |   2 +-
 ports/easyhook/portfile.cmake                      |   2 +
 ports/easyhook/vcpkg.json                          |   2 +-
 ports/fbthrift/portfile.cmake                      |   2 +-
 ports/fbthrift/vcpkg.json                          |   1 +
 ports/ffmpeg/portfile.cmake                        |   4 +-
 ports/ffmpeg/vcpkg.json                            |   2 +-
 ports/fontconfig/portfile.cmake                    |  10 +-
 ports/fontconfig/vcpkg.json                        |   2 +-
 ports/freeglut/portfile.cmake                      |   4 +-
 ports/freeglut/vcpkg.json                          |   2 +-
 ports/freerdp/portfile.cmake                       |   6 +-
 ports/freerdp/vcpkg.json                           |   2 +-
 ports/geogram/portfile.cmake                       |   3 +-
 ports/geogram/vcpkg.json                           |   2 +-
 ports/gettext/portfile.cmake                       |   2 +-
 ports/gettext/vcpkg.json                           |   1 +
 ports/glib/portfile.cmake                          |   6 +-
 ports/glib/vcpkg.json                              |   2 +-
 ports/graphqlparser/portfile.cmake                 |   2 +-
 ports/graphqlparser/vcpkg.json                     |   2 +-
 ports/graphviz/portfile.cmake                      |   2 +-
 ports/graphviz/vcpkg.json                          |   2 +-
 ports/guile/portfile.cmake                         |   4 +-
 ports/guile/vcpkg.json                             |   1 +
 ports/gz-common5/portfile.cmake                    |   3 +-
 ports/gz-common5/vcpkg.json                        |   2 +-
 ports/hayai/portfile.cmake                         |   2 +
 ports/hayai/vcpkg.json                             |   2 +-
 ports/hdf5/portfile.cmake                          |   6 +-
 ports/hdf5/vcpkg.json                              |   1 +
 ports/hidapi/portfile.cmake                        |   2 +-
 ports/hidapi/vcpkg.json                            |   1 +
 ports/hpx/portfile.cmake                           |   2 +-
 ports/hpx/vcpkg.json                               |   1 +
 ports/hwloc/portfile.cmake                         |   4 +-
 ports/hwloc/vcpkg.json                             |   1 +
 ports/icu/portfile.cmake                           |   2 +-
 ports/icu/vcpkg.json                               |   2 +-
 ports/intel-mkl/portfile.cmake                     |   4 +-
 ports/intel-mkl/vcpkg.json                         |   2 +-
 ports/libevent/portfile.cmake                      |   1 +
 ports/libevent/vcpkg.json                          |   1 +
 ports/libgeotiff/portfile.cmake                    |   1 -
 ports/libgeotiff/vcpkg.json                        |   1 +
 ports/libheif/portfile.cmake                       |   4 +-
 ports/libheif/vcpkg.json                           |   2 +-
 ports/libjpeg-turbo/portfile.cmake                 |   8 +-
 ports/libjpeg-turbo/vcpkg.json                     |   1 +
 ports/libsigcpp/portfile.cmake                     |   2 +-
 ports/libsigcpp/vcpkg.json                         |   1 +
 ports/libspatialite/portfile.cmake                 |   2 +-
 ports/libspatialite/vcpkg.json                     |   2 +-
 ports/libssh/portfile.cmake                        |   4 +-
 ports/libssh/vcpkg.json                            |   2 +-
 ports/libssh2/portfile.cmake                       |   4 +-
 ports/libssh2/vcpkg.json                           |   2 +-
 ports/libwebsockets/portfile.cmake                 |   4 +-
 ports/libwebsockets/vcpkg.json                     |   1 +
 ports/libxslt/portfile.cmake                       |   2 +-
 ports/libxslt/vcpkg.json                           |   2 +-
 ports/mathgl/portfile.cmake                        |   4 +-
 ports/mathgl/vcpkg.json                            |   2 +-
 ports/mimalloc/portfile.cmake                      |   4 +-
 ports/mimalloc/vcpkg.json                          |   2 +-
 ports/minizip/portfile.cmake                       |   2 +-
 ports/minizip/vcpkg.json                           |   1 +
 ports/monkeys-audio/portfile.cmake                 |   2 +
 ports/monkeys-audio/vcpkg.json                     |   2 +-
 ports/nanomsg/portfile.cmake                       |   1 +
 ports/nanomsg/vcpkg.json                           |   2 +-
 ports/nlohmann-json/portfile.cmake                 |   1 +
 ports/nlohmann-json/vcpkg.json                     |   1 +
 ports/ogre/portfile.cmake                          |   6 +-
 ports/ogre/vcpkg.json                              |   1 +
 ports/omniorb/portfile.cmake                       |   4 +-
 ports/omniorb/vcpkg.json                           |   2 +-
 ports/ompl/portfile.cmake                          |   2 +-
 ports/ompl/vcpkg.json                              |   1 +
 ports/opencv3/portfile.cmake                       |   5 +-
 ports/opencv3/vcpkg.json                           |   2 +-
 ports/opencv4/portfile.cmake                       |   1 +
 ports/opencv4/vcpkg.json                           |   2 +-
 ports/paraview/portfile.cmake                      |   3 +-
 ports/paraview/vcpkg.json                          |   1 +
 ports/pipewire/portfile.cmake                      |   4 +-
 ports/pipewire/vcpkg.json                          |   1 +
 ports/protobuf/portfile.cmake                      |   1 +
 ports/protobuf/vcpkg.json                          |   2 +-
 ports/python3/portfile.cmake                       |   2 +-
 ports/python3/vcpkg.json                           |   2 +-
 ports/qpid-proton/portfile.cmake                   |   2 +-
 ports/qpid-proton/vcpkg.json                       |   2 +-
 ports/qt5-base/cmake/qt_fix_makefile_install.cmake |   2 +-
 ports/qt5-base/vcpkg.json                          |   1 +
 ports/qtapplicationmanager/portfile.cmake          |   2 +-
 ports/qtapplicationmanager/vcpkg.json              |   1 +
 ports/qtbase/cmake/qt_install_submodule.cmake      |   7 +-
 ports/qtbase/portfile.cmake                        |   3 +-
 ports/qtbase/vcpkg.json                            |   1 +
 ports/qtinterfaceframework/portfile.cmake          |   2 +-
 ports/qtinterfaceframework/vcpkg.json              |   1 +
 ports/qtmultimedia/portfile.cmake                  |   2 +-
 ports/qtmultimedia/vcpkg.json                      |   1 +
 ports/ryml/portfile.cmake                          |   2 +-
 ports/ryml/vcpkg.json                              |   1 +
 ports/sail/portfile.cmake                          |   4 +-
 ports/sail/vcpkg.json                              |   1 +
 ports/sdl2/portfile.cmake                          |   8 +-
 ports/sdl2/vcpkg.json                              |   1 +
 ports/shiftmedia-libgcrypt/portfile.cmake          |   2 +
 ports/shiftmedia-libgcrypt/vcpkg.json              |   1 +
 ports/shiftmedia-libgnutls/portfile.cmake          |   2 +
 ports/shiftmedia-libgnutls/vcpkg.json              |   2 +-
 ports/skia/portfile.cmake                          |   2 +-
 ports/skia/vcpkg.json                              |   1 +
 ports/sockpp/portfile.cmake                        |   2 +-
 ports/sockpp/vcpkg.json                            |   1 +
 ports/stxxl/portfile.cmake                         |   1 +
 ports/stxxl/vcpkg.json                             |   2 +-
 ports/symengine/portfile.cmake                     |   1 +
 ports/symengine/vcpkg.json                         |   2 +-
 ports/taglib/portfile.cmake                        |   4 +-
 ports/taglib/vcpkg.json                            |   2 +-
 ports/uthenticode/portfile.cmake                   |   5 -
 ports/uthenticode/vcpkg.json                       |   1 +
 ports/vcpkg-qmake/vcpkg.json                       |   2 +-
 .../vcpkg-qmake/z_vcpkg_qmake_fix_makefiles.cmake  |   3 +-
 ports/vcpkg-tool-meson/vcpkg.json                  |   2 +-
 ports/vcpkg-tool-meson/vcpkg_install_meson.cmake   |   2 +-
 ports/vtk/portfile.cmake                           |   2 +-
 ports/vtk/vcpkg.json                               |   1 +
 ports/wxwidgets/portfile.cmake                     |   4 +-
 ports/wxwidgets/vcpkg.json                         |   1 +
 ports/x264/portfile.cmake                          |   2 +-
 ports/x264/vcpkg.json                              |   1 +
 ports/xcb/portfile.cmake                           |   4 +-
 ports/xcb/vcpkg.json                               |   2 +-
 ports/xmlsec/portfile.cmake                        |   1 +
 ports/xmlsec/vcpkg.json                            |   1 +
 ports/zfp/portfile.cmake                           |   2 +-
 ports/zfp/vcpkg.json                               |   2 +-
 ports/zopfli/portfile.cmake                        |   4 +
 ports/zopfli/vcpkg.json                            |   2 +-
 scripts/cmake/vcpkg_install_meson.cmake            |   2 +-
 scripts/cmake/vcpkg_replace_string.cmake           |  17 ++-
 versions/a-/activemq-cpp.json                      |   5 +
 versions/a-/apr.json                               |   5 +
 versions/a-/armadillo.json                         |   5 +
 versions/a-/assimp.json                            |   5 +
 versions/a-/aws-sdk-cpp.json                       |   5 +
 versions/b-/blitz.json                             |   5 +
 versions/b-/botan.json                             |   5 +
 versions/baseline.json                             | 166 ++++++++++-----------
 versions/c-/ccfits.json                            |   5 +
 versions/c-/cfitsio.json                           |   5 +
 versions/c-/curl.json                              |   5 +
 versions/d-/dcmtk.json                             |   5 +
 versions/d-/duktape.json                           |   5 +
 versions/e-/easyhook.json                          |   5 +
 versions/f-/fbthrift.json                          |   5 +
 versions/f-/ffmpeg.json                            |   5 +
 versions/f-/fontconfig.json                        |   5 +
 versions/f-/freeglut.json                          |   5 +
 versions/f-/freerdp.json                           |   5 +
 versions/g-/geogram.json                           |   5 +
 versions/g-/gettext.json                           |   5 +
 versions/g-/glib.json                              |   5 +
 versions/g-/graphqlparser.json                     |   5 +
 versions/g-/graphviz.json                          |   5 +
 versions/g-/guile.json                             |   5 +
 versions/g-/gz-common5.json                        |   5 +
 versions/h-/hayai.json                             |   5 +
 versions/h-/hdf5.json                              |   5 +
 versions/h-/hidapi.json                            |   5 +
 versions/h-/hpx.json                               |   5 +
 versions/h-/hwloc.json                             |   5 +
 versions/i-/icu.json                               |   5 +
 versions/i-/intel-mkl.json                         |   5 +
 versions/l-/libevent.json                          |   5 +
 versions/l-/libgeotiff.json                        |   5 +
 versions/l-/libheif.json                           |   5 +
 versions/l-/libjpeg-turbo.json                     |   5 +
 versions/l-/libsigcpp.json                         |   5 +
 versions/l-/libspatialite.json                     |   5 +
 versions/l-/libssh.json                            |   5 +
 versions/l-/libssh2.json                           |   5 +
 versions/l-/libwebsockets.json                     |   5 +
 versions/l-/libxslt.json                           |   5 +
 versions/m-/mathgl.json                            |   5 +
 versions/m-/mimalloc.json                          |   5 +
 versions/m-/minizip.json                           |   5 +
 versions/m-/monkeys-audio.json                     |   5 +
 versions/n-/nanomsg.json                           |   5 +
 versions/n-/nlohmann-json.json                     |   5 +
 versions/o-/ogre.json                              |   5 +
 versions/o-/omniorb.json                           |   5 +
 versions/o-/ompl.json                              |   5 +
 versions/o-/opencv3.json                           |   5 +
 versions/o-/opencv4.json                           |   5 +
 versions/p-/paraview.json                          |   5 +
 versions/p-/pipewire.json                          |   5 +
 versions/p-/protobuf.json                          |   5 +
 versions/p-/python3.json                           |   5 +
 versions/q-/qpid-proton.json                       |   5 +
 versions/q-/qt5-base.json                          |   5 +
 versions/q-/qtapplicationmanager.json              |   5 +
 versions/q-/qtbase.json                            |   5 +
 versions/q-/qtinterfaceframework.json              |   5 +
 versions/q-/qtmultimedia.json                      |   5 +
 versions/r-/ryml.json                              |   5 +
 versions/s-/sail.json                              |   5 +
 versions/s-/sdl2.json                              |   5 +
 versions/s-/shiftmedia-libgcrypt.json              |   5 +
 versions/s-/shiftmedia-libgnutls.json              |   5 +
 versions/s-/skia.json                              |   5 +
 versions/s-/sockpp.json                            |   5 +
 versions/s-/stxxl.json                             |   5 +
 versions/s-/symengine.json                         |   5 +
 versions/t-/taglib.json                            |   5 +
 versions/u-/uthenticode.json                       |   5 +
 versions/v-/vcpkg-qmake.json                       |   5 +
 versions/v-/vcpkg-tool-meson.json                  |   5 +
 versions/v-/vtk.json                               |   5 +
 versions/w-/wxwidgets.json                         |   5 +
 versions/x-/x264.json                              |   5 +
 versions/x-/xcb.json                               |   5 +
 versions/x-/xmlsec.json                            |   5 +
 versions/z-/zfp.json                               |   5 +
 versions/z-/zopfli.json                            |   5 +
 253 files changed, 752 insertions(+), 258 deletions(-)

2024-09-22 13:18:46,531 - 147 - INFO - run: git add .
2024-09-22 13:18:46,553 - 147 - INFO - run: git commit -m [vcpkg_replace_string] warn unchanged by call (#34719) --author gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
[main ed54cbd3b] [vcpkg_replace_string] warn unchanged by call (#34719)
 Author: gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
 13 files changed, 883 insertions(+)
 create mode 100644 ports/gettext/0003-Fix-win-unicode-paths.patch
 create mode 100644 ports/gettext/assume-modern-darwin.patch
 create mode 100644 ports/gettext/bashify.cmake
 create mode 100644 ports/gettext/config-step-order.patch
 create mode 100644 ports/gettext/install-autopoint.cmake
 create mode 100644 ports/gettext/parallel-gettext-tools.patch
 create mode 100644 ports/gettext/portfile.cmake
 create mode 100644 ports/gettext/rel_path.patch
 create mode 100644 ports/gettext/subdirs.patch
 create mode 100644 ports/gettext/uwp.patch
 create mode 100644 ports/gettext/vcpkg-port-config.cmake
 create mode 100644 ports/gettext/vcpkg.json
 create mode 100644 versions/g-/gettext.json
2024-09-22 13:18:46,616 - 360 - WARNING - copy downloads/vcpkg/ports/gettext-libintl -> ./ports/gettext-libintl
2024-09-22 13:18:46,619 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gettext-libintl.json -> ./versions/g-/gettext-libintl.json
2024-09-22 13:18:46,619 - 382 - INFO - gettext-libintl
commit b593af97f717a0821badaf159d1f1c8f0463c245
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-05 20:06:12 +0200

    [gettext-libintl] Handle atypical Linux installations (#39662)

    Co-authored-by: Lily Wang <v-lilywang@microsoft.com>

 ports/gettext-libintl/detect/CMakeLists.txt | 16 ++++++++++++++++
 ports/gettext-libintl/portfile.cmake        | 21 ++++++++++++++++-----
 ports/gettext-libintl/vcpkg.json            |  7 ++++++-
 versions/baseline.json                      |  2 +-
 versions/g-/gettext-libintl.json            |  5 +++++
 5 files changed, 44 insertions(+), 7 deletions(-)

2024-09-22 13:18:46,619 - 147 - INFO - run: git add .
2024-09-22 13:18:46,640 - 147 - INFO - run: git commit -m [gettext-libintl] Handle atypical Linux installations (#39662) --author Kai Pastor <dg0yt@darc.de>
[main ea209d198] [gettext-libintl] Handle atypical Linux installations (#39662)
 Author: Kai Pastor <dg0yt@darc.de>
 9 files changed, 345 insertions(+)
 create mode 100644 ports/gettext-libintl/0003-Fix-win-unicode-paths.patch
 create mode 100644 ports/gettext-libintl/bashify.cmake
 create mode 100644 ports/gettext-libintl/detect/CMakeLists.txt
 create mode 100644 ports/gettext-libintl/portfile.cmake
 create mode 100644 ports/gettext-libintl/usage
 create mode 100644 ports/gettext-libintl/uwp.patch
 create mode 100644 ports/gettext-libintl/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/gettext-libintl/vcpkg.json
 create mode 100644 versions/g-/gettext-libintl.json
2024-09-22 13:18:46,703 - 360 - WARNING - copy downloads/vcpkg/ports/icu -> ./ports/icu
2024-09-22 13:18:46,708 - 369 - WARNING - copy downloads/vcpkg/versions/i-/icu.json -> ./versions/i-/icu.json
2024-09-22 13:18:46,709 - 382 - INFO - icu
commit f3e209dba79087e8e6e66aa87e954e53e565be16
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-08 16:15:55 +0200

    [icu] Fix mingw (#39742)

 ports/icu/mingw-strict-ansi.diff | 12 ++++++++++++
 ports/icu/portfile.cmake         |  1 +
 ports/icu/vcpkg.json             |  2 +-
 versions/baseline.json           |  2 +-
 versions/i-/icu.json             |  5 +++++
 5 files changed, 20 insertions(+), 2 deletions(-)

2024-09-22 13:18:46,710 - 147 - INFO - run: git add .
2024-09-22 13:18:46,732 - 147 - INFO - run: git commit -m [icu] Fix mingw (#39742) --author Kai Pastor <dg0yt@darc.de>
[main b10f43805] [icu] Fix mingw (#39742)
 Author: Kai Pastor <dg0yt@darc.de>
 14 files changed, 666 insertions(+)
 create mode 100644 ports/icu/darwin-rpath.patch
 create mode 100644 ports/icu/disable-escapestr-tool.patch
 create mode 100644 ports/icu/disable-static-prefix.patch
 create mode 100644 ports/icu/fix-extra.patch
 create mode 100644 ports/icu/fix-win-build.patch
 create mode 100644 ports/icu/fix_parallel_build_on_windows.patch
 create mode 100644 ports/icu/mingw-dll-install.patch
 create mode 100644 ports/icu/mingw-strict-ansi.diff
 create mode 100644 ports/icu/portfile.cmake
 create mode 100644 ports/icu/remove-MD-from-configure.patch
 create mode 100644 ports/icu/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/icu/vcpkg-cross-data.patch
 create mode 100644 ports/icu/vcpkg.json
 create mode 100644 versions/i-/icu.json
2024-09-22 13:18:46,793 - 360 - WARNING - copy downloads/vcpkg/ports/libiconv -> ./ports/libiconv
2024-09-22 13:18:46,795 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libiconv.json -> ./versions/l-/libiconv.json
2024-09-22 13:18:46,796 - 382 - INFO - libiconv
commit 460f9487ff827da59f016b7383839087081da72f
Author: Alonso Schaich <alonsoschaich@fastmail.fm>
Date:   2024-07-15 18:37:21 +0000

    [libiconv] Deploy on BSDs (#39824)

 ports/libiconv/portfile.cmake | 2 +-
 ports/libiconv/vcpkg.json     | 2 +-
 versions/baseline.json        | 2 +-
 versions/l-/libiconv.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:18:46,796 - 147 - INFO - run: git add .
2024-09-22 13:18:46,817 - 147 - INFO - run: git commit -m [libiconv] Deploy on BSDs (#39824) --author Alonso Schaich <alonsoschaich@fastmail.fm>
[main 31851750e] [libiconv] Deploy on BSDs (#39824)
 Author: Alonso Schaich <alonsoschaich@fastmail.fm>
 9 files changed, 347 insertions(+)
 create mode 100644 ports/libiconv/0002-Config-for-MSVC.patch
 create mode 100644 ports/libiconv/0003-Add-export.patch
 create mode 100644 ports/libiconv/0004-ModuleFileName.patch
 create mode 100644 ports/libiconv/clang-fortify.patch
 create mode 100644 ports/libiconv/portfile.cmake
 create mode 100644 ports/libiconv/usage
 create mode 100644 ports/libiconv/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/libiconv/vcpkg.json
 create mode 100644 versions/l-/libiconv.json
2024-09-22 13:18:46,878 - 360 - WARNING - copy downloads/vcpkg/ports/boost-mpi -> ./ports/boost-mpi
2024-09-22 13:18:46,879 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-mpi.json -> ./versions/b-/boost-mpi.json
2024-09-22 13:18:46,880 - 382 - INFO - boost-mpi
commit aae75b35540713013dd231c7406a72e3feb43e2e
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-07-24 19:18:11 +0200

    [boost-python] remove features (#40054)

 ports/boost-mpi/vcpkg.json                   |  5 +----
 ports/boost-python/vcpkg.json                | 23 +++--------------------
 scripts/boost/generate-ports.ps1             | 18 ++----------------
 scripts/test_ports/vcpkg-ci-boost/vcpkg.json | 11 -----------
 versions/b-/boost-mpi.json                   |  5 +++++
 versions/b-/boost-python.json                |  5 +++++
 versions/baseline.json                       |  4 ++--
 7 files changed, 18 insertions(+), 53 deletions(-)

2024-09-22 13:18:46,880 - 147 - INFO - run: git add .
2024-09-22 13:18:46,902 - 147 - INFO - run: git commit -m [boost-python] remove features (#40054) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main d5542b075] [boost-python] remove features (#40054)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 3 files changed, 282 insertions(+)
 create mode 100644 ports/boost-mpi/portfile.cmake
 create mode 100644 ports/boost-mpi/vcpkg.json
 create mode 100644 versions/b-/boost-mpi.json
2024-09-22 13:18:46,967 - 360 - WARNING - copy downloads/vcpkg/ports/vcpkg-tool-meson -> ./ports/vcpkg-tool-meson
2024-09-22 13:18:46,970 - 369 - WARNING - copy downloads/vcpkg/versions/v-/vcpkg-tool-meson.json -> ./versions/v-/vcpkg-tool-meson.json
2024-09-22 13:18:46,971 - 382 - INFO - vcpkg-tool-meson
commit fde6eac0a7a864032f888796f4d2b459b2cc0c5a
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-30 08:03:10 +0200

    [vcpkg-tool-meson] Update to 1.5.1 (#40138)

 ports/vcpkg-tool-meson/adjust-python-dep.patch     | 53 +++++++++++-----------
 ports/vcpkg-tool-meson/meson-1.4-llvm-18.diff      | 13 ------
 ports/vcpkg-tool-meson/portfile.cmake              |  1 -
 .../remove-freebsd-pcfile-specialization.patch     | 22 ++++-----
 ports/vcpkg-tool-meson/vcpkg-port-config.cmake     |  5 +-
 ports/vcpkg-tool-meson/vcpkg.json                  |  8 ++--
 ports/vcpkg-tool-meson/vcpkg_configure_meson.cmake | 18 ++++----
 versions/baseline.json                             |  4 +-
 versions/v-/vcpkg-tool-meson.json                  |  5 ++
 9 files changed, 58 insertions(+), 71 deletions(-)

2024-09-22 13:18:46,971 - 147 - INFO - run: git add .
2024-09-22 13:18:46,993 - 147 - INFO - run: git commit -m [vcpkg-tool-meson] Update to 1.5.1 (#40138) --author Kai Pastor <dg0yt@darc.de>
[main bbfee7fdb] [vcpkg-tool-meson] Update to 1.5.1 (#40138)
 Author: Kai Pastor <dg0yt@darc.de>
 12 files changed, 887 insertions(+)
 create mode 100644 ports/vcpkg-tool-meson/adjust-args.patch
 create mode 100644 ports/vcpkg-tool-meson/adjust-python-dep.patch
 create mode 100644 ports/vcpkg-tool-meson/install.cmake
 create mode 100644 ports/vcpkg-tool-meson/meson-intl.patch
 create mode 100644 ports/vcpkg-tool-meson/meson.template.in
 create mode 100644 ports/vcpkg-tool-meson/portfile.cmake
 create mode 100644 ports/vcpkg-tool-meson/remove-freebsd-pcfile-specialization.patch
 create mode 100644 ports/vcpkg-tool-meson/vcpkg-port-config.cmake
 create mode 100644 ports/vcpkg-tool-meson/vcpkg.json
 create mode 100644 ports/vcpkg-tool-meson/vcpkg_configure_meson.cmake
 create mode 100644 ports/vcpkg-tool-meson/vcpkg_install_meson.cmake
 create mode 100644 versions/v-/vcpkg-tool-meson.json
2024-09-22 13:18:47,059 - 360 - WARNING - copy downloads/vcpkg/ports/pkgconf -> ./ports/pkgconf
2024-09-22 13:18:47,061 - 369 - WARNING - copy downloads/vcpkg/versions/p-/pkgconf.json -> ./versions/p-/pkgconf.json
2024-09-22 13:18:47,062 - 382 - INFO - pkgconf
commit 791aeb5cb69b510175e2e547acc29183c87cbbac
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-08-13 01:44:08 +0200

    [pkgconf] Update to 2.3.0 (#40358)

 ports/pkgconf/portfile.cmake | 2 +-
 ports/pkgconf/vcpkg.json     | 2 +-
 versions/baseline.json       | 2 +-
 versions/p-/pkgconf.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:18:47,062 - 147 - INFO - run: git add .
2024-09-22 13:18:47,084 - 147 - INFO - run: git commit -m [pkgconf] Update to 2.3.0 (#40358) --author Kai Pastor <dg0yt@darc.de>
[main df50385bd] [pkgconf] Update to 2.3.0 (#40358)
 Author: Kai Pastor <dg0yt@darc.de>
 3 files changed, 149 insertions(+)
 create mode 100644 ports/pkgconf/portfile.cmake
 create mode 100644 ports/pkgconf/vcpkg.json
 create mode 100644 versions/p-/pkgconf.json
2024-09-22 13:18:47,162 - 360 - WARNING - copy downloads/vcpkg/ports/sqlite3 -> ./ports/sqlite3
2024-09-22 13:18:47,165 - 369 - WARNING - copy downloads/vcpkg/versions/s-/sqlite3.json -> ./versions/s-/sqlite3.json
2024-09-22 13:18:47,166 - 382 - INFO - sqlite3
commit c3f7523208aa1c794331138253cc65a61276c2b4
Author: c8ef <c8ef@outlook.com>
Date:   2024-08-16 15:28:46 +0800

    [sqlite3] update to 3.46.1 (#40435)

 ports/sqlite3/portfile.cmake | 2 +-
 ports/sqlite3/vcpkg.json     | 3 +--
 versions/baseline.json       | 4 ++--
 versions/s-/sqlite3.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:18:47,166 - 147 - INFO - run: git add .
2024-09-22 13:18:47,187 - 147 - INFO - run: git commit -m [sqlite3] update to 3.46.1 (#40435) --author c8ef <c8ef@outlook.com>
[main feb1b69b4] [sqlite3] update to 3.46.1 (#40435)
 Author: c8ef <c8ef@outlook.com>
 10 files changed, 732 insertions(+)
 create mode 100644 ports/sqlite3/CMakeLists.txt
 create mode 100644 ports/sqlite3/add-config-include.patch
 create mode 100644 ports/sqlite3/fix-arm-uwp.patch
 create mode 100644 ports/sqlite3/portfile.cmake
 create mode 100644 ports/sqlite3/sqlite3-config.in.cmake
 create mode 100644 ports/sqlite3/sqlite3-vcpkg-config.h.in
 create mode 100644 ports/sqlite3/sqlite3.pc.in
 create mode 100644 ports/sqlite3/usage
 create mode 100644 ports/sqlite3/vcpkg.json
 create mode 100644 versions/s-/sqlite3.json
2024-09-22 13:18:47,251 - 360 - WARNING - copy downloads/vcpkg/ports/boost-stacktrace -> ./ports/boost-stacktrace
2024-09-22 13:18:47,253 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-stacktrace.json -> ./versions/b-/boost-stacktrace.json
2024-09-22 13:18:47,253 - 382 - INFO - boost-stacktrace
commit abe69d7c9f1d44e630aafecbf407362a15995db9
Author: moritz-h <7849248+moritz-h@users.noreply.github.com>
Date:   2024-08-21 08:15:36 +0200

    [boost-stacktrace] add libbacktrace (#40079)

    Co-authored-by: Monica <liuyumei01@beyondsoft.com>

 ports/boost-stacktrace/features.cmake | 20 +++++++-------------
 ports/boost-stacktrace/vcpkg.json     | 30 ++++++++++++++++++++++++++++--
 scripts/boost/generate-ports.ps1      | 16 +++++++++++++++-
 versions/b-/boost-stacktrace.json     |  5 +++++
 versions/baseline.json                |  2 +-
 5 files changed, 56 insertions(+), 17 deletions(-)

2024-09-22 13:18:47,254 - 147 - INFO - run: git add .
2024-09-22 13:18:47,276 - 147 - INFO - run: git commit -m [boost-stacktrace] add libbacktrace (#40079) --author moritz-h <7849248+moritz-h@users.noreply.github.com>
[main d0d68523e] [boost-stacktrace] add libbacktrace (#40079)
 Author: moritz-h <7849248+moritz-h@users.noreply.github.com>
 5 files changed, 300 insertions(+)
 create mode 100644 ports/boost-stacktrace/features.cmake
 create mode 100644 ports/boost-stacktrace/fix_config-check.diff
 create mode 100644 ports/boost-stacktrace/portfile.cmake
 create mode 100644 ports/boost-stacktrace/vcpkg.json
 create mode 100644 versions/b-/boost-stacktrace.json
2024-09-22 13:18:47,336 - 360 - WARNING - copy downloads/vcpkg/ports/boost-cmake -> ./ports/boost-cmake
2024-09-22 13:18:47,341 - 369 - WARNING - copy downloads/vcpkg/versions/b-/boost-cmake.json -> ./versions/b-/boost-cmake.json
2024-09-22 13:18:47,342 - 382 - INFO - boost-cmake
commit 0f0b1221077b7b8d119c07e9e500e138ee05541c
Author: WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
Date:   2024-09-05 13:33:36 +0800

    [boost-cmake] Backport MSVC 19.40 is still vc143 (#40778)

 ports/boost-cmake/portfile.cmake |  7 +++++
 ports/boost-cmake/vcpkg.json     |  2 +-
 scripts/boost/generate-ports.ps1 | 63 ++++++++++++++++++++++++++++++----------
 versions/b-/boost-cmake.json     |  5 ++++
 versions/baseline.json           |  2 +-
 5 files changed, 62 insertions(+), 17 deletions(-)

2024-09-22 13:18:47,342 - 147 - INFO - run: git add .
2024-09-22 13:18:47,364 - 147 - INFO - run: git commit -m [boost-cmake] Backport MSVC 19.40 is still vc143 (#40778) --author WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
[main 10247b152] [boost-cmake] Backport MSVC 19.40 is still vc143 (#40778)
 Author: WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
 13 files changed, 350 insertions(+)
 create mode 100644 ports/boost-cmake/CMakeLists.txt.in
 create mode 100644 ports/boost-cmake/add-optional-deps.diff
 create mode 100644 ports/boost-cmake/fix-missing-archs.diff
 create mode 100644 ports/boost-cmake/fix-mpi.diff
 create mode 100644 ports/boost-cmake/no-prefix.diff
 create mode 100644 ports/boost-cmake/portfile.cmake
 create mode 100644 ports/boost-cmake/ref_sha.cmake
 create mode 100644 ports/boost-cmake/usage
 create mode 100644 ports/boost-cmake/vcpkg-build.diff
 create mode 100644 ports/boost-cmake/vcpkg-port-config.cmake
 create mode 100644 ports/boost-cmake/vcpkg.json
 create mode 100644 ports/boost-cmake/zstd.diff
 create mode 100644 versions/b-/boost-cmake.json
2024-09-22 13:18:47,428 - 360 - WARNING - copy downloads/vcpkg/ports/expat -> ./ports/expat
2024-09-22 13:18:47,430 - 369 - WARNING - copy downloads/vcpkg/versions/e-/expat.json -> ./versions/e-/expat.json
2024-09-22 13:18:47,431 - 382 - INFO - expat
commit 120b4767ae9f4156b94ebac0e0d91cf4b0e81d3b
Author: aristotelos <arisvd@gmail.com>
Date:   2024-09-10 05:24:40 +0200

    [expat] Update to 2.6.3 (#40836)

 ports/expat/portfile.cmake | 2 +-
 ports/expat/vcpkg.json     | 3 +--
 versions/baseline.json     | 4 ++--
 versions/e-/expat.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:18:47,431 - 147 - INFO - run: git add .
2024-09-22 13:18:47,454 - 147 - INFO - run: git commit -m [expat] Update to 2.6.3 (#40836) --author aristotelos <arisvd@gmail.com>
[main a3b33ad09] [expat] Update to 2.6.3 (#40836)
 Author: aristotelos <arisvd@gmail.com>
 4 files changed, 211 insertions(+)
 create mode 100644 ports/expat/portfile.cmake
 create mode 100644 ports/expat/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/expat/vcpkg.json
 create mode 100644 versions/e-/expat.json
PS D:\sources\MediaPorts\vcpkg-media-registry> python pick_port.py --pick-port=ffmpeg
2024-09-22 13:20:12,063 - 91 - INFO - parse_cli_args
2024-09-22 13:20:12,064 - 396 - INFO - CliArgs(msft_vcpkg_root_dir='downloads/vcpkg', msft_vcpkg_url='https://github.com/microsoft/vcpkg.git', msft_vcpkg_branch='master', msft_vcpkg_baseline='98aa6396292d57e737a6ef999d4225ca488859d5', my_vcpkg_branch='main', pick_port='ffmpeg')
2024-09-22 13:20:12,064 - 287 - INFO - update_msft
2024-09-22 13:20:12,065 - 147 - INFO - run: git fetch
2024-09-22 13:20:12,820 - 147 - INFO - run: git rev-parse --abbrev-ref HEAD
2024-09-22 13:20:12,837 - 147 - INFO - run: git reset --hard 98aa6396292d57e737a6ef999d4225ca488859d5
HEAD is now at 98aa63962 [fast-double-parser] update to 0.8.0 (#40975)
2024-09-22 13:20:12,941 - 196 - WARNING - ffmpeg has 137 necessary ports: ["abseil", "alsa", "amd-amf", "aom", "avisynthplus", "brotli", "bzip2", "c-ares", "cairo", "cpu-features", "curl", "dav1d", "dbus", "dirent", "egl-registry", "expat", "fastcgi", "fdk-aac", "ffmpeg", "ffnvcodec", "fontconfig", "freeglut", "freetype", "fribidi", "getopt", "getopt-win32", "gettext", "gettext-libintl", "gettimeofday", "giflib", "glib", "gmp", "gobject-introspection", "gperf", "graphite2", "gsasl", "harfbuzz", "icu", "krb5", "lcms", "leptonica", "lerc", "libarchive", "libass", "libcap", "libdeflate", "libffi", "libgcrypt", "libgnutls", "libgpg-error", "libiconv", "libidn2", "libilbc", "libjpeg-turbo", "liblzma", "libmodplug", "libmount", "libogg", "libopenmpt", "libpng", "libpsl", "libsamplerate", "libsrt", "libssh", "libssh2", "libsystemd", "libtasn1", "libtheora", "libunistring", "libuuid", "libvorbis", "libvpx", "libwebp", "libx11", "libxau", "libxcrypt", "libxdmcp", "libxml2", "libxslt", "lz4", "lzo", "mbedtls", "mfx-dispatch", "mp3lame", "mpg123", "ncurses", "nettle", "nghttp2", "opencl", "opengl", "opengl-registry", "openh264", "openjpeg", "openldap", "openssl", "opus", "pango", "pcre2", "pixman", "pkgconf", "pthread", "pthread-stubs", "pthreads", "python3", "sdl1", "sdl2", "shiftmedia-libgnutls", "snappy", "soxr", "speex", "sqlite3", "tensorflow", "tensorflow-common", "tesseract", "tiff", "vcpkg-cmake", "vcpkg-cmake-config", "vcpkg-cmake-get-vars", "vcpkg-get-python", "vcpkg-msbuild", "vcpkg-pkgconfig-get-modules", "vcpkg-tool-bazel", "vcpkg-tool-meson", "vs-yasm", "wolfssl", "x264", "x265", "xcb", "xcb-proto", "xcb-util-m4", "xorg-macros", "xproto", "xtrans", "yasm", "yasm-tool-helper", "zlib", "zstd"]
2024-09-22 13:22:29,150 - 147 - INFO - run: git checkout main
Already on 'main'
Your branch is ahead of 'origin/main' by 36 commits.
  (use "git push" to publish your local commits)
2024-09-22 13:22:29,209 - 360 - WARNING - copy downloads/vcpkg/ports/gmp -> ./ports/gmp
2024-09-22 13:22:29,212 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gmp.json -> ./versions/g-/gmp.json
2024-09-22 13:22:29,213 - 382 - INFO - gmp
commit b7a1088ae9bfed114dd36e0d60ddb3db3b7a4b7f
Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
Date:   2022-02-25 02:50:02 +0800

    [yasm/yasm-tool] Incorporate yasm-tool into yasm (#23218)

    * [yasm/yasm-tool] Incorporate yasm-tool into yasm

    * version

    * Fix merge issue

    * version

    * Add missing dependency feature

    * version

    * Apply suggestions

    * version

 ports/gmp/vcpkg.json                               |  7 +++-
 ports/yasm-tool-helper/vcpkg.json                  | 12 ++++--
 ports/yasm-tool-helper/yasm-tool-helper.cmake.in   |  2 +-
 ports/yasm-tool/portfile.cmake                     | 46 +---------------------
 ports/yasm-tool/vcpkg.json                         | 15 ++++---
 ports/yasm/portfile.cmake                          |  4 +-
 .../{yasm-tool => yasm}/vcpkg-port-config.cmake.in |  6 +--
 ports/yasm/vcpkg.json                              |  4 +-
 versions/baseline.json                             | 10 ++---
 versions/g-/gmp.json                               |  5 +++
 versions/y-/yasm-tool-helper.json                  |  5 +++
 versions/y-/yasm-tool.json                         |  5 +++
 versions/y-/yasm.json                              |  5 +++
 13 files changed, 56 insertions(+), 70 deletions(-)

2024-09-22 13:22:29,213 - 147 - INFO - run: git add .
2024-09-22 13:22:29,234 - 147 - INFO - run: git commit -m [yasm/yasm-tool] Incorporate yasm-tool into yasm (#23218) --author Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
[main 938824c2e] [yasm/yasm-tool] Incorporate yasm-tool into yasm (#23218)
 Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
 9 files changed, 565 insertions(+)
 create mode 100644 ports/gmp/arm64-coff.patch
 create mode 100644 ports/gmp/asmflags.patch
 create mode 100644 ports/gmp/cross-tools.patch
 create mode 100644 ports/gmp/msvc_symbol.patch
 create mode 100644 ports/gmp/portfile.cmake
 create mode 100644 ports/gmp/subdirs.patch
 create mode 100644 ports/gmp/usage
 create mode 100644 ports/gmp/vcpkg.json
 create mode 100644 versions/g-/gmp.json
2024-09-22 13:22:29,301 - 360 - WARNING - copy downloads/vcpkg/ports/libilbc -> ./ports/libilbc
2024-09-22 13:22:29,305 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libilbc.json -> ./versions/l-/libilbc.json
2024-09-22 13:22:29,305 - 382 - INFO - libilbc
commit 5afd32266c257e8cdd8e1c272bdf8964e37dd501
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2022-04-14 20:08:23 +0200

    [qtinterfaceframework|opencv] fix python stuff (#24041)

    * add upstream patch

    * [skip actions] add the patch file

    * fine tune

    * [opencv] update portfiles to use vcpkg-get-python-packages

    * fix references

    * try another fix

    * add all deps

    * add code from tensorflow about venv

    * retry

    * fix file path

    * new approach

    * unset pythonhome

    * next unset

    * try this instead.

    * retry without the PYTHON_LIB_PATH stuff

    * try and error

    * next try

    * retry

    * typo fix

    * try updating

    * retry

    * more try and error

    * reorder

    * drop qface version

    * use qface 2.0.5

    * bump watchdog

    * fix call on !windows

    * fine tuning

    * refactor function signature

    * update version

    * fix formating

    * version stuff

    * create dir before usage

    * fine tuning

    * version stuff

    * update and patch libilbc

    * formating stuff

    * fix version-string

    * version stuff

    * add license

    * version update

    * bump version

    * version stuff

    * version stuff

    Co-authored-by: Alexander Neumann <you@example.com>
    Co-authored-by: Stefano Sinigardi <stesinigardi@hotmail.com>

 ports/libilbc/absl.patch                           |  39 ++++++
 ports/libilbc/portfile.cmake                       |  30 ++---
 ports/libilbc/vcpkg.json                           |  13 +-
 ports/mesa/portfile.cmake                          |   8 +-
 ports/mesa/vcpkg.json                              |   2 +-
 ports/opencv2/portfile.cmake                       |  48 +------
 ports/opencv2/vcpkg.json                           |   8 +-
 ports/opencv3/portfile.cmake                       |  48 +------
 ports/opencv3/vcpkg.json                           |   8 +-
 ports/opencv4/portfile.cmake                       |  46 +------
 ports/opencv4/vcpkg.json                           |   6 +-
 ports/qtinterfaceframework/49b44d4.diff            | 148 +++++++++++++++++++++
 ports/qtinterfaceframework/portfile.cmake          |  66 ++-------
 .../qtinterfaceframework/requirements_minimal.txt  |  14 ++
 ports/qtinterfaceframework/vcpkg.json              |   8 +-
 ports/vcpkg-get-python-packages/portfile.cmake     |   3 +
 ports/vcpkg-get-python-packages/python310._pth     |   7 +
 ports/vcpkg-get-python-packages/vcpkg.json         |   2 +-
 .../x_vcpkg_get_python_packages.cmake              | 114 ++++++++++++----
 scripts/ci.baseline.txt                            |   3 -
 versions/baseline.json                             |  16 +--
 versions/l-/libilbc.json                           |   5 +
 versions/m-/mesa.json                              |   5 +
 versions/o-/opencv2.json                           |   5 +
 versions/o-/opencv3.json                           |   5 +
 versions/o-/opencv4.json                           |   5 +
 versions/q-/qtinterfaceframework.json              |   5 +
 versions/v-/vcpkg-get-python-packages.json         |   5 +
 28 files changed, 407 insertions(+), 265 deletions(-)

2024-09-22 13:22:29,306 - 147 - INFO - run: git add .
2024-09-22 13:22:29,327 - 147 - INFO - run: git commit -m [qtinterfaceframework|opencv] fix python stuff (#24041) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main b80fb3c4c] [qtinterfaceframework|opencv] fix python stuff (#24041)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 5 files changed, 115 insertions(+)
 create mode 100644 ports/libilbc/absl.patch
 create mode 100644 ports/libilbc/do-not-build-ilbc_test.patch
 create mode 100644 ports/libilbc/portfile.cmake
 create mode 100644 ports/libilbc/vcpkg.json
 create mode 100644 versions/l-/libilbc.json
2024-09-22 13:22:29,389 - 360 - WARNING - copy downloads/vcpkg/ports/fastcgi -> ./ports/fastcgi
2024-09-22 13:22:29,390 - 369 - WARNING - copy downloads/vcpkg/versions/f-/fastcgi.json -> ./versions/f-/fastcgi.json
2024-09-22 13:22:29,391 - 382 - INFO - fastcgi
commit 8da5d2b4503b3100b6b7bb26ffeeefd0e8a25799
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2022-05-19 23:43:34 +0200

    [OpenJPEG] Update to 2.5.0 (#24734)

    * update openjpeg

    * update openjpeg

    * add arm patch and license

    * reduce to version

    * update db

    * fix fastcgi to always use make

    * remove from baseline

    * openjpeg add tools feature

    * vdb

    * add supports statement. fastcgi uses stuff which only is allowed in desktop apps.

    * format manfiest

    * ver db

    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/fastcgi/dll.patch                            | 109 +++++++++++++++++++++
 ports/fastcgi/portfile.cmake                       |  84 ++++++----------
 ports/fastcgi/vcpkg.json                           |   5 +-
 ports/openjpeg/Enable-tools-of-each-features.patch |  13 ---
 ports/openjpeg/arm.patch                           |  13 +++
 ports/openjpeg/dll.location.patch                  |  32 ------
 ports/openjpeg/fix-lrintf-to-opj_lrintf.patch      |  13 ---
 ports/openjpeg/fix-static.patch                    |  59 +++++++++++
 ports/openjpeg/no-wx.patch                         |  10 ++
 ports/openjpeg/portfile.cmake                      |  37 ++++---
 ports/openjpeg/vcpkg.json                          |  25 ++++-
 scripts/ci.baseline.txt                            |   1 -
 versions/baseline.json                             |   4 +-
 versions/f-/fastcgi.json                           |   5 +
 versions/o-/openjpeg.json                          |   5 +
 15 files changed, 274 insertions(+), 141 deletions(-)

2024-09-22 13:22:29,391 - 147 - INFO - run: git add .
2024-09-22 13:22:29,413 - 147 - INFO - run: git commit -m [OpenJPEG] Update to 2.5.0 (#24734) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main 661a5b986] [OpenJPEG] Update to 2.5.0 (#24734)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 4 files changed, 199 insertions(+)
 create mode 100644 ports/fastcgi/dll.patch
 create mode 100644 ports/fastcgi/portfile.cmake
 create mode 100644 ports/fastcgi/vcpkg.json
 create mode 100644 versions/f-/fastcgi.json
2024-09-22 13:22:29,473 - 360 - WARNING - copy downloads/vcpkg/ports/yasm -> ./ports/yasm
2024-09-22 13:22:29,475 - 369 - WARNING - copy downloads/vcpkg/versions/y-/yasm.json -> ./versions/y-/yasm.json
2024-09-22 13:22:29,476 - 382 - INFO - yasm
commit 7f49d67ef8e43bf95c3a14403126c5aaa9e054b3
Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
Date:   2022-07-11 23:24:23 +0000

    [vcpkg baseline][yasm/vcpkg-tool-ninja] Fix build (#25678)

    * [yasm/vcpkg-tool-ninja] Fix build

    * version

 ports/vcpkg-tool-ninja/portfile.cmake          |  4 +++-
 ports/vcpkg-tool-ninja/use-internal-re2c.patch | 13 +++++++++++++
 ports/vcpkg-tool-ninja/vcpkg.json              |  1 +
 ports/yasm/portfile.cmake                      |  1 +
 ports/yasm/vcpkg.json                          |  2 +-
 versions/baseline.json                         |  4 ++--
 versions/v-/vcpkg-tool-ninja.json              |  5 +++++
 versions/y-/yasm.json                          |  5 +++++
 8 files changed, 31 insertions(+), 4 deletions(-)

2024-09-22 13:22:29,476 - 147 - INFO - run: git add .
2024-09-22 13:22:29,497 - 147 - INFO - run: git commit -m [vcpkg baseline][yasm/vcpkg-tool-ninja] Fix build (#25678) --author Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
[main e1d4a1228] [vcpkg baseline][yasm/vcpkg-tool-ninja] Fix build (#25678)
 Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
 6 files changed, 263 insertions(+)
 create mode 100644 ports/yasm/add-feature-tools.patch
 create mode 100644 ports/yasm/fix-arm-cross-build.patch
 create mode 100644 ports/yasm/portfile.cmake
 create mode 100644 ports/yasm/vcpkg-port-config.cmake.in
 create mode 100644 ports/yasm/vcpkg.json
 create mode 100644 versions/y-/yasm.json
2024-09-22 13:22:29,563 - 360 - WARNING - copy downloads/vcpkg/ports/dbus -> ./ports/dbus
2024-09-22 13:22:29,564 - 369 - WARNING - copy downloads/vcpkg/versions/d-/dbus.json -> ./versions/d-/dbus.json
2024-09-22 13:22:29,566 - 382 - INFO - dbus
commit 552f1ee5f83e370b9df9dc677181c2dd765b22ba
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2022-08-22 21:26:13 +0200

    [Part1|xwindow PR] Split up to dbus (#22642)

    * first batch of xwindow PR ports - up to dbus

    * first batch of xwindow PR ports - up to dbus

    * format manifest

    * version stuff

    * remove if block

    * version stuff

    * fix xcb hash

    * fix xproto dependency on meson blocking cross builds

    * adjust message

    * use X11_xcb_LIB

    * version stuff

    * put xlib arm64-windows on baseline

    * fix dbus on osx and linux

    * version stuff

    * forget to set the value

    * fix --export-dynamic on osx

    * version dbus

    * ci-retrigger

    * add license (needs tool update)

    * version adjustments

    * version update

    * remove unnecessary comments

    * v db

    * Apply suggestions from code review

    Co-authored-by: Billy O'Neal <bion@microsoft.com>

    * nitpicks

    * rename xau to libxau

    * use vcpkg_install_copyright and silence usage

    * xtrans silence usage

    * format-manifest

    * v db

    * make license null for ports without exact match

    * xdmcp rename to libxdmcp

    * merge x11 wrapper into xlib
    rename xlib to libx11 to avoid a metaport

    * v db

    * missed dbus depending on x11.

    * v db

    * Update scripts/ci.baseline.txt

    Co-authored-by: LilyWangLL <94091114+LilyWangLL@users.noreply.github.com>
    Co-authored-by: Alexander Neumann <you@example.com>
    Co-authored-by: JackBoosY <yuzaiyang@beyondsoft.com>
    Co-authored-by: Billy O'Neal <bion@microsoft.com>

 ports/dbus/cmake.dep.patch                |  15 +++
 ports/dbus/getpeereid.patch               |  26 ++++++
 ports/dbus/pkgconfig.patch                |  17 ++++
 ports/dbus/portfile.cmake                 |  64 +++++++++++++
 ports/dbus/rdynamic.patch                 |  15 +++
 ports/dbus/rt_pc_link.patch               |  27 ++++++
 ports/dbus/vcpkg.json                     |  20 ++++
 ports/libx11/cl.build.patch               | 147 ++++++++++++++++++++++++++++++
 ports/libx11/dllimport.patch              |  44 +++++++++
 ports/libx11/io_include.patch             |  12 +++
 ports/libx11/portfile.cmake               |  80 ++++++++++++++++
 ports/libx11/vcpkg-cmake-wrapper.cmake    |  12 +++
 ports/libx11/vcpkg.json                   |  17 ++++
 ports/libx11/vcxserver.patch              | 138 ++++++++++++++++++++++++++++
 ports/libxau/portfile.cmake               |  31 +++++++
 ports/libxau/vcpkg.json                   |  12 +++
 ports/libxdmcp/configure.ac.patch         |  13 +++
 ports/libxdmcp/portfile.cmake             |  36 ++++++++
 ports/libxdmcp/vcpkg.json                 |  12 +++
 ports/pthread-stubs/portfile.cmake        |  51 +++++++++++
 ports/pthread-stubs/vcpkg.json            |  10 ++
 ports/xcb-proto/portfile.cmake            |  49 ++++++++++
 ports/xcb-proto/vcpkg.json                |  18 ++++
 ports/xcb-util-m4/portfile.cmake          |  15 +++
 ports/xcb-util-m4/vcpkg.json              |   7 ++
 ports/xcb/configure.patch                 |  47 ++++++++++
 ports/xcb/getpid_include.patch            |  14 +++
 ports/xcb/makefile.patch                  |  13 +++
 ports/xcb/portfile.cmake                  | 107 ++++++++++++++++++++++
 ports/xcb/use_xwindows_includes.patch     |  21 +++++
 ports/xcb/vcpkg.json                      |  22 +++++
 ports/xorg-macros/portfile.cmake          |  67 ++++++++++++++
 ports/xorg-macros/skip_rawcpp.patch       |  43 +++++++++
 ports/xorg-macros/vcpkg.json              |   8 ++
 ports/xproto/portfile.cmake               |  51 +++++++++++
 ports/xproto/upstream-1.patch             |  12 +++
 ports/xproto/vcpkg.json                   |  15 +++
 ports/xproto/vcxserver-xw32defs.patch     |  22 +++++
 ports/xproto/windows-include-guards.patch |  41 +++++++++
 ports/xproto/windows-io.patch             |  12 +++
 ports/xproto/windows-long64.patch         |  48 ++++++++++
 ports/xproto/windows-none.patch           |  85 +++++++++++++++++
 ports/xproto/windows_mean_and_lean.patch  |  13 +++
 ports/xtrans/portfile.cmake               |  64 +++++++++++++
 ports/xtrans/symbols.patch                |  15 +++
 ports/xtrans/vcpkg.json                   |  10 ++
 ports/xtrans/win32.patch                  |  58 ++++++++++++
 scripts/ci.baseline.txt                   |   2 +
 versions/baseline.json                    |  44 +++++++++
 versions/d-/dbus.json                     |   9 ++
 versions/l-/libx11.json                   |   9 ++
 versions/l-/libxau.json                   |   9 ++
 versions/l-/libxdmcp.json                 |   9 ++
 versions/p-/pthread-stubs.json            |   9 ++
 versions/x-/xcb-proto.json                |   9 ++
 versions/x-/xcb-util-m4.json              |   9 ++
 versions/x-/xcb.json                      |   9 ++
 versions/x-/xorg-macros.json              |   9 ++
 versions/x-/xproto.json                   |   9 ++
 versions/x-/xtrans.json                   |   9 ++
 60 files changed, 1821 insertions(+)

2024-09-22 13:22:29,567 - 147 - INFO - run: git add .
2024-09-22 13:22:29,589 - 147 - INFO - run: git commit -m [Part1|xwindow PR] Split up to dbus (#22642) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main 3bf25f919] [Part1|xwindow PR] Split up to dbus (#22642)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 7 files changed, 271 insertions(+)
 create mode 100644 ports/dbus/cmake.dep.patch
 create mode 100644 ports/dbus/getpeereid.patch
 create mode 100644 ports/dbus/libsystemd.patch
 create mode 100644 ports/dbus/pkgconfig.patch
 create mode 100644 ports/dbus/portfile.cmake
 create mode 100644 ports/dbus/vcpkg.json
 create mode 100644 versions/d-/dbus.json
2024-09-22 13:22:29,650 - 360 - WARNING - copy downloads/vcpkg/ports/speex -> ./ports/speex
2024-09-22 13:22:29,651 - 369 - WARNING - copy downloads/vcpkg/versions/s-/speex.json -> ./versions/s-/speex.json
2024-09-22 13:22:29,652 - 382 - INFO - speex
commit 8e3595fad04f60f55250ff0e2f2d4e7e7a580a50
Author: Kai Pastor <dg0yt@darc.de>
Date:   2022-09-09 21:08:05 +0200

    [speex] Use native autotools for all triplets (#26502)

    * Use autotools build for windows

    * Fix license

    * Limit subdirs for vpckg build

    * Update versions

    * CI [skip actions]

 ...001-make-pkg-config-lib-name-configurable.patch |  13 ---
 ports/speex/CMakeLists.txt                         | 111 ---------------------
 ports/speex/fix-vla-check.patch                    |  13 +++
 ports/speex/portfile.cmake                         |  56 ++++-------
 ports/speex/subdirs.patch                          |  13 +++
 ports/speex/vcpkg.json                             |  10 +-
 versions/baseline.json                             |   2 +-
 versions/s-/speex.json                             |   5 +
 8 files changed, 53 insertions(+), 170 deletions(-)

2024-09-22 13:22:29,652 - 147 - INFO - run: git add .
2024-09-22 13:22:29,673 - 147 - INFO - run: git commit -m [speex] Use native autotools for all triplets (#26502) --author Kai Pastor <dg0yt@darc.de>
[main 9f55b10dd] [speex] Use native autotools for all triplets (#26502)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 147 insertions(+)
 create mode 100644 ports/speex/fix-vla-check.patch
 create mode 100644 ports/speex/portfile.cmake
 create mode 100644 ports/speex/subdirs.patch
 create mode 100644 ports/speex/vcpkg.json
 create mode 100644 versions/s-/speex.json
2024-09-22 13:22:29,737 - 360 - WARNING - copy downloads/vcpkg/ports/tensorflow-common -> ./ports/tensorflow-common
2024-09-22 13:22:29,743 - 369 - WARNING - copy downloads/vcpkg/versions/t-/tensorflow-common.json -> ./versions/t-/tensorflow-common.json
2024-09-22 13:22:29,743 - 382 - INFO - tensorflow-common
commit a251c002471d8931eecc12201f84aa8e8e01dbbb
Author: 7FrogTW <jjyyg1123@gmail.com>
Date:   2022-10-22 01:32:45 +0800

    chore: upgrade tensorflow-cc portfile (#24861) (#24861)

    Co-authored-by: Jonliu1993 <13720414433@163.com>

 ports/tensorflow-cc/vcpkg.json                     | 12 ++--
 ports/tensorflow-common/fix-build-error.patch      |  2 +-
 .../generate_static_link_cmd_linux.py              |  2 +-
 ports/tensorflow-common/tensorflow-common.cmake    | 54 ++++++++++++++----
 ports/tensorflow-common/vcpkg.json                 |  6 +-
 ports/tensorflow/vcpkg.json                        | 12 ++--
 ports/vcpkg-tool-bazel/portfile.cmake              | 64 ++++++++++++++++++++++
 ports/vcpkg-tool-bazel/vcpkg.json                  |  8 +++
 versions/baseline.json                             | 16 ++++--
 versions/t-/tensorflow-cc.json                     |  5 ++
 versions/t-/tensorflow-common.json                 |  5 ++
 versions/t-/tensorflow.json                        |  5 ++
 versions/v-/vcpkg-tool-bazel.json                  |  9 +++
 13 files changed, 170 insertions(+), 30 deletions(-)

2024-09-22 13:22:29,743 - 147 - INFO - run: git add .
2024-09-22 13:22:29,766 - 147 - INFO - run: git commit -m chore: upgrade tensorflow-cc portfile (#24861) (#24861) --author 7FrogTW <jjyyg1123@gmail.com>
[main 2e8eae0bc] chore: upgrade tensorflow-cc portfile (#24861) (#24861)
 Author: 7FrogTW <jjyyg1123@gmail.com>
 21 files changed, 1470 insertions(+)
 create mode 100644 ports/tensorflow-common/LICENSE.txt
 create mode 100644 ports/tensorflow-common/README-linux
 create mode 100644 ports/tensorflow-common/README-macos
 create mode 100644 ports/tensorflow-common/README-windows
 create mode 100644 ports/tensorflow-common/change-macros-for-static-lib.patch
 create mode 100644 ports/tensorflow-common/convert_lib_params_linux.py
 create mode 100644 ports/tensorflow-common/convert_lib_params_macos.py
 create mode 100644 ports/tensorflow-common/convert_lib_params_windows.py
 create mode 100644 ports/tensorflow-common/fix-build-error.patch
 create mode 100644 ports/tensorflow-common/fix-windows-build.patch
 create mode 100644 ports/tensorflow-common/generate_static_link_cmd_linux.py
 create mode 100644 ports/tensorflow-common/generate_static_link_cmd_macos.py
 create mode 100644 ports/tensorflow-common/generate_static_link_cmd_windows.py
 create mode 100644 ports/tensorflow-common/portfile.cmake
 create mode 100644 ports/tensorflow-common/tensorflow-common.cmake
 create mode 100644 ports/tensorflow-common/tensorflow-config-shared.cmake.in
 create mode 100644 ports/tensorflow-common/tensorflow-config-static.cmake.in
 create mode 100644 ports/tensorflow-common/tensorflow-config-windows-dll.cmake.in
 create mode 100644 ports/tensorflow-common/tensorflow-config-windows-lib.cmake.in
 create mode 100644 ports/tensorflow-common/vcpkg.json
 create mode 100644 versions/t-/tensorflow-common.json
2024-09-22 13:22:29,826 - 360 - WARNING - copy downloads/vcpkg/ports/pthread-stubs -> ./ports/pthread-stubs
2024-09-22 13:22:29,828 - 369 - WARNING - copy downloads/vcpkg/versions/p-/pthread-stubs.json -> ./versions/p-/pthread-stubs.json
2024-09-22 13:22:29,829 - 382 - INFO - pthread-stubs
commit 3e3484ad700cbfce1c8661c7cea7f9e6c09f76cd
Author: Matthias Kuhn <matthias@opengis.ch>
Date:   2022-11-02 04:00:18 +0100

    [pthread-stubs] allow building release only (#27530)

    * [pthread-stubs] allow building release only

    * Address review comment

 ports/pthread-stubs/portfile.cmake | 32 +++++++++++++++++---------------
 ports/pthread-stubs/vcpkg.json     |  1 +
 versions/baseline.json             |  2 +-
 versions/p-/pthread-stubs.json     |  5 +++++
 4 files changed, 24 insertions(+), 16 deletions(-)

2024-09-22 13:22:29,829 - 147 - INFO - run: git add .
2024-09-22 13:22:29,850 - 147 - INFO - run: git commit -m [pthread-stubs] allow building release only (#27530) --author Matthias Kuhn <matthias@opengis.ch>
[main 1aa6d0259] [pthread-stubs] allow building release only (#27530)
 Author: Matthias Kuhn <matthias@opengis.ch>
 3 files changed, 78 insertions(+)
 create mode 100644 ports/pthread-stubs/portfile.cmake
 create mode 100644 ports/pthread-stubs/vcpkg.json
 create mode 100644 versions/p-/pthread-stubs.json
2024-09-22 13:22:29,911 - 360 - WARNING - copy downloads/vcpkg/ports/lcms -> ./ports/lcms
2024-09-22 13:22:29,913 - 369 - WARNING - copy downloads/vcpkg/versions/l-/lcms.json -> ./versions/l-/lcms.json
2024-09-22 13:22:29,914 - 382 - INFO - lcms
commit e3a3942a9eb0cb47c12898e5fd819f258441b6f6
Author: Nick <quyykk@protonmail.com>
Date:   2022-11-03 23:14:09 +0100

    [libjxl][lcms][highway] update to latest version (#27593)

    * [highway] update to 1.0.2

    * [lcms] update to 2.14

    * [libjxl] update to 0.7.0

 ports/highway/portfile.cmake                      |  15 ++-
 ports/highway/vcpkg.json                          |  10 +-
 ports/lcms/CMakeLists.txt                         |   7 +-
 ports/lcms/fix-shared-library.patch               |  12 +++
 ports/lcms/portfile.cmake                         |  12 ++-
 ports/lcms/{cpp17.patch => remove-register.patch} |   6 +-
 ports/lcms/remove_library_directive.patch         |   8 +-
 ports/lcms/shared.patch                           |  10 --
 ports/lcms/vcpkg.json                             |   4 +-
 ports/libjxl/disable-jxl_extras.patch             |  14 ---
 ports/libjxl/fix-dependencies.patch               | 125 +++++-----------------
 ports/libjxl/fix-install-directories.patch        |  36 -------
 ports/libjxl/fix-link-flags.patch                 |  15 ---
 ports/libjxl/portfile.cmake                       |  38 ++-----
 ports/libjxl/vcpkg.json                           |   4 +-
 versions/baseline.json                            |  10 +-
 versions/h-/highway.json                          |   5 +
 versions/l-/lcms.json                             |   5 +
 versions/l-/libjxl.json                           |   5 +
 19 files changed, 109 insertions(+), 232 deletions(-)

2024-09-22 13:22:29,914 - 147 - INFO - run: git add .
2024-09-22 13:22:29,936 - 147 - INFO - run: git commit -m [libjxl][lcms][highway] update to latest version (#27593) --author Nick <quyykk@protonmail.com>
[main 43e116389] [libjxl][lcms][highway] update to latest version (#27593)
 Author: Nick <quyykk@protonmail.com>
 8 files changed, 226 insertions(+)
 create mode 100644 ports/lcms/CMakeLists.txt
 create mode 100644 ports/lcms/fix-shared-library.patch
 create mode 100644 ports/lcms/portfile.cmake
 create mode 100644 ports/lcms/remove-register.patch
 create mode 100644 ports/lcms/remove_library_directive.patch
 create mode 100644 ports/lcms/usage
 create mode 100644 ports/lcms/vcpkg.json
 create mode 100644 versions/l-/lcms.json
2024-09-22 13:22:29,998 - 360 - WARNING - copy downloads/vcpkg/ports/libogg -> ./ports/libogg
2024-09-22 13:22:29,999 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libogg.json -> ./versions/l-/libogg.json
2024-09-22 13:22:30,000 - 382 - INFO - libogg
commit 38b53e80ebdc62ea418abb488c51bde52d28426e
Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
Date:   2022-12-27 09:53:18 +0100

    [libogg] Disable tests (#28526)

    * [libogg] Disable license

    * [libogg] Disable license

    * version

 ports/libogg/portfile.cmake | 21 +++++++++++----------
 ports/libogg/vcpkg.json     | 14 +++++++++++++-
 versions/baseline.json      |  2 +-
 versions/l-/libogg.json     |  5 +++++
 4 files changed, 30 insertions(+), 12 deletions(-)

2024-09-22 13:22:30,000 - 147 - INFO - run: git add .
2024-09-22 13:22:30,021 - 147 - INFO - run: git commit -m [libogg] Disable tests (#28526) --author Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
[main 5c6004d3a] [libogg] Disable tests (#28526)
 Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
 3 files changed, 123 insertions(+)
 create mode 100644 ports/libogg/portfile.cmake
 create mode 100644 ports/libogg/vcpkg.json
 create mode 100644 versions/l-/libogg.json
2024-09-22 13:22:30,081 - 360 - WARNING - copy downloads/vcpkg/ports/libsamplerate -> ./ports/libsamplerate
2024-09-22 13:22:30,083 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libsamplerate.json -> ./versions/l-/libsamplerate.json
2024-09-22 13:22:30,084 - 382 - INFO - libsamplerate
commit c8fa9ac7439206aa59aec8df75900bec4e5db965
Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
Date:   2022-12-27 10:01:50 +0100

    [libsamplerate] Delete docs (#28551)

    * [libsamplerate] Delete docs

    * version

 ports/libsamplerate/portfile.cmake | 16 ++++++++--------
 ports/libsamplerate/vcpkg.json     | 16 ++++++++++++++--
 versions/baseline.json             |  2 +-
 versions/l-/libsamplerate.json     |  5 +++++
 4 files changed, 28 insertions(+), 11 deletions(-)

2024-09-22 13:22:30,084 - 147 - INFO - run: git add .
2024-09-22 13:22:30,105 - 147 - INFO - run: git commit -m [libsamplerate] Delete docs (#28551) --author Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
[main 345362761] [libsamplerate] Delete docs (#28551)
 Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
 3 files changed, 89 insertions(+)
 create mode 100644 ports/libsamplerate/portfile.cmake
 create mode 100644 ports/libsamplerate/vcpkg.json
 create mode 100644 versions/l-/libsamplerate.json
2024-09-22 13:22:30,167 - 360 - WARNING - copy downloads/vcpkg/ports/libtasn1 -> ./ports/libtasn1
2024-09-22 13:22:30,169 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libtasn1.json -> ./versions/l-/libtasn1.json
2024-09-22 13:22:30,170 - 382 - INFO - libtasn1
commit c74c03819aecba36ae814f41b40fb2489c13f101
Author: Kai Pastor <dg0yt@darc.de>
Date:   2023-03-09 20:49:08 +0100

    [libtasn1] Fix android clang (#30093)

 ports/libtasn1/clang-fortify.patch | 64 ++++++++++++++++++++++++++++++++++++++
 ports/libtasn1/portfile.cmake      |  6 ++--
 ports/libtasn1/vcpkg.json          |  1 +
 versions/baseline.json             |  2 +-
 versions/l-/libtasn1.json          |  5 +++
 5 files changed, 74 insertions(+), 4 deletions(-)

2024-09-22 13:22:30,170 - 147 - INFO - run: git add .
2024-09-22 13:22:30,191 - 147 - INFO - run: git commit -m [libtasn1] Fix android clang (#30093) --author Kai Pastor <dg0yt@darc.de>
[main fde45a9be] [libtasn1] Fix android clang (#30093)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 267 insertions(+)
 create mode 100644 ports/libtasn1/clang-fortify.patch
 create mode 100644 ports/libtasn1/msvc_fixes.patch
 create mode 100644 ports/libtasn1/portfile.cmake
 create mode 100644 ports/libtasn1/vcpkg.json
 create mode 100644 versions/l-/libtasn1.json
2024-09-22 13:22:30,254 - 360 - WARNING - copy downloads/vcpkg/ports/opengl -> ./ports/opengl
2024-09-22 13:22:30,256 - 369 - WARNING - copy downloads/vcpkg/versions/o-/opengl.json -> ./versions/o-/opengl.json
2024-09-22 13:22:30,256 - 382 - INFO - opengl
commit 7a4ca3fd46d591ae62313e2d6a451515cbbfef4e
Author: Chuck Walbourn <walbourn@users.noreply.github.com>
Date:   2023-03-20 12:02:25 -0700

    UWP toolchain fix and update some supports expressions for uwp/xbox (#30096)

    * UWP toolchain fix and update some ports supports expressions for uwp/xbox

    * Update baseline

    * More ports updated for !xbox

    * Update baseline

    * Update support expression for ms-gdkx

    * Update baseline

    * ms-gdkx port should fail on ado system

    * Revert change to opengl-registry since its needed for angle on UWP

    * Minor github actions cr

    * Refresh baseline

 ports/cppxaml/vcpkg.json                     |  4 +++-
 ports/cuda/vcpkg.json                        |  4 ++--
 ports/kinectsdk1/vcpkg.json                  |  4 ++--
 ports/kinectsdk2/vcpkg.json                  |  4 ++--
 ports/ms-gdkx/vcpkg.json                     |  3 ++-
 ports/opengl/vcpkg.json                      |  4 ++--
 ports/vulkan-headers/vcpkg.json              |  4 ++--
 ports/vulkan-hpp/vcpkg.json                  |  4 ++--
 ports/vulkan-memory-allocator-hpp/vcpkg.json |  2 ++
 ports/vulkan-memory-allocator/vcpkg.json     |  4 +++-
 ports/vulkan/vcpkg.json                      |  5 +++--
 scripts/ci.baseline.txt                      |  5 +++++
 scripts/toolchains/uwp.cmake                 |  8 +++-----
 versions/baseline.json                       | 22 +++++++++++-----------
 versions/c-/cppxaml.json                     |  5 +++++
 versions/c-/cuda.json                        |  5 +++++
 versions/k-/kinectsdk1.json                  |  5 +++++
 versions/k-/kinectsdk2.json                  |  5 +++++
 versions/m-/ms-gdkx.json                     |  5 +++++
 versions/o-/opengl.json                      |  5 +++++
 versions/v-/vulkan-headers.json              |  5 +++++
 versions/v-/vulkan-hpp.json                  |  5 +++++
 versions/v-/vulkan-memory-allocator-hpp.json |  5 +++++
 versions/v-/vulkan-memory-allocator.json     |  5 +++++
 versions/v-/vulkan.json                      |  5 +++++
 25 files changed, 99 insertions(+), 33 deletions(-)

2024-09-22 13:22:30,256 - 147 - INFO - run: git add .
2024-09-22 13:22:30,278 - 147 - INFO - run: git commit -m UWP toolchain fix and update some supports expressions for uwp/xbox (#30096) --author Chuck Walbourn <walbourn@users.noreply.github.com>
[main 6a53ded30] UWP toolchain fix and update some supports expressions for uwp/xbox (#30096)
 Author: Chuck Walbourn <walbourn@users.noreply.github.com>
 6 files changed, 204 insertions(+)
 create mode 100644 ports/opengl/glu.pc.in
 create mode 100644 ports/opengl/opengl.pc.in
 create mode 100644 ports/opengl/portfile.cmake
 create mode 100644 ports/opengl/usage
 create mode 100644 ports/opengl/vcpkg.json
 create mode 100644 versions/o-/opengl.json
2024-09-22 13:22:30,397 - 360 - WARNING - copy downloads/vcpkg/ports/gettimeofday -> ./ports/gettimeofday
2024-09-22 13:22:30,400 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gettimeofday.json -> ./versions/g-/gettimeofday.json
2024-09-22 13:22:30,401 - 382 - INFO - gettimeofday
commit 7cfd63db7ff8855ab8e2baebeb80b37f5c0818db
Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
Date:   2023-04-22 05:48:12 +0800

    [many ports]switch to vcpkg-cmake / vcpkg-cmake-config part 2 (#29882)

    Co-authored-by: jyu49 <yu_jack@apple.com>
    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/eathread/portfile.cmake                      |  10 +-
 ports/eathread/vcpkg.json                          |   2 +-
 ports/ecos/portfile.cmake                          |   8 +-
 ports/ecos/vcpkg.json                              |   2 +-
 ports/entityx/portfile.cmake                       |   7 +-
 ports/entityx/vcpkg.json                           |   2 +-
 ports/fastfeat/portfile.cmake                      |  10 +-
 ports/fastfeat/vcpkg.json                          |   2 +-
 ports/fastlz/portfile.cmake                        |   8 +-
 ports/fastlz/vcpkg.json                            |   2 +-
 ports/fdlibm/portfile.cmake                        |   8 +-
 ports/fdlibm/vcpkg.json                            |   2 +-
 ports/flashlight-cpu/portfile.cmake                |   8 +-
 ports/flashlight-cpu/vcpkg.json                    |   2 +-
 ports/flashlight-cuda/portfile.cmake               |   8 +-
 ports/flashlight-cuda/vcpkg.json                   |   2 +-
 ports/fmem/portfile.cmake                          |   6 +-
 ports/fmem/vcpkg.json                              |   2 +-
 ports/foonathan-memory/portfile.cmake              |  56 +++++------
 ports/foonathan-memory/vcpkg.json                  |   2 +-
 ports/fp16/portfile.cmake                          |   6 +-
 ports/fp16/vcpkg.json                              |   2 +-
 ports/freeopcua/portfile.cmake                     |   8 +-
 ports/freeopcua/vcpkg.json                         |   2 +-
 ports/functions-framework-cpp/portfile.cmake       |  12 +--
 ports/functions-framework-cpp/vcpkg.json           |   2 +-
 ports/fxdiv/portfile.cmake                         |   7 +-
 ports/fxdiv/vcpkg.json                             |   2 +-
 ports/g2o/portfile.cmake                           |  12 +--
 ports/g2o/vcpkg.json                               |   2 +-
 ports/gamma/portfile.cmake                         |   6 +-
 ports/gamma/vcpkg.json                             |   2 +-
 ports/gasol/portfile.cmake                         |   5 +-
 ports/gasol/vcpkg.json                             |   2 +-
 ports/genann/portfile.cmake                        |   7 +-
 ports/genann/vcpkg.json                            |   2 +-
 ports/gettimeofday/portfile.cmake                  |   4 +-
 ports/gettimeofday/vcpkg.json                      |   2 +-
 ports/gflags/portfile.cmake                        |   8 +-
 ports/gflags/vcpkg.json                            |   2 +-
 ports/gl2ps/portfile.cmake                         |   6 +-
 ports/gl2ps/vcpkg.json                             |   2 +-
 ports/gli/portfile.cmake                           |  10 +-
 ports/gli/vcpkg.json                               |   2 +-
 ports/globjects/portfile.cmake                     |   8 +-
 ports/globjects/vcpkg.json                         |   2 +-
 ports/gloo/portfile.cmake                          |   5 +-
 ports/gloo/vcpkg.json                              |   2 +-
 ports/glui/portfile.cmake                          |  12 +--
 ports/glui/vcpkg.json                              |   2 +-
 ports/gmime/portfile.cmake                         |  20 ++--
 ports/gmime/vcpkg.json                             |   2 +-
 ports/graphicsmagick/portfile.cmake                |  20 ++--
 ports/graphicsmagick/vcpkg.json                    |   2 +-
 ports/h5py-lzf/portfile.cmake                      |   8 +-
 ports/h5py-lzf/vcpkg.json                          |   2 +-
 ports/hayai/portfile.cmake                         |  30 +++---
 ports/hayai/vcpkg.json                             |   2 +-
 ports/http-parser/portfile.cmake                   |   9 +-
 ports/http-parser/vcpkg.json                       |   2 +-
 ports/hungarian/portfile.cmake                     |  14 +--
 ports/hungarian/vcpkg.json                         |   4 +-
 .../vcpkg-port-config.cmake                        |  31 ++++---
 ports/ignition-modularscripts/vcpkg.json           |  14 ++-
 ports/iniparser/portfile.cmake                     |  12 +--
 ports/iniparser/vcpkg.json                         |   2 +-
 ports/io2d/portfile.cmake                          |  10 +-
 ports/io2d/vcpkg.json                              |   2 +-
 ports/itpp/portfile.cmake                          |  14 +--
 ports/itpp/vcpkg.json                              |   2 +-
 ports/jbig2dec/portfile.cmake                      |   6 +-
 ports/jbig2dec/vcpkg.json                          |   2 +-
 ports/jbigkit/portfile.cmake                       |  12 +--
 ports/jbigkit/vcpkg.json                           |   2 +-
 ports/jinja2cpplight/portfile.cmake                |  12 +--
 ports/jinja2cpplight/vcpkg.json                    |   2 +-
 ports/json-spirit/portfile.cmake                   |  14 ++-
 ports/json-spirit/vcpkg.json                       |   2 +-
 ports/json11/portfile.cmake                        |   9 +-
 ports/json11/vcpkg.json                            |   2 +-
 ports/json5-parser/portfile.cmake                  |   8 +-
 ports/json5-parser/vcpkg.json                      |   2 +-
 ports/kd-soap/portfile.cmake                       |  10 +-
 ports/kd-soap/vcpkg.json                           |   1 +
 ports/kenlm/portfile.cmake                         |   8 +-
 ports/kenlm/vcpkg.json                             |   2 +-
 ports/kuku/portfile.cmake                          |   6 +-
 ports/kuku/vcpkg.json                              |   2 +-
 ports/kvasir-mpl/portfile.cmake                    |   9 +-
 ports/kvasir-mpl/vcpkg.json                        |   2 +-
 ports/lapack/portfile.cmake                        |   4 +-
 ports/lapack/vcpkg.json                            |   2 +-
 ports/levmar/portfile.cmake                        |   6 +-
 ports/levmar/vcpkg.json                            |   2 +-
 ports/libaiff/portfile.cmake                       |   8 +-
 ports/libaiff/vcpkg.json                           |   2 +-
 ports/libcds/portfile.cmake                        |   8 +-
 ports/libcds/vcpkg.json                            |   2 +-
 ports/libconfig/portfile.cmake                     |  12 +--
 ports/libconfig/vcpkg.json                         |   2 +-
 versions/baseline.json                             | 102 ++++++++++-----------
 versions/e-/eathread.json                          |   5 +
 versions/e-/ecos.json                              |   5 +
 versions/e-/entityx.json                           |   5 +
 versions/f-/fastfeat.json                          |   5 +
 versions/f-/fastlz.json                            |   5 +
 versions/f-/fdlibm.json                            |   5 +
 versions/f-/flashlight-cpu.json                    |   5 +
 versions/f-/flashlight-cuda.json                   |   5 +
 versions/f-/fmem.json                              |   5 +
 versions/f-/foonathan-memory.json                  |   5 +
 versions/f-/fp16.json                              |   5 +
 versions/f-/freeopcua.json                         |   5 +
 versions/f-/functions-framework-cpp.json           |   5 +
 versions/f-/fxdiv.json                             |   5 +
 versions/g-/g2o.json                               |   5 +
 versions/g-/gamma.json                             |   5 +
 versions/g-/gasol.json                             |   5 +
 versions/g-/genann.json                            |   5 +
 versions/g-/gettimeofday.json                      |   5 +
 versions/g-/gflags.json                            |   5 +
 versions/g-/gl2ps.json                             |   5 +
 versions/g-/gli.json                               |   5 +
 versions/g-/globjects.json                         |   5 +
 versions/g-/gloo.json                              |   5 +
 versions/g-/glui.json                              |   5 +
 versions/g-/gmime.json                             |   5 +
 versions/g-/graphicsmagick.json                    |   5 +
 versions/h-/h5py-lzf.json                          |   5 +
 versions/h-/hayai.json                             |   5 +
 versions/h-/http-parser.json                       |   5 +
 versions/h-/hungarian.json                         |   5 +
 versions/i-/ignition-modularscripts.json           |   5 +
 versions/i-/iniparser.json                         |   5 +
 versions/i-/io2d.json                              |   5 +
 versions/i-/itpp.json                              |   5 +
 versions/j-/jbig2dec.json                          |   5 +
 versions/j-/jbigkit.json                           |   5 +
 versions/j-/jinja2cpplight.json                    |   5 +
 versions/j-/json-spirit.json                       |   5 +
 versions/j-/json11.json                            |   5 +
 versions/j-/json5-parser.json                      |   5 +
 versions/k-/kd-soap.json                           |   5 +
 versions/k-/kenlm.json                             |   5 +
 versions/k-/kuku.json                              |   5 +
 versions/k-/kvasir-mpl.json                        |   5 +
 versions/l-/lapack.json                            |   5 +
 versions/l-/levmar.json                            |   5 +
 versions/l-/libaiff.json                           |   5 +
 versions/l-/libcds.json                            |   5 +
 versions/l-/libconfig.json                         |   5 +
 151 files changed, 637 insertions(+), 373 deletions(-)

2024-09-22 13:22:30,402 - 147 - INFO - run: git add .
2024-09-22 13:22:30,424 - 147 - INFO - run: git commit -m [many ports]switch to vcpkg-cmake / vcpkg-cmake-config part 2 (#29882) --author Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
[main ea75f72be] [many ports]switch to vcpkg-cmake / vcpkg-cmake-config part 2 (#29882)
 Author: Jack路Boos路Yu <47264268+JackBoosY@users.noreply.github.com>
 8 files changed, 183 insertions(+)
 create mode 100644 ports/gettimeofday/CMakeLists.txt
 create mode 100644 ports/gettimeofday/LICENSE
 create mode 100644 ports/gettimeofday/gettimeofday.c
 create mode 100644 ports/gettimeofday/gettimeofday.def
 create mode 100644 ports/gettimeofday/gettimeofday.h
 create mode 100644 ports/gettimeofday/portfile.cmake
 create mode 100644 ports/gettimeofday/vcpkg.json
 create mode 100644 versions/g-/gettimeofday.json
2024-09-22 13:22:30,487 - 360 - WARNING - copy downloads/vcpkg/ports/pthreads -> ./ports/pthreads
2024-09-22 13:22:30,492 - 369 - WARNING - copy downloads/vcpkg/versions/p-/pthreads.json -> ./versions/p-/pthreads.json
2024-09-22 13:22:30,492 - 382 - INFO - pthreads
commit 13a0b7ba8dd2af538fdf24d860e67c5b951788fb
Author: Benjamin Oldenburg <benjamin.oldenburg@ordis.co.th>
Date:   2023-05-05 00:27:12 +0700

    [pthreads] Fixed whitespaces in path issue (#31179)

    * quotes

    * Updated version

    * move static patch filenames to vcpkg_from_sourceforge()

 ports/pthreads/portfile.cmake           |  5 +++--
 ports/pthreads/vcpkg.json               |  2 +-
 ports/pthreads/whitespace_in_path.patch | 27 +++++++++++++++++++++++++++
 versions/baseline.json                  |  2 +-
 versions/p-/pthreads.json               |  5 +++++
 5 files changed, 37 insertions(+), 4 deletions(-)

2024-09-22 13:22:30,493 - 147 - INFO - run: git add .
2024-09-22 13:22:30,514 - 147 - INFO - run: git commit -m [pthreads] Fixed whitespaces in path issue (#31179) --author Benjamin Oldenburg <benjamin.oldenburg@ordis.co.th>
[main 279faca80] [pthreads] Fixed whitespaces in path issue (#31179)
 Author: Benjamin Oldenburg <benjamin.oldenburg@ordis.co.th>
 16 files changed, 709 insertions(+)
 create mode 100644 ports/pthreads/PThreads4WConfig.cmake
 create mode 100644 ports/pthreads/fix-arm-macro.patch
 create mode 100644 ports/pthreads/fix-arm64-version_rc.patch
 create mode 100644 ports/pthreads/fix-install.patch
 create mode 100644 ports/pthreads/fix-pthread_getname_np.patch
 create mode 100644 ports/pthreads/fix-uwp-linkage.patch
 create mode 100644 ports/pthreads/portfile.cmake
 create mode 100644 ports/pthreads/usage
 create mode 100644 ports/pthreads/use-md.patch
 create mode 100644 ports/pthreads/use-mt.patch
 create mode 100644 ports/pthreads/vcpkg-cmake-wrapper-pthread.cmake
 create mode 100644 ports/pthreads/vcpkg-cmake-wrapper-pthreads-windows.cmake
 create mode 100644 ports/pthreads/vcpkg-cmake-wrapper-pthreads.cmake
 create mode 100644 ports/pthreads/vcpkg.json
 create mode 100644 ports/pthreads/whitespace_in_path.patch
 create mode 100644 versions/p-/pthreads.json
2024-09-22 13:22:30,600 - 360 - WARNING - copy downloads/vcpkg/ports/gperf -> ./ports/gperf
2024-09-22 13:22:30,602 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gperf.json -> ./versions/g-/gperf.json
2024-09-22 13:22:30,603 - 382 - INFO - gperf
commit 56a44f31819bef1955f5d9168410a5fc17b95154
Author: Ridwan Abdul Hafidh <github@rdhafidh.web.id>
Date:   2023-08-07 23:11:58 +0700

    [gperf] Fix error in cpp17 mode (#32980)

    * fix gperf in cpp17 mode

    * update version

    * update version #2

    * remove unused header patch file

    * update version 3

    ---------

    Co-authored-by: rdh <ridwanabdulhafidh@gmail.com>

 ports/gperf/portfile.cmake                      |  2 ++
 ports/gperf/remove_register_keyword_cpp17.patch | 13 +++++++++++++
 ports/gperf/vcpkg.json                          |  2 +-
 versions/baseline.json                          |  2 +-
 versions/g-/gperf.json                          |  5 +++++
 5 files changed, 22 insertions(+), 2 deletions(-)

2024-09-22 13:22:30,603 - 147 - INFO - run: git add .
2024-09-22 13:22:30,625 - 147 - INFO - run: git commit -m [gperf] Fix error in cpp17 mode (#32980) --author Ridwan Abdul Hafidh <github@rdhafidh.web.id>
[main 6a9748af6] [gperf] Fix error in cpp17 mode (#32980)
 Author: Ridwan Abdul Hafidh <github@rdhafidh.web.id>
 6 files changed, 148 insertions(+)
 create mode 100644 ports/gperf/CMakeLists.txt
 create mode 100644 ports/gperf/config.h.in
 create mode 100644 ports/gperf/portfile.cmake
 create mode 100644 ports/gperf/remove_register_keyword_cpp17.patch
 create mode 100644 ports/gperf/vcpkg.json
 create mode 100644 versions/g-/gperf.json
2024-09-22 13:22:30,708 - 360 - WARNING - copy downloads/vcpkg/ports/harfbuzz -> ./ports/harfbuzz
2024-09-22 13:22:30,710 - 369 - WARNING - copy downloads/vcpkg/versions/h-/harfbuzz.json -> ./versions/h-/harfbuzz.json
2024-09-22 13:22:30,710 - 382 - INFO - harfbuzz
commit 500700a90cc07ff507c53bf438356457f3cb5ee2
Author: Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
Date:   2023-09-18 09:52:14 -0700

    [atk/gdk-pixbuf/gtk/gtk3/harfbuzz/pango] Fix dependency gobject-instrospection of feature instrospection (#33792)

    * [atk/gdk-pixbuf/gtk/gtk3/harfbuzz/pango] Fix dependency gobject-instrospection of feature instrospection

    * update version

 ports/atk/portfile.cmake        |  3 ---
 ports/atk/vcpkg.json            | 11 ++---------
 ports/gdk-pixbuf/portfile.cmake |  3 ---
 ports/gdk-pixbuf/vcpkg.json     | 11 ++---------
 ports/gtk/portfile.cmake        |  3 ---
 ports/gtk/vcpkg.json            |  9 +--------
 ports/gtk3/vcpkg.json           |  9 +--------
 ports/harfbuzz/portfile.cmake   |  3 ---
 ports/harfbuzz/vcpkg.json       | 10 ++--------
 ports/pango/portfile.cmake      |  3 ---
 ports/pango/vcpkg.json          | 10 +---------
 versions/a-/atk.json            |  5 +++++
 versions/baseline.json          | 12 ++++++------
 versions/g-/gdk-pixbuf.json     |  5 +++++
 versions/g-/gtk.json            |  5 +++++
 versions/g-/gtk3.json           |  5 +++++
 versions/h-/harfbuzz.json       |  5 +++++
 versions/p-/pango.json          |  5 +++++
 18 files changed, 45 insertions(+), 72 deletions(-)

2024-09-22 13:22:30,711 - 147 - INFO - run: git add .
2024-09-22 13:22:30,734 - 147 - INFO - run: git commit -m [atk/gdk-pixbuf/gtk/gtk3/harfbuzz/pango] Fix dependency gobject-instrospection of feature instrospection (#33792) --author Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
[main dd5e8af27] [atk/gdk-pixbuf/gtk/gtk3/harfbuzz/pango] Fix dependency gobject-instrospection of feature instrospection (#33792)
 Author: Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
 6 files changed, 770 insertions(+)
 create mode 100644 ports/harfbuzz/fix-win32-build.patch
 create mode 100644 ports/harfbuzz/harfbuzzConfig.cmake.in
 create mode 100644 ports/harfbuzz/portfile.cmake
 create mode 100644 ports/harfbuzz/usage
 create mode 100644 ports/harfbuzz/vcpkg.json
 create mode 100644 versions/h-/harfbuzz.json
2024-09-22 13:22:30,796 - 360 - WARNING - copy downloads/vcpkg/ports/cpu-features -> ./ports/cpu-features
2024-09-22 13:22:30,798 - 369 - WARNING - copy downloads/vcpkg/versions/c-/cpu-features.json -> ./versions/c-/cpu-features.json
2024-09-22 13:22:30,799 - 382 - INFO - cpu-features
commit 219c8de64388ade190529a6d7277b5274b561c65
Author: Weihang Ding <798047000@qq.com>
Date:   2023-09-19 00:14:08 +0800

    [cpu-features] Bump to 0.9.0 (#33831)

    * [cpu-features] Bump to 0.9.0

    * Update version database

 ports/cpu-features/fix-windows.patch               | 18 --------
 .../make_list_cpu_features_optional.patch          | 52 ----------------------
 ports/cpu-features/portfile.cmake                  |  7 +--
 ports/cpu-features/vcpkg.json                      |  6 +--
 versions/baseline.json                             |  4 +-
 versions/c-/cpu-features.json                      |  5 +++
 6 files changed, 10 insertions(+), 82 deletions(-)

2024-09-22 13:22:30,799 - 147 - INFO - run: git add .
2024-09-22 13:22:30,822 - 147 - INFO - run: git commit -m [cpu-features] Bump to 0.9.0 (#33831) --author Weihang Ding <798047000@qq.com>
[main fcc7c379b] [cpu-features] Bump to 0.9.0 (#33831)
 Author: Weihang Ding <798047000@qq.com>
 5 files changed, 121 insertions(+)
 create mode 100644 ports/cpu-features/portfile.cmake
 create mode 100644 ports/cpu-features/usage
 create mode 100644 ports/cpu-features/usage_android
 create mode 100644 ports/cpu-features/vcpkg.json
 create mode 100644 versions/c-/cpu-features.json
2024-09-22 13:22:30,885 - 360 - WARNING - copy downloads/vcpkg/ports/getopt-win32 -> ./ports/getopt-win32
2024-09-22 13:22:30,887 - 369 - WARNING - copy downloads/vcpkg/versions/g-/getopt-win32.json -> ./versions/g-/getopt-win32.json
2024-09-22 13:22:30,888 - 382 - INFO - getopt-win32
commit 41e267049e8edaf37193794d46d33a3582985d5e
Author: Weihang Ding <798047000@qq.com>
Date:   2023-09-29 14:37:56 +0800

    [getopt-win32] Bump to 1.1.0.20220925 (#33893)

    * [getopt-win32] Bump to 1.1.0.20220925

    * Update version database

 ports/getopt-win32/getopt.h.patch | 50 ---------------------------------------
 ports/getopt-win32/portfile.cmake | 14 +++++------
 ports/getopt-win32/vcpkg.json     |  5 ++--
 versions/baseline.json            |  4 ++--
 versions/g-/getopt-win32.json     |  5 ++++
 5 files changed, 16 insertions(+), 62 deletions(-)

2024-09-22 13:22:30,888 - 147 - INFO - run: git add .
2024-09-22 13:22:30,912 - 147 - INFO - run: git commit -m [getopt-win32] Bump to 1.1.0.20220925 (#33893) --author Weihang Ding <798047000@qq.com>
[main 64fe3abdf] [getopt-win32] Bump to 1.1.0.20220925 (#33893)
 Author: Weihang Ding <798047000@qq.com>
 5 files changed, 134 insertions(+)
 create mode 100644 ports/getopt-win32/CMakeLists.txt
 create mode 100644 ports/getopt-win32/portfile.cmake
 create mode 100644 ports/getopt-win32/usage
 create mode 100644 ports/getopt-win32/vcpkg.json
 create mode 100644 versions/g-/getopt-win32.json
2024-09-22 13:22:30,979 - 360 - WARNING - copy downloads/vcpkg/ports/libgcrypt -> ./ports/libgcrypt
2024-09-22 13:22:30,981 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libgcrypt.json -> ./versions/l-/libgcrypt.json
2024-09-22 13:22:30,982 - 382 - INFO - libgcrypt
commit fc3b54c757d71afb094058b830bc2d6ec0013c2c
Author: Kai Pastor <dg0yt@darc.de>
Date:   2023-10-04 05:34:51 +0200

    [libgpg-error,libgcrypt,libassuan,gpgme,libgwenhywfar] Update and fix (#34135)

 ports/gpgme/disable-tests.patch         | 51 -----------------------------
 ports/gpgme/fix-c++11.patch             | 56 -------------------------------
 ports/gpgme/portfile.cmake              | 32 ++++++++++--------
 ports/gpgme/vcpkg.json                  | 10 ++----
 ports/libassuan/cross-tools.patch       |  8 ++---
 ports/libassuan/portfile.cmake          | 24 +++++++-------
 ports/libassuan/vcpkg.json              |  2 +-
 ports/libgcrypt/portfile.cmake          | 21 +++++++-----
 ports/libgcrypt/upstream-fa21ddc1.patch | 20 ++++++++++++
 ports/libgcrypt/vcpkg.json              |  3 +-
 ports/libgpg-error/gpgrt-config.patch   | 51 +++++++++++++++++++++++++++++
 ports/libgpg-error/portfile.cmake       | 16 +++------
 ports/libgpg-error/vcpkg.json           |  9 +++--
 ports/libgwenhywfar/portfile.cmake      | 58 +++++++++++++++++----------------
 ports/libgwenhywfar/vcpkg.json          | 12 +++++--
 versions/baseline.json                  | 12 +++----
 versions/g-/gpgme.json                  |  5 +++
 versions/l-/libassuan.json              |  5 +++
 versions/l-/libgcrypt.json              |  5 +++
 versions/l-/libgpg-error.json           |  5 +++
 versions/l-/libgwenhywfar.json          |  5 +++
 21 files changed, 201 insertions(+), 209 deletions(-)

2024-09-22 13:22:30,983 - 147 - INFO - run: git add .
2024-09-22 13:22:31,006 - 147 - INFO - run: git commit -m [libgpg-error,libgcrypt,libassuan,gpgme,libgwenhywfar] Update and fix (#34135) --author Kai Pastor <dg0yt@darc.de>
[main 4a4f0a921] [libgpg-error,libgcrypt,libassuan,gpgme,libgwenhywfar] Update and fix (#34135)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 193 insertions(+)
 create mode 100644 ports/libgcrypt/cross-tools.patch
 create mode 100644 ports/libgcrypt/portfile.cmake
 create mode 100644 ports/libgcrypt/upstream-fa21ddc1.patch
 create mode 100644 ports/libgcrypt/vcpkg.json
 create mode 100644 versions/l-/libgcrypt.json
2024-09-22 13:22:31,069 - 360 - WARNING - copy downloads/vcpkg/ports/brotli -> ./ports/brotli
2024-09-22 13:22:31,070 - 369 - WARNING - copy downloads/vcpkg/versions/b-/brotli.json -> ./versions/b-/brotli.json
2024-09-22 13:22:31,071 - 382 - INFO - brotli
commit 3acb7541e854452d33f71037a8f63a88899e63d3
Author: DownerCase <119755054+DownerCase@users.noreply.github.com>
Date:   2023-10-13 20:53:31 +0300

    [Brotli] Fix emscripten (#34157)

 ports/brotli/emscripten.patch | 15 +++++++++++++++
 ports/brotli/portfile.cmake   | 12 +++++++++---
 ports/brotli/vcpkg.json       |  1 +
 versions/b-/brotli.json       |  5 +++++
 versions/baseline.json        |  2 +-
 5 files changed, 31 insertions(+), 4 deletions(-)

2024-09-22 13:22:31,071 - 147 - INFO - run: git add .
2024-09-22 13:22:31,094 - 147 - INFO - run: git commit -m [Brotli] Fix emscripten (#34157) --author DownerCase <119755054+DownerCase@users.noreply.github.com>
[main ad242088c] [Brotli] Fix emscripten (#34157)
 Author: DownerCase <119755054+DownerCase@users.noreply.github.com>
 8 files changed, 246 insertions(+)
 create mode 100644 ports/brotli/emscripten.patch
 create mode 100644 ports/brotli/fix-arm-uwp.patch
 create mode 100644 ports/brotli/install.patch
 create mode 100644 ports/brotli/pkgconfig.patch
 create mode 100644 ports/brotli/portfile.cmake
 create mode 100644 ports/brotli/usage
 create mode 100644 ports/brotli/vcpkg.json
 create mode 100644 versions/b-/brotli.json
2024-09-22 13:22:31,157 - 360 - WARNING - copy downloads/vcpkg/ports/dirent -> ./ports/dirent
2024-09-22 13:22:31,159 - 369 - WARNING - copy downloads/vcpkg/versions/d-/dirent.json -> ./versions/d-/dirent.json
2024-09-22 13:22:31,159 - 382 - INFO - dirent
commit 91f1776a2c36e5431c4792c989aeaa50214fc0ff
Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
Date:   2023-10-18 02:09:26 +0800

    [dirent] update to 1.24 (#34043)

    * [dirent] update to 1.24

    * [dirent] update to 1.24

    * fix deps

    * fix deps

    * fix deps

    * fix deps

    * CI [skip actions]

    * CI [skip actions]

    * fix deps

    * CI [skip actions]

    * fix deps

 ports/dirent/portfile.cmake                        |  4 +--
 ports/dirent/vcpkg.json                            |  3 +-
 .../libmagic/0016-Fix-file_famagic-function.patch  | 40 ++++++++++++++++++++++
 ports/libmagic/portfile.cmake                      |  1 +
 ports/libmagic/vcpkg.json                          |  2 +-
 versions/baseline.json                             |  6 ++--
 versions/d-/dirent.json                            |  5 +++
 versions/l-/libmagic.json                          |  5 +++
 8 files changed, 58 insertions(+), 8 deletions(-)

2024-09-22 13:22:31,160 - 147 - INFO - run: git add .
2024-09-22 13:22:31,182 - 147 - INFO - run: git commit -m [dirent] update to 1.24 (#34043) --author Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
[main f16d8489f] [dirent] update to 1.24 (#34043)
 Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
 3 files changed, 63 insertions(+)
 create mode 100644 ports/dirent/portfile.cmake
 create mode 100644 ports/dirent/vcpkg.json
 create mode 100644 versions/d-/dirent.json
2024-09-22 13:22:31,246 - 360 - WARNING - copy downloads/vcpkg/ports/avisynthplus -> ./ports/avisynthplus
2024-09-22 13:22:31,248 - 369 - WARNING - copy downloads/vcpkg/versions/a-/avisynthplus.json -> ./versions/a-/avisynthplus.json
2024-09-22 13:22:31,249 - 382 - INFO - avisynthplus
commit b58df1160822908af3a50e3e45f8eb26d7006686
Author: Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
Date:   2023-11-14 21:54:21 +0100

    [ffmpeg] Bump to 6.1 (#35042)

    * [ffmpeg] Bump to 6.1

    * [ffnvcodec] Bump to 11.1.5.3

    * vcpkg x-add-version --all

    * [avisynthplus] Bump to 3.7.3

    * vcpkg x-add-version --all

    * [avisynthplus] Remove no more required patch

    * vcpkg x-add-version --all

    * Apply suggestions from code review

    Co-authored-by: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>

    * vcpkg x-add-version --all

    ---------

    Co-authored-by: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>

 ports/avisynthplus/clang-cl.patch              | 20 ---------
 ports/avisynthplus/portfile.cmake              |  6 +--
 ports/avisynthplus/vcpkg.json                  |  3 +-
 ports/ffmpeg/0001-create-lib-libraries.patch   |  6 ++-
 ports/ffmpeg/0004-fix-debug-build.patch        | 11 +++--
 ports/ffmpeg/0006-fix-StaticFeatures.patch     | 14 +++---
 ports/ffmpeg/0020-fix-aarch64-libswscale.patch | 16 +++----
 ports/ffmpeg/0024-fix-gcc13-binutils.patch     | 60 --------------------------
 ports/ffmpeg/portfile.cmake                    |  5 +--
 ports/ffmpeg/vcpkg.json                        |  3 +-
 ports/ffnvcodec/portfile.cmake                 |  4 +-
 ports/ffnvcodec/vcpkg.json                     |  2 +-
 versions/a-/avisynthplus.json                  |  5 +++
 versions/baseline.json                         | 10 ++---
 versions/f-/ffmpeg.json                        |  5 +++
 versions/f-/ffnvcodec.json                     |  5 +++
 16 files changed, 53 insertions(+), 122 deletions(-)

2024-09-22 13:22:31,249 - 147 - INFO - run: git add .
2024-09-22 13:22:31,271 - 147 - INFO - run: git commit -m [ffmpeg] Bump to 6.1 (#35042) --author Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
[main ead41ef98] [ffmpeg] Bump to 6.1 (#35042)
 Author: Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
 3 files changed, 108 insertions(+)
 create mode 100644 ports/avisynthplus/portfile.cmake
 create mode 100644 ports/avisynthplus/vcpkg.json
 create mode 100644 versions/a-/avisynthplus.json
2024-09-22 13:22:31,337 - 360 - WARNING - copy downloads/vcpkg/ports/libtheora -> ./ports/libtheora
2024-09-22 13:22:31,340 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libtheora.json -> ./versions/l-/libtheora.json
2024-09-22 13:22:31,341 - 382 - INFO - libtheora
commit a42af01b72c28a8e1d7b48107b33e4f286a55ef6
Author: Park DongHa <luncliff@gmail.com>
Date:   2023-11-21 12:31:49 +0900

    [libtheora] install pkg-config files (#34904)

    * [libtheora] create pkg-config files

    * [libtheora] fix expression

    * [libtheora] update baseline

    * [libtheora] provide version from portfile

    * Update ports/libtheora/CMakeLists.txt

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

    * Update ports/libtheora/portfile.cmake

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

    * Update ports/libtheora/CMakeLists.txt

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

    * [libtheora] update baseline

    ---------

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

 ports/libtheora/CMakeLists.txt | 13 +++++++++++++
 ports/libtheora/portfile.cmake |  3 ++-
 ports/libtheora/vcpkg.json     |  2 +-
 versions/baseline.json         |  2 +-
 versions/l-/libtheora.json     |  5 +++++
 5 files changed, 22 insertions(+), 3 deletions(-)

2024-09-22 13:22:31,342 - 147 - INFO - run: git add .
2024-09-22 13:22:31,364 - 147 - INFO - run: git commit -m [libtheora] install pkg-config files (#34904) --author Park DongHa <luncliff@gmail.com>
[main c4970bee0] [libtheora] install pkg-config files (#34904)
 Author: Park DongHa <luncliff@gmail.com>
 7 files changed, 394 insertions(+)
 create mode 100644 ports/libtheora/0001-fix-uwp.patch
 create mode 100644 ports/libtheora/CMakeLists.txt
 create mode 100644 ports/libtheora/libtheora.def
 create mode 100644 ports/libtheora/portfile.cmake
 create mode 100644 ports/libtheora/unofficial-theora-config.cmake.in
 create mode 100644 ports/libtheora/vcpkg.json
 create mode 100644 versions/l-/libtheora.json
2024-09-22 13:22:31,429 - 360 - WARNING - copy downloads/vcpkg/ports/graphite2 -> ./ports/graphite2
2024-09-22 13:22:31,430 - 369 - WARNING - copy downloads/vcpkg/versions/g-/graphite2.json -> ./versions/g-/graphite2.json
2024-09-22 13:22:31,431 - 382 - INFO - graphite2
commit 92a8ae82bc57e0a782cfc4c81e75c81a38534105
Author: Kai Pastor <dg0yt@darc.de>
Date:   2023-12-06 23:04:33 +0100

    [graphite2] Burn-in library linkage (#35528)

 ports/graphite2/portfile.cmake | 9 ++++++---
 ports/graphite2/vcpkg.json     | 2 +-
 versions/baseline.json         | 2 +-
 versions/g-/graphite2.json     | 5 +++++
 4 files changed, 13 insertions(+), 5 deletions(-)

2024-09-22 13:22:31,432 - 147 - INFO - run: git add .
2024-09-22 13:22:31,454 - 147 - INFO - run: git commit -m [graphite2] Burn-in library linkage (#35528) --author Kai Pastor <dg0yt@darc.de>
[main 4889c443c] [graphite2] Burn-in library linkage (#35528)
 Author: Kai Pastor <dg0yt@darc.de>
 4 files changed, 147 insertions(+)
 create mode 100644 ports/graphite2/disable-tests.patch
 create mode 100644 ports/graphite2/portfile.cmake
 create mode 100644 ports/graphite2/vcpkg.json
 create mode 100644 versions/g-/graphite2.json
2024-09-22 13:22:31,579 - 360 - WARNING - copy downloads/vcpkg/ports/soxr -> ./ports/soxr
2024-09-22 13:22:31,581 - 369 - WARNING - copy downloads/vcpkg/versions/s-/soxr.json -> ./versions/s-/soxr.json
2024-09-22 13:22:31,582 - 382 - INFO - soxr
commit 81052aa9b7801644c0a8e806809d8af45143fbcf
Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
Date:   2024-02-06 21:39:03 +0100

    [soxr] do not autodetect lib (#36587)

 ports/soxr/portfile.cmake | 5 +++--
 ports/soxr/vcpkg.json     | 2 +-
 versions/baseline.json    | 2 +-
 versions/s-/soxr.json     | 5 +++++
 4 files changed, 10 insertions(+), 4 deletions(-)

2024-09-22 13:22:31,582 - 147 - INFO - run: git add .
2024-09-22 13:22:31,606 - 147 - INFO - run: git commit -m [soxr] do not autodetect lib (#36587) --author autoantwort <41973254+autoantwort@users.noreply.github.com>
[main c6e44c226] [soxr] do not autodetect lib (#36587)
 Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
 6 files changed, 143 insertions(+)
 create mode 100644 ports/soxr/001_initialize-resampler.patch
 create mode 100644 ports/soxr/002_disable_warning.patch
 create mode 100644 ports/soxr/003_detect_arm.patch
 create mode 100644 ports/soxr/portfile.cmake
 create mode 100644 ports/soxr/vcpkg.json
 create mode 100644 versions/s-/soxr.json
2024-09-22 13:22:31,670 - 360 - WARNING - copy downloads/vcpkg/ports/egl-registry -> ./ports/egl-registry
2024-09-22 13:22:31,673 - 369 - WARNING - copy downloads/vcpkg/versions/e-/egl-registry.json -> ./versions/e-/egl-registry.json
2024-09-22 13:22:31,674 - 382 - INFO - egl-registry
commit d0d63ec3bb4e8a844b15293e920865563ecd787e
Author: moritz-h <7849248+moritz-h@users.noreply.github.com>
Date:   2024-02-21 18:32:54 +0100

    [opengl-registry/egl-registry] update (#36856)

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [x] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [x] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [x] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    This PR updates the `opengl-registry` and `egl-registry` ports to the
    latest version. In addition both ports have broken copyright information
    as both repositories are using individual licenses for each file. I
    tried to fix this by including a vendored copyright file for the
    `egl-registry` port. For `opengl-registry` I have just included a note
    that all files are individually licensed. A proper fix for this seems to
    be already worked on in #28644.

 ports/egl-registry/copyright         | 28 ++++++++++++++++++++++++++++
 ports/egl-registry/portfile.cmake    | 11 +++--------
 ports/egl-registry/vcpkg.json        |  4 ++--
 ports/opengl-registry/copyright      |  2 ++
 ports/opengl-registry/portfile.cmake | 13 ++++---------
 ports/opengl-registry/vcpkg.json     |  4 ++--
 versions/baseline.json               |  4 ++--
 versions/e-/egl-registry.json        |  5 +++++
 versions/o-/opengl-registry.json     |  5 +++++
 9 files changed, 53 insertions(+), 23 deletions(-)

2024-09-22 13:22:31,674 - 147 - INFO - run: git add .
2024-09-22 13:22:31,698 - 147 - INFO - run: git commit -m [opengl-registry/egl-registry] update (#36856) --author moritz-h <7849248+moritz-h@users.noreply.github.com>
[main 24579178e] [opengl-registry/egl-registry] update (#36856)
 Author: moritz-h <7849248+moritz-h@users.noreply.github.com>
 4 files changed, 110 insertions(+)
 create mode 100644 ports/egl-registry/copyright
 create mode 100644 ports/egl-registry/portfile.cmake
 create mode 100644 ports/egl-registry/vcpkg.json
 create mode 100644 versions/e-/egl-registry.json
2024-09-22 13:22:31,790 - 360 - WARNING - copy downloads/vcpkg/ports/giflib -> ./ports/giflib
2024-09-22 13:22:31,795 - 369 - WARNING - copy downloads/vcpkg/versions/g-/giflib.json -> ./versions/g-/giflib.json
2024-09-22 13:22:31,796 - 382 - INFO - giflib
commit 198ea1e47ae69700d3713900fc0d2cb8cb5c547c
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-02-29 02:08:22 +0100

    [giflib] Update to 5.2.2 (#36975)

    Refresh patches
    Use strtok_s for strtok_r on MSVC, export GifDrawBoxedText8x8.

 .../giflib/disable-GifDrawBoxedText8x8-win32.patch | 36 ---------
 ports/giflib/exports.def                           |  2 +-
 ports/giflib/fix-compile-error.patch               | 75 ------------------
 ports/giflib/msvc-guard-unistd-h.patch             | 14 ----
 ports/giflib/msvc.diff                             | 89 ++++++++++++++++++++++
 ports/giflib/portfile.cmake                        | 12 +--
 ports/giflib/vcpkg.json                            |  3 +-
 versions/baseline.json                             |  4 +-
 versions/g-/giflib.json                            |  5 ++
 9 files changed, 102 insertions(+), 138 deletions(-)

2024-09-22 13:22:31,796 - 147 - INFO - run: git add .
2024-09-22 13:22:31,819 - 147 - INFO - run: git commit -m [giflib] Update to 5.2.2 (#36975) --author Kai Pastor <dg0yt@darc.de>
[main 995a43bea] [giflib] Update to 5.2.2 (#36975)
 Author: Kai Pastor <dg0yt@darc.de>
 8 files changed, 319 insertions(+)
 create mode 100644 ports/giflib/CMakeLists.txt
 create mode 100644 ports/giflib/exports.def
 create mode 100644 ports/giflib/msvc.diff
 create mode 100644 ports/giflib/portfile.cmake
 create mode 100644 ports/giflib/usage
 create mode 100644 ports/giflib/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/giflib/vcpkg.json
 create mode 100644 versions/g-/giflib.json
2024-09-22 13:22:31,908 - 360 - WARNING - copy downloads/vcpkg/ports/lerc -> ./ports/lerc
2024-09-22 13:22:31,911 - 369 - WARNING - copy downloads/vcpkg/versions/l-/lerc.json -> ./versions/l-/lerc.json
2024-09-22 13:22:31,912 - 382 - INFO - lerc
commit 408a9027bf13bed59d4a2a723c9df10e8b5a098b
Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
Date:   2024-03-08 14:49:57 +0800

    [lerc] update to 4.0.4 (#37163)

    - [X] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md)
    - [X] SHA512s are updated for each updated download
    - [ ] ~The "supports" clause reflects platforms that may be fixed by
    this new version~
    - [ ] ~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~
    - [ ] ~Any patches that are no longer applied are deleted from the
    port's directory.~
    - [X] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [X] Only one version is added to each modified port's versions file.

 ports/lerc/create_package.patch                |  9 ++++-----
 ports/lerc/cxx-linkage-pkgconfig.patch         |  8 ++++----
 ports/lerc/fix-climits-include.patch           | 12 ++++++++++++
 ports/lerc/include_algorithm_for_std_min.patch | 24 ------------------------
 ports/lerc/portfile.cmake                      |  6 +++---
 ports/lerc/vcpkg.json                          |  3 +--
 versions/baseline.json                         |  4 ++--
 versions/l-/lerc.json                          |  5 +++++
 8 files changed, 31 insertions(+), 40 deletions(-)

2024-09-22 13:22:31,912 - 147 - INFO - run: git add .
2024-09-22 13:22:31,935 - 147 - INFO - run: git commit -m [lerc] update to 4.0.4 (#37163) --author Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
[main e8f98ee22] [lerc] update to 4.0.4 (#37163)
 Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
 6 files changed, 154 insertions(+)
 create mode 100644 ports/lerc/create_package.patch
 create mode 100644 ports/lerc/cxx-linkage-pkgconfig.patch
 create mode 100644 ports/lerc/fix-climits-include.patch
 create mode 100644 ports/lerc/portfile.cmake
 create mode 100644 ports/lerc/vcpkg.json
 create mode 100644 versions/l-/lerc.json
2024-09-22 13:22:32,005 - 360 - WARNING - copy downloads/vcpkg/ports/glib -> ./ports/glib
2024-09-22 13:22:32,008 - 369 - WARNING - copy downloads/vcpkg/versions/g-/glib.json -> ./versions/g-/glib.json
2024-09-22 13:22:32,008 - 382 - INFO - glib
commit a664e41ee50b61adcc90a44a761eca139a4b7dd7
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-03-11 22:09:15 +0100

    [vcpkg-tool-meson] Update meson to 1.3.2 (#28084)

 ports/gdk-pixbuf/fix-static-deps.patch             |  12 +
 ports/gdk-pixbuf/portfile.cmake                    |   2 +-
 ports/gdk-pixbuf/vcpkg.json                        |   2 +-
 ports/glib/libintl.patch                           |   2 +-
 ports/glib/vcpkg.json                              |   1 +
 ports/gobject-introspection/portfile.cmake         |  10 +-
 ports/gobject-introspection/vcpkg.json             |   6 +-
 ports/libnice/vcpkg.json                           |   8 +-
 ports/mesa/portfile.cmake                          |   5 +
 ports/mesa/vcpkg.json                              |   1 +
 ports/thorvg/portfile.cmake                        |   4 +-
 ports/thorvg/vcpkg.json                            |   1 +
 ports/vcpkg-tool-meson/adjust-args.patch           |  12 +
 ports/vcpkg-tool-meson/adjust-python-dep.patch     |  46 +++
 ports/vcpkg-tool-meson/meson-intl.patch            |   5 +-
 ports/vcpkg-tool-meson/meson.template.in           |  41 ++
 ports/vcpkg-tool-meson/portfile.cmake              |  86 ++--
 .../remove-freebsd-pcfile-specialization.patch     |  23 +-
 ports/vcpkg-tool-meson/vcpkg-port-config.cmake     |  64 ++-
 ports/vcpkg-tool-meson/vcpkg.json                  |   3 +-
 ports/vcpkg-tool-meson/vcpkg_configure_meson.cmake | 452 +++++++++++++++++++++
 ports/vcpkg-tool-meson/vcpkg_install_meson.cmake   |  71 ++++
 ports/xcb-proto/portfile.cmake                     |   4 +-
 ports/xcb-proto/vcpkg.json                         |   2 +-
 scripts/cmake/vcpkg_configure_meson.cmake          |  27 +-
 .../cmake/vcpkg_find_acquire_program(MESON).cmake  |   2 +-
 versions/baseline.json                             |  18 +-
 versions/g-/gdk-pixbuf.json                        |   5 +
 versions/g-/glib.json                              |   5 +
 versions/g-/gobject-introspection.json             |   5 +
 versions/l-/libnice.json                           |   5 +
 versions/m-/mesa.json                              |   5 +
 versions/t-/thorvg.json                            |   5 +
 versions/v-/vcpkg-tool-meson.json                  |   5 +
 versions/x-/xcb-proto.json                         |   5 +
 35 files changed, 849 insertions(+), 101 deletions(-)

2024-09-22 13:22:32,009 - 147 - INFO - run: git add .
2024-09-22 13:22:32,033 - 147 - INFO - run: git commit -m [vcpkg-tool-meson] Update meson to 1.3.2 (#28084) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main e8ddec309] [vcpkg-tool-meson] Update meson to 1.3.2 (#28084)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 5 files changed, 516 insertions(+)
 create mode 100644 ports/glib/libintl.patch
 create mode 100644 ports/glib/portfile.cmake
 create mode 100644 ports/glib/use-libiconv-on-windows.patch
 create mode 100644 ports/glib/vcpkg.json
 create mode 100644 versions/g-/glib.json
2024-09-22 13:22:32,094 - 360 - WARNING - copy downloads/vcpkg/ports/ffnvcodec -> ./ports/ffnvcodec
2024-09-22 13:22:32,096 - 369 - WARNING - copy downloads/vcpkg/versions/f-/ffnvcodec.json -> ./versions/f-/ffnvcodec.json
2024-09-22 13:22:32,097 - 382 - INFO - ffnvcodec
commit 3c58f93014204ebc81b211f4c885c2aefb4abf8f
Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
Date:   2024-03-12 04:10:54 +0800

    [ffnvcodec] update to 12.1.14.0 (#37322)

    - [X] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md)
    - [X] SHA512s are updated for each updated download
    - [ ] ~The "supports" clause reflects platforms that may be fixed by
    this new version~
    - [ ] ~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~
    - [ ] ~Any patches that are no longer applied are deleted from the
    port's directory.~
    - [X] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [X] Only one version is added to each modified port's versions file.

 ports/ffnvcodec/portfile.cmake | 2 +-
 ports/ffnvcodec/vcpkg.json     | 2 +-
 versions/baseline.json         | 2 +-
 versions/f-/ffnvcodec.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:32,097 - 147 - INFO - run: git add .
2024-09-22 13:22:32,119 - 147 - INFO - run: git commit -m [ffnvcodec] update to 12.1.14.0 (#37322) --author Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
[main af6fe6833] [ffnvcodec] update to 12.1.14.0 (#37322)
 Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
 6 files changed, 346 insertions(+)
 create mode 100644 ports/ffnvcodec/LICENSE.txt
 create mode 100644 ports/ffnvcodec/build.sh
 create mode 100644 ports/ffnvcodec/copyright
 create mode 100644 ports/ffnvcodec/portfile.cmake
 create mode 100644 ports/ffnvcodec/vcpkg.json
 create mode 100644 versions/f-/ffnvcodec.json
2024-09-22 13:22:32,180 - 360 - WARNING - copy downloads/vcpkg/ports/libunistring -> ./ports/libunistring
2024-09-22 13:22:32,183 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libunistring.json -> ./versions/l-/libunistring.json
2024-09-22 13:22:32,183 - 382 - INFO - libunistring
commit e2dcca969356157c1562394abb41d6b10b629322
Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
Date:   2024-03-12 04:12:02 +0800

    [libunistring] update to 1.2 (#37266)

    - [X] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md)
    - [X] SHA512s are updated for each updated download
    - [ ] ~The "supports" clause reflects platforms that may be fixed by
    this new version~
    - [ ] ~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~
    - [ ] ~Any patches that are no longer applied are deleted from the
    port's directory.~
    - [X] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [X] Only one version is added to each modified port's versions file.

 ports/libunistring/portfile.cmake | 2 +-
 ports/libunistring/vcpkg.json     | 3 +--
 versions/baseline.json            | 4 ++--
 versions/l-/libunistring.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:22:32,184 - 147 - INFO - run: git add .
2024-09-22 13:22:32,205 - 147 - INFO - run: git commit -m [libunistring] update to 1.2 (#37266) --author Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
[main fff3616cf] [libunistring] update to 1.2 (#37266)
 Author: Jia Yue Hua <3423893+jiayuehua@users.noreply.github.com>
 7 files changed, 191 insertions(+)
 create mode 100644 ports/libunistring/copyright
 create mode 100644 ports/libunistring/disable-gnulib-fetch.patch
 create mode 100644 ports/libunistring/disable-subdirs.patch
 create mode 100644 ports/libunistring/parallelize-symbol-collection.patch
 create mode 100644 ports/libunistring/portfile.cmake
 create mode 100644 ports/libunistring/vcpkg.json
 create mode 100644 versions/l-/libunistring.json
2024-09-22 13:22:32,269 - 360 - WARNING - copy downloads/vcpkg/ports/libvpx -> ./ports/libvpx
2024-09-22 13:22:32,273 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libvpx.json -> ./versions/l-/libvpx.json
2024-09-22 13:22:32,273 - 382 - INFO - libvpx
commit 65bd24dc944274a2aeb6a86e42e74330fd2c6ffd
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-03-12 04:33:15 +0100

    Don't require vcpkg-msbuild for mingw (#37336)

    Amends #33105 et al.

    Ports selected by grep for vcpkg-msbuild in vcpkg.json && MINGW in
    portfile.cmake.

 ports/libmicrohttpd/vcpkg.json |  3 ++-
 ports/libusb/vcpkg.json        |  3 ++-
 ports/libvpx/vcpkg.json        |  4 ++--
 ports/mp3lame/vcpkg.json       |  4 ++--
 ports/sdl1/vcpkg.json          |  4 ++--
 versions/baseline.json         | 10 +++++-----
 versions/l-/libmicrohttpd.json |  5 +++++
 versions/l-/libusb.json        |  5 +++++
 versions/l-/libvpx.json        |  5 +++++
 versions/m-/mp3lame.json       |  5 +++++
 versions/s-/sdl1.json          |  5 +++++
 11 files changed, 40 insertions(+), 13 deletions(-)

2024-09-22 13:22:32,273 - 147 - INFO - run: git add .
2024-09-22 13:22:32,296 - 147 - INFO - run: git commit -m Don't require vcpkg-msbuild for mingw (#37336) --author Kai Pastor <dg0yt@darc.de>
[main ce1972568] Don't require vcpkg-msbuild for mingw (#37336)
 Author: Kai Pastor <dg0yt@darc.de>
 9 files changed, 794 insertions(+)
 create mode 100644 ports/libvpx/0002-Fix-nasm-debug-format-flag.patch
 create mode 100644 ports/libvpx/0003-add-uwp-v142-and-v143-support.patch
 create mode 100644 ports/libvpx/0004-remove-library-suffixes.patch
 create mode 100644 ports/libvpx/0005-fix-arm64-build.patch
 create mode 100644 ports/libvpx/portfile.cmake
 create mode 100644 ports/libvpx/unofficial-libvpx-config.cmake.in
 create mode 100644 ports/libvpx/vcpkg.json
 create mode 100644 ports/libvpx/vpx.pc.in
 create mode 100644 versions/l-/libvpx.json
2024-09-22 13:22:32,357 - 360 - WARNING - copy downloads/vcpkg/ports/libmount -> ./ports/libmount
2024-09-22 13:22:32,359 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libmount.json -> ./versions/l-/libmount.json
2024-09-22 13:22:32,359 - 382 - INFO - libmount
commit 41e2412494b99064a7690be505197868fe505598
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-04-02 00:04:12 +0200

    [libmount,libsystemd] Updates, fixes (#37869)

 ports/libmount/hide-private-symbols.diff       | 15 ++++++
 ports/libmount/portfile.cmake                  |  4 +-
 ports/libmount/vcpkg.json                      |  2 +-
 ports/libsystemd/disable-warning-nonnull.patch | 14 ++++++
 ports/libsystemd/only-libsystemd.patch         | 62 ++++++++++++++++++++++++
 ports/libsystemd/pkgconfig.patch               | 18 ++++++-
 ports/libsystemd/portfile.cmake                | 65 ++++++++++----------------
 ports/libsystemd/vcpkg.json                    |  3 +-
 versions/baseline.json                         |  4 +-
 versions/l-/libmount.json                      |  5 ++
 versions/l-/libsystemd.json                    |  5 ++
 11 files changed, 149 insertions(+), 48 deletions(-)

2024-09-22 13:22:32,359 - 147 - INFO - run: git add .
2024-09-22 13:22:32,382 - 147 - INFO - run: git commit -m [libmount,libsystemd] Updates, fixes (#37869) --author Kai Pastor <dg0yt@darc.de>
[main 9269dfcf8] [libmount,libsystemd] Updates, fixes (#37869)
 Author: Kai Pastor <dg0yt@darc.de>
 4 files changed, 124 insertions(+)
 create mode 100644 ports/libmount/hide-private-symbols.diff
 create mode 100644 ports/libmount/portfile.cmake
 create mode 100644 ports/libmount/vcpkg.json
 create mode 100644 versions/l-/libmount.json
2024-09-22 13:22:32,443 - 360 - WARNING - copy downloads/vcpkg/ports/ncurses -> ./ports/ncurses
2024-09-22 13:22:32,445 - 369 - WARNING - copy downloads/vcpkg/versions/n-/ncurses.json -> ./versions/n-/ncurses.json
2024-09-22 13:22:32,446 - 382 - INFO - ncurses
commit be4195ad1079827dbd7da07b6162bc06b04a1c9c
Author: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
Date:   2024-04-10 00:16:18 +0800

    [ncurses] Fixing insufficient usage message (#37942)

    <!-- If your PR fixes issues, please note that here by adding "Fixes
    #NNNNNN." for each fixed issue on separate lines. -->
    Fixes https://github.com/microsoft/vcpkg/issues/37867

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [ ] ~SHA512s are updated for each updated download.~
    - [ ] ~The "supports" clause reflects platforms that may be fixed by
    this new version.~
    - [ ] ~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~
    - [ ] ~Any patches that are no longer applied are deleted from the
    port's directory.~
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

 ports/ncurses/portfile.cmake | 2 +-
 ports/ncurses/usage          | 4 ++--
 ports/ncurses/vcpkg.json     | 2 +-
 versions/baseline.json       | 2 +-
 versions/n-/ncurses.json     | 5 +++++
 5 files changed, 10 insertions(+), 5 deletions(-)

2024-09-22 13:22:32,446 - 147 - INFO - run: git add .
2024-09-22 13:22:32,468 - 147 - INFO - run: git commit -m [ncurses] Fixing insufficient usage message (#37942) --author Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
[main 29396eba0] [ncurses] Fixing insufficient usage message (#37942)
 Author: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
 4 files changed, 136 insertions(+)
 create mode 100644 ports/ncurses/portfile.cmake
 create mode 100644 ports/ncurses/usage
 create mode 100644 ports/ncurses/vcpkg.json
 create mode 100644 versions/n-/ncurses.json
2024-09-22 13:22:32,551 - 360 - WARNING - copy downloads/vcpkg/ports/pcre2 -> ./ports/pcre2
2024-09-22 13:22:32,554 - 369 - WARNING - copy downloads/vcpkg/versions/p-/pcre2.json -> ./versions/p-/pcre2.json
2024-09-22 13:22:32,554 - 382 - INFO - pcre2
commit 00abcfb2e3614ae3b0594c43497b74346b3025d5
Author: Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
Date:   2024-04-19 04:54:25 -0700

    [pcre2] Update to 10.43 (#38105)

    <!-- If your PR fixes issues, please note that here by adding "Fixes
    #NNNNNN." for each fixed issue on separate lines. -->
    Fixes #38083
    <!-- If you are still working on the PR, open it as a Draft:
    https://github.blog/2019-02-14-introducing-draft-pull-requests/. -->



    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [ ] ~~The "supports" clause reflects platforms that may be fixed by
    this new version.~~
    - [ ] ~~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~~
    - [ ] ~~Any patches that are no longer applied are deleted from the
    port's directory.~~
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    All features passed with following triplets:
    ```
    x86-windows
    x64-windows
    x64-windows-static
    ```
    Usage test passed on `x64-windows`.
    <!-- If this PR adds a new port, please uncomment and fill out this
    checklist:

    - [ ] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [ ] The name of the port matches an existing name for this component
    on https://repology.org/ if possible, and/or is strongly associated with
    that component on search engines.
    - [ ] Optional dependencies are resolved in exactly one way. For
    example, if the component is built with CMake, all `find_package` calls
    are REQUIRED, are satisfied by `vcpkg.json`'s declared dependencies, or
    disabled with
    [CMAKE_DISABLE_FIND_PACKAGE_Xxx](https://cmake.org/cmake/help/latest/variable/CMAKE_DISABLE_FIND_PACKAGE_PackageName.html).
    - [ ] The versioning scheme in `vcpkg.json` matches what upstream says.
    - [ ] The license declaration in `vcpkg.json` matches what upstream
    says.
    - [ ] The installed as the "copyright" file matches what upstream says.
    - [ ] The source code of the component installed comes from an
    authoritative source.
    - [ ] The generated "usage text" is accurate. See
    [adding-usage](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/examples/adding-usage.md)
    for context.
    - [ ] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [ ] Only one version is in the new port's versions file.
    - [ ] Only one version is added to each modified port's versions file.

    END OF NEW PORT CHECKLIST (delete this line) -->

    ---------

    Co-authored-by: Lily Wang <v-lilywang@microsoft.com>

 ports/pcre2/fix-cmake.patch        | 155 +++++++++++++++++--------------------
 ports/pcre2/no-static-suffix.patch |  14 ++--
 ports/pcre2/portfile.cmake         |   2 +-
 ports/pcre2/vcpkg.json             |   3 +-
 versions/baseline.json             |   4 +-
 versions/p-/pcre2.json             |   5 ++
 6 files changed, 88 insertions(+), 95 deletions(-)

2024-09-22 13:22:32,555 - 147 - INFO - run: git add .
2024-09-22 13:22:32,578 - 147 - INFO - run: git commit -m [pcre2] Update to 10.43 (#38105) --author Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
[main 123b82309] [pcre2] Update to 10.43 (#38105)
 Author: Lily Wang <94091114+LilyWangLL@users.noreply.github.com>
 7 files changed, 636 insertions(+)
 create mode 100644 ports/pcre2/fix-cmake.patch
 create mode 100644 ports/pcre2/no-static-suffix.patch
 create mode 100644 ports/pcre2/pcre2-10.35_fix-uwp.patch
 create mode 100644 ports/pcre2/portfile.cmake
 create mode 100644 ports/pcre2/usage
 create mode 100644 ports/pcre2/vcpkg.json
 create mode 100644 versions/p-/pcre2.json
2024-09-22 13:22:32,640 - 360 - WARNING - copy downloads/vcpkg/ports/libx11 -> ./ports/libx11
2024-09-22 13:22:32,645 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libx11.json -> ./versions/l-/libx11.json
2024-09-22 13:22:32,645 - 382 - INFO - libx11
commit 6ab331448c76fbd1ca4fb599d374924e6d5e3024
Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
Date:   2024-04-23 18:14:09 +0200

    [libx11] Optimize Build (#38319)

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [x] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [x] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [x] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    To beat:
    - x64-windows: 28 min
    - x86-windows: 28 min
    - x64-windows-static-md: 26 min
    - x64-windows-static: 26 min
    - arm64-windows: 26 min

 ports/libx11/optimize-configure.patch | 13 +++++++++++++
 ports/libx11/portfile.cmake           | 12 +++++++-----
 ports/libx11/vcpkg.json               |  2 +-
 versions/baseline.json                |  2 +-
 versions/l-/libx11.json               |  5 +++++
 5 files changed, 27 insertions(+), 7 deletions(-)

2024-09-22 13:22:32,646 - 147 - INFO - run: git add .
2024-09-22 13:22:32,669 - 147 - INFO - run: git commit -m [libx11] Optimize Build (#38319) --author Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
[main 44792fd1a] [libx11] Optimize Build (#38319)
 Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
 10 files changed, 564 insertions(+)
 create mode 100644 ports/libx11/add_dl_pc.patch
 create mode 100644 ports/libx11/cl.build.patch
 create mode 100644 ports/libx11/dllimport.patch
 create mode 100644 ports/libx11/io_include.patch
 create mode 100644 ports/libx11/optimize-configure.patch
 create mode 100644 ports/libx11/portfile.cmake
 create mode 100644 ports/libx11/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/libx11/vcpkg.json
 create mode 100644 ports/libx11/vcxserver.patch
 create mode 100644 versions/l-/libx11.json
2024-09-22 13:22:32,734 - 360 - WARNING - copy downloads/vcpkg/ports/cairo -> ./ports/cairo
2024-09-22 13:22:32,737 - 369 - WARNING - copy downloads/vcpkg/versions/c-/cairo.json -> ./versions/c-/cairo.json
2024-09-22 13:22:32,738 - 382 - INFO - cairo
commit a6fff517cc6807dfe128431bb7805e47eb73717c
Author: Sebastian Sch盲fer <38749758+scschaefer@users.noreply.github.com>
Date:   2024-04-24 14:05:39 +0200

    [cairo] Move hard lzo dependency to feature (#38313)

    Fixes #38312

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [ ] SHA512s are updated for each updated download.
    - [ ] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [ ] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [ ] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

 ports/cairo/cairo_add_lzo_feature_option.patch | 25 +++++++++++++++++++++++++
 ports/cairo/portfile.cmake                     |  7 +++++++
 ports/cairo/vcpkg.json                         |  8 +++++++-
 versions/baseline.json                         |  2 +-
 versions/c-/cairo.json                         |  5 +++++
 5 files changed, 45 insertions(+), 2 deletions(-)

2024-09-22 13:22:32,738 - 147 - INFO - run: git add .
2024-09-22 13:22:32,762 - 147 - INFO - run: git commit -m [cairo] Move hard lzo dependency to feature (#38313) --author Sebastian Sch盲fer <38749758+scschaefer@users.noreply.github.com>
[main adc2b34b2] [cairo] Move hard lzo dependency to feature (#38313)
 Author: Sebastian Sch盲fer <38749758+scschaefer@users.noreply.github.com>
 10 files changed, 505 insertions(+)
 create mode 100644 ports/cairo/cairo_add_lzo_feature_option.patch
 create mode 100644 ports/cairo/cairo_static_fix.patch
 create mode 100644 ports/cairo/disable-atomic-ops-check.patch
 create mode 100644 ports/cairo/fix-alloca-undefine.patch
 create mode 100644 ports/cairo/fix-static-missing-lib-msimg32.patch
 create mode 100644 ports/cairo/fix_clang-cl_build.patch
 create mode 100644 ports/cairo/portfile.cmake
 create mode 100644 ports/cairo/usage
 create mode 100644 ports/cairo/vcpkg.json
 create mode 100644 versions/c-/cairo.json
2024-09-22 13:22:32,824 - 360 - WARNING - copy downloads/vcpkg/ports/amd-amf -> ./ports/amd-amf
2024-09-22 13:22:32,825 - 369 - WARNING - copy downloads/vcpkg/versions/a-/amd-amf.json -> ./versions/a-/amd-amf.json
2024-09-22 13:22:32,826 - 382 - INFO - amd-amf
commit b9091ce29ef3297b95bf6f7c594fff0d5b9a3dbb
Author: Adrian Bibby Walther <adrianbibbywalther@gmail.com>
Date:   2024-04-29 15:08:30 +0200

    [amd-amf] Fix SHA512 hash (#38435)

    #38382 forgot to update the SHA512 hash, breaking the package. This
    fixes it. I've tested that it builds again.

    - [X] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [X] SHA512s are updated for each updated download.
    - [X] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [X] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [X] Any patches that are no longer applied are deleted from the port's
    directory.
    - [X] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [X] Only one version is added to each modified port's versions file.

 ports/amd-amf/portfile.cmake | 2 +-
 ports/amd-amf/vcpkg.json     | 1 +
 versions/a-/amd-amf.json     | 5 +++++
 versions/baseline.json       | 2 +-
 4 files changed, 8 insertions(+), 2 deletions(-)

2024-09-22 13:22:32,826 - 147 - INFO - run: git add .
2024-09-22 13:22:32,850 - 147 - INFO - run: git commit -m [amd-amf] Fix SHA512 hash (#38435) --author Adrian Bibby Walther <adrianbibbywalther@gmail.com>
[main cdfd5d452] [amd-amf] Fix SHA512 hash (#38435)
 Author: Adrian Bibby Walther <adrianbibbywalther@gmail.com>
 3 files changed, 44 insertions(+)
 create mode 100644 ports/amd-amf/portfile.cmake
 create mode 100644 ports/amd-amf/vcpkg.json
 create mode 100644 versions/a-/amd-amf.json
2024-09-22 13:22:32,913 - 360 - WARNING - copy downloads/vcpkg/ports/libxcrypt -> ./ports/libxcrypt
2024-09-22 13:22:32,914 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libxcrypt.json -> ./versions/l-/libxcrypt.json
2024-09-22 13:22:32,915 - 382 - INFO - libxcrypt
commit 9f22b3df4c33e312f919caff260edaee28b47e84
Author: WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
Date:   2024-04-30 18:25:23 +0000

    [libxcrypt] Add build requirements (#38376)

    Fix #38372

    Add message of build requirements `autoconf` `automake` `libtool`
    `pkg-config` from [upstream
    README](https://github.com/besser82/libxcrypt?tab=readme-ov-file#build-requirements-and-instructions)

    ### Checklist
    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [ ] ~SHA512s are updated for each updated download.~
    - [ ] ~The "supports" clause reflects platforms that may be fixed by
    this new version.~
    - [ ] ~Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.~
    - [ ] ~Any patches that are no longer applied are deleted from the
    port's directory.~
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    ### Test
    Port install tests pass with following triplets:
    * x64-linux

 ports/libxcrypt/portfile.cmake | 15 +++++++++++++++
 ports/libxcrypt/vcpkg.json     |  1 +
 versions/baseline.json         |  2 +-
 versions/l-/libxcrypt.json     |  5 +++++
 4 files changed, 22 insertions(+), 1 deletion(-)

2024-09-22 13:22:32,915 - 147 - INFO - run: git add .
2024-09-22 13:22:32,937 - 147 - INFO - run: git commit -m [libxcrypt] Add build requirements (#38376) --author WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
[main 1626297f4] [libxcrypt] Add build requirements (#38376)
 Author: WangWeiLin-MV <156736127+WangWeiLin-MV@users.noreply.github.com>
 3 files changed, 58 insertions(+)
 create mode 100644 ports/libxcrypt/portfile.cmake
 create mode 100644 ports/libxcrypt/vcpkg.json
 create mode 100644 versions/l-/libxcrypt.json
2024-09-22 13:22:33,012 - 360 - WARNING - copy downloads/vcpkg/ports/aom -> ./ports/aom
2024-09-22 13:22:33,015 - 369 - WARNING - copy downloads/vcpkg/versions/a-/aom.json -> ./versions/a-/aom.json
2024-09-22 13:22:33,016 - 382 - INFO - aom
commit c591ac6466a55ef0a05a3d56bb1489ca36e50102
Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
Date:   2024-04-30 20:50:26 +0200

    [Qt] Update to 6.6.3 (#37731)

    Fixes https://github.com/microsoft/vcpkg/issues/37766

 ports/aom/portfile.cmake                           |   7 +
 ports/aom/vcpkg.json                               |   1 +
 ports/ffmpeg/portfile.cmake                        |  58 +++-
 ports/ffmpeg/vcpkg-cmake-wrapper.cmake             | 283 ++++++++++++++++++
 ports/ffmpeg/vcpkg.json                            |   2 +-
 ports/mp3lame/Config.cmake.in                      |  11 +-
 ports/mp3lame/vcpkg.json                           |   2 +-
 ports/opencv4/portfile.cmake                       |   3 +
 ports/opencv4/vcpkg.json                           |   2 +-
 ports/openh264/portfile.cmake                      |   7 +
 ports/openh264/vcpkg.json                          |   2 +-
 ports/pulseaudio/portfile.cmake                    |  95 ++++++
 ports/pulseaudio/vcpkg.json                        |  46 +++
 ports/qt/vcpkg.json                                |  13 +-
 ports/qt3d/vcpkg.json                              |   2 +-
 ports/qt5compat/vcpkg.json                         |   3 +-
 ports/qtactiveqt/vcpkg.json                        |   2 +-
 ports/qtapplicationmanager/vcpkg.json              |   2 +-
 ports/qtbase/allow_outside_prefix.patch            |   8 +-
 ports/qtbase/cmake/qt_install_submodule.cmake      |   3 +-
 ports/qtbase/cmake/qt_port_data.cmake              |  91 +++---
 ports/qtbase/cmake/qt_port_details.cmake           |   2 +-
 ports/qtbase/config_install.patch                  |   8 +-
 ports/qtbase/fix_cmake_build_type.patch            |  24 --
 .../patches/0001-CVE-2023-51714-qtbase-6.6.diff    |  36 ---
 .../patches/0002-CVE-2023-51714-qtbase-6.6.diff    |  44 ---
 .../qtbase/patches/CVE-2024-25580-qtbase-6.6.diff  | 325 ---------------------
 ports/qtbase/portfile.cmake                        |   6 -
 ports/qtbase/vcpkg.json                            |   3 +-
 ports/qtcharts/vcpkg.json                          |   3 +-
 ports/qtcoap/vcpkg.json                            |   3 +-
 ports/qtconnectivity/vcpkg.json                    |   3 +-
 ports/qtdatavis3d/vcpkg.json                       |   3 +-
 ports/qtdeclarative/vcpkg.json                     |   2 +-
 ports/qtdeviceutilities/vcpkg.json                 |   3 +-
 ports/qtdoc/vcpkg.json                             |   3 +-
 ports/qtgraphs/vcpkg.json                          |   3 +-
 ports/qtgrpc/vcpkg.json                            |   3 +-
 ports/qthttpserver/vcpkg.json                      |   3 +-
 ports/qtimageformats/vcpkg.json                    |   3 +-
 ports/qtinterfaceframework/vcpkg.json              |   3 +-
 ports/qtlanguageserver/vcpkg.json                  |   3 +-
 ports/qtlocation/vcpkg.json                        |   3 +-
 ports/qtlottie/vcpkg.json                          |   2 +-
 ports/qtmqtt/vcpkg.json                            |   3 +-
 ports/qtmultimedia/portfile.cmake                  |  32 +-
 ports/qtmultimedia/remove_export_macro.patch       | 182 ------------
 ports/qtmultimedia/remove_unistd.patch             |  24 --
 ports/qtmultimedia/static_find_modules.patch       |  54 ++--
 ports/qtmultimedia/vcpkg.json                      |  17 +-
 ports/qtnetworkauth/vcpkg.json                     |   3 +-
 ports/qtopcua/vcpkg.json                           |   3 +-
 ports/qtpositioning/vcpkg.json                     |   3 +-
 ports/qtquick3d/vcpkg.json                         |   3 +-
 ports/qtquick3dphysics/vcpkg.json                  |   3 +-
 ports/qtquickeffectmaker/vcpkg.json                |   3 +-
 ports/qtquicktimeline/vcpkg.json                   |   3 +-
 ports/qtremoteobjects/vcpkg.json                   |   3 +-
 ports/qtscxml/vcpkg.json                           |   3 +-
 ports/qtsensors/vcpkg.json                         |   3 +-
 ports/qtserialbus/vcpkg.json                       |   3 +-
 ports/qtserialport/vcpkg.json                      |   3 +-
 ports/qtshadertools/vcpkg.json                     |   3 +-
 ports/qtspeech/vcpkg.json                          |   3 +-
 ports/qtsvg/vcpkg.json                             |   3 +-
 ports/qttools/vcpkg.json                           |   3 +-
 ports/qttranslations/vcpkg.json                    |   3 +-
 ports/qtvirtualkeyboard/vcpkg.json                 |   2 +-
 ports/qtwayland/vcpkg.json                         |   2 +-
 ports/qtwebchannel/vcpkg.json                      |   3 +-
 ports/qtwebengine/msvc-template.patch              | 140 ---------
 ports/qtwebengine/portfile.cmake                   |   7 +-
 ports/qtwebengine/vcpkg.json                       |   3 +-
 ports/qtwebsockets/vcpkg.json                      |   3 +-
 ports/qtwebview/vcpkg.json                         |   3 +-
 ports/vtk/portfile.cmake                           |   8 +
 ports/vtk/vcpkg.json                               |   1 +
 versions/a-/aom.json                               |   5 +
 versions/baseline.json                             | 186 ++++++------
 versions/f-/ffmpeg.json                            |   5 +
 versions/m-/mp3lame.json                           |   5 +
 versions/o-/opencv4.json                           |   5 +
 versions/o-/openh264.json                          |   5 +
 versions/p-/pulseaudio.json                        |   9 +
 versions/q-/qt.json                                |   5 +
 versions/q-/qt3d.json                              |   5 +
 versions/q-/qt5compat.json                         |   5 +
 versions/q-/qtactiveqt.json                        |   5 +
 versions/q-/qtapplicationmanager.json              |   5 +
 versions/q-/qtbase.json                            |   5 +
 versions/q-/qtcharts.json                          |   5 +
 versions/q-/qtcoap.json                            |   5 +
 versions/q-/qtconnectivity.json                    |   5 +
 versions/q-/qtdatavis3d.json                       |   5 +
 versions/q-/qtdeclarative.json                     |   5 +
 versions/q-/qtdeviceutilities.json                 |   5 +
 versions/q-/qtdoc.json                             |   5 +
 versions/q-/qtgraphs.json                          |   5 +
 versions/q-/qtgrpc.json                            |   5 +
 versions/q-/qthttpserver.json                      |   5 +
 versions/q-/qtimageformats.json                    |   5 +
 versions/q-/qtinterfaceframework.json              |   5 +
 versions/q-/qtlanguageserver.json                  |   5 +
 versions/q-/qtlocation.json                        |   5 +
 versions/q-/qtlottie.json                          |   5 +
 versions/q-/qtmqtt.json                            |   5 +
 versions/q-/qtmultimedia.json                      |   5 +
 versions/q-/qtnetworkauth.json                     |   5 +
 versions/q-/qtopcua.json                           |   5 +
 versions/q-/qtpositioning.json                     |   5 +
 versions/q-/qtquick3d.json                         |   5 +
 versions/q-/qtquick3dphysics.json                  |   5 +
 versions/q-/qtquickeffectmaker.json                |   5 +
 versions/q-/qtquicktimeline.json                   |   5 +
 versions/q-/qtremoteobjects.json                   |   5 +
 versions/q-/qtscxml.json                           |   5 +
 versions/q-/qtsensors.json                         |   5 +
 versions/q-/qtserialbus.json                       |   5 +
 versions/q-/qtserialport.json                      |   5 +
 versions/q-/qtshadertools.json                     |   5 +
 versions/q-/qtspeech.json                          |   5 +
 versions/q-/qtsvg.json                             |   5 +
 versions/q-/qttools.json                           |   5 +
 versions/q-/qttranslations.json                    |   5 +
 versions/q-/qtvirtualkeyboard.json                 |   5 +
 versions/q-/qtwayland.json                         |   5 +
 versions/q-/qtwebchannel.json                      |   5 +
 versions/q-/qtwebengine.json                       |   5 +
 versions/q-/qtwebsockets.json                      |   5 +
 versions/q-/qtwebview.json                         |   5 +
 versions/v-/vtk.json                               |   5 +
 131 files changed, 1044 insertions(+), 1080 deletions(-)

2024-09-22 13:22:33,017 - 147 - INFO - run: git add .
2024-09-22 13:22:33,041 - 147 - INFO - run: git commit -m [Qt] Update to 6.6.3 (#37731) --author Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
[main d48c9bd71] [Qt] Update to 6.6.3 (#37731)
 Author: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
 6 files changed, 220 insertions(+)
 create mode 100644 ports/aom/aom-rename-static.diff
 create mode 100644 ports/aom/aom-uninitialized-pointer.diff
 create mode 100644 ports/aom/export-config.diff
 create mode 100644 ports/aom/portfile.cmake
 create mode 100644 ports/aom/vcpkg.json
 create mode 100644 versions/a-/aom.json
2024-09-22 13:22:33,110 - 360 - WARNING - copy downloads/vcpkg/ports/libwebp -> ./ports/libwebp
2024-09-22 13:22:33,113 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libwebp.json -> ./versions/l-/libwebp.json
2024-09-22 13:22:33,114 - 382 - INFO - libwebp
commit 3a882b3efc01c0e3118b54ca51eff57205117b55
Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
Date:   2024-05-02 04:40:19 +0200

    [many ports] Don't depend on default features of tiff (#38049)

    This removes the transitive dependency of liblzma via tiff

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [x] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [x] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [x] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    ---------

    Co-authored-by: Alexander Neumann <30894796+Neumann-A@users.noreply.github.com>
    Co-authored-by: Alexander Neumann <you@example.com>
    Co-authored-by: Billy Robert O'Neal III <bion@microsoft.com>

 ports/dcmtk/vcpkg.json            |  7 ++++--
 ports/devil/vcpkg.json            |  7 ++++--
 ports/graphicsmagick/vcpkg.json   |  6 ++++-
 ports/itk/vcpkg.json              |  6 ++++-
 ports/libgd/vcpkg.json            |  7 ++++--
 ports/libgxps/vcpkg.json          |  7 ++++--
 ports/libwebp/vcpkg.json          | 26 ++++++++++++++++----
 ports/mapnik/vcpkg.json           |  7 ++++--
 ports/opencv2/vcpkg.json          |  7 ++++--
 ports/opencv3/vcpkg.json          |  7 ++++--
 ports/opencv4/vcpkg.json          |  7 ++++--
 ports/openimageio/vcpkg.json      |  7 ++++--
 ports/openjpeg/vcpkg.json         |  6 ++++-
 ports/openmvg/vcpkg.json          |  7 ++++--
 ports/openmvs/vcpkg.json          |  7 ++++--
 ports/openslide/vcpkg.json        |  7 ++++--
 ports/pangolin/vcpkg.json         |  7 ++++--
 ports/poppler/vcpkg.json          |  6 ++++-
 ports/qt5-imageformats/vcpkg.json |  7 ++++--
 ports/qtimageformats/vcpkg.json   |  6 ++++-
 ports/sail/vcpkg.json             |  6 ++++-
 ports/sdl2-image/vcpkg.json       |  7 ++++--
 ports/selene/vcpkg.json           |  7 ++++--
 ports/vtk/vcpkg.json              |  7 ++++--
 ports/vxl/vcpkg.json              |  7 ++++--
 ports/wxwidgets/vcpkg.json        |  7 ++++--
 versions/baseline.json            | 52 +++++++++++++++++++--------------------
 versions/d-/dcmtk.json            |  5 ++++
 versions/d-/devil.json            |  5 ++++
 versions/g-/graphicsmagick.json   |  5 ++++
 versions/i-/itk.json              |  5 ++++
 versions/l-/libgd.json            |  5 ++++
 versions/l-/libgxps.json          |  5 ++++
 versions/l-/libwebp.json          |  5 ++++
 versions/m-/mapnik.json           |  5 ++++
 versions/o-/opencv2.json          |  5 ++++
 versions/o-/opencv3.json          |  5 ++++
 versions/o-/opencv4.json          |  5 ++++
 versions/o-/openimageio.json      |  5 ++++
 versions/o-/openjpeg.json         |  5 ++++
 versions/o-/openmvg.json          |  5 ++++
 versions/o-/openmvs.json          |  5 ++++
 versions/o-/openslide.json        |  5 ++++
 versions/p-/pangolin.json         |  5 ++++
 versions/p-/poppler.json          |  5 ++++
 versions/q-/qt5-imageformats.json |  5 ++++
 versions/q-/qtimageformats.json   |  5 ++++
 versions/s-/sail.json             |  5 ++++
 versions/s-/sdl2-image.json       |  5 ++++
 versions/s-/selene.json           |  5 ++++
 versions/v-/vtk.json              |  5 ++++
 versions/v-/vxl.json              |  5 ++++
 versions/w-/wxwidgets.json        |  5 ++++
 53 files changed, 302 insertions(+), 75 deletions(-)

2024-09-22 13:22:33,114 - 147 - INFO - run: git add .
2024-09-22 13:22:33,137 - 147 - INFO - run: git commit -m [many ports] Don't depend on default features of tiff (#38049) --author Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
[main c9d275e26] [many ports] Don't depend on default features of tiff (#38049)
 Author: Thomas1664 <46387399+Thomas1664@users.noreply.github.com>
 7 files changed, 552 insertions(+)
 create mode 100644 ports/libwebp/0002-cmake-config.patch
 create mode 100644 ports/libwebp/0003-simd.patch
 create mode 100644 ports/libwebp/0008-sdl.patch
 create mode 100644 ports/libwebp/portfile.cmake
 create mode 100644 ports/libwebp/usage
 create mode 100644 ports/libwebp/vcpkg.json
 create mode 100644 versions/l-/libwebp.json
2024-09-22 13:22:33,219 - 360 - WARNING - copy downloads/vcpkg/ports/nghttp2 -> ./ports/nghttp2
2024-09-22 13:22:33,220 - 369 - WARNING - copy downloads/vcpkg/versions/n-/nghttp2.json -> ./versions/n-/nghttp2.json
2024-09-22 13:22:33,220 - 382 - INFO - nghttp2
commit a9ba76585964e9fc4079c8475b2b957fb38b6ba4
Author: Alexis La Goutte <alexis.lagoutte@gmail.com>
Date:   2024-05-25 04:19:35 +0200

    [nghttp2] update to 1.62.1 (#38857)

 ports/nghttp2/portfile.cmake | 2 +-
 ports/nghttp2/vcpkg.json     | 2 +-
 versions/baseline.json       | 2 +-
 versions/n-/nghttp2.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:33,222 - 147 - INFO - run: git add .
2024-09-22 13:22:33,244 - 147 - INFO - run: git commit -m [nghttp2] update to 1.62.1 (#38857) --author Alexis La Goutte <alexis.lagoutte@gmail.com>
[main e9a831480] [nghttp2] update to 1.62.1 (#38857)
 Author: Alexis La Goutte <alexis.lagoutte@gmail.com>
 3 files changed, 230 insertions(+)
 create mode 100644 ports/nghttp2/portfile.cmake
 create mode 100644 ports/nghttp2/vcpkg.json
 create mode 100644 versions/n-/nghttp2.json
2024-09-22 13:22:33,306 - 360 - WARNING - copy downloads/vcpkg/ports/pixman -> ./ports/pixman
2024-09-22 13:22:33,308 - 369 - WARNING - copy downloads/vcpkg/versions/p-/pixman.json -> ./versions/p-/pixman.json
2024-09-22 13:22:33,309 - 382 - INFO - pixman
commit f62d0f19c19e4d03782842a28333f94db8c0a11e
Author: Flole <Flole998@users.noreply.github.com>
Date:   2024-06-04 07:17:32 +0200

    [pixman] Fix x86 builds not using MSVC (#38851)

    Fixes the `#Todo` comment in pixman's portfile.cmale

 ports/pixman/portfile.cmake | 8 ++++++--
 ports/pixman/vcpkg.json     | 1 +
 versions/baseline.json      | 2 +-
 versions/p-/pixman.json     | 5 +++++
 4 files changed, 13 insertions(+), 3 deletions(-)

2024-09-22 13:22:33,309 - 147 - INFO - run: git add .
2024-09-22 13:22:33,331 - 147 - INFO - run: git commit -m [pixman] Fix x86 builds not using MSVC (#38851) --author Flole <Flole998@users.noreply.github.com>
[main fd42f9308] [pixman] Fix x86 builds not using MSVC (#38851)
 Author: Flole <Flole998@users.noreply.github.com>
 6 files changed, 358 insertions(+)
 create mode 100644 ports/pixman/fix_clang-cl.patch
 create mode 100644 ports/pixman/missing_intrin_include.patch
 create mode 100644 ports/pixman/no-host-cpu-checks.patch
 create mode 100644 ports/pixman/portfile.cmake
 create mode 100644 ports/pixman/vcpkg.json
 create mode 100644 versions/p-/pixman.json
2024-09-22 13:22:33,393 - 360 - WARNING - copy downloads/vcpkg/ports/libvorbis -> ./ports/libvorbis
2024-09-22 13:22:33,395 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libvorbis.json -> ./versions/l-/libvorbis.json
2024-09-22 13:22:33,396 - 382 - INFO - libvorbis
commit cec6b3798e3e32d12d1f2dbbeebeb0c7fabfcbf1
Author: Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
Date:   2024-06-04 07:40:39 +0200

    [libvorbis] Fix libogg find_package (#39067)

    - [x] Changes comply with the [maintainer
    guide](https://github.com/microsoft/vcpkg-docs/blob/main/vcpkg/contributing/maintainer-guide.md).
    - [x] SHA512s are updated for each updated download.
    - [ ] The "supports" clause reflects platforms that may be fixed by this
    new version.
    - [ ] Any fixed [CI
    baseline](https://github.com/microsoft/vcpkg/blob/master/scripts/ci.baseline.txt)
    entries are removed from that file.
    - [ ] Any patches that are no longer applied are deleted from the port's
    directory.
    - [x] The version database is fixed by rerunning `./vcpkg x-add-version
    --all` and committing the result.
    - [x] Only one version is added to each modified port's versions file.

    ---

    Fix Ogg find_package.

    Libogg now ships with an `OggConfig.cmake` file and the current way to
    find it does not work anymore.
    All the patch does adds the CONFIG notation to the find_package
    function.

    ---

    Repro case:

    1. Add this to your own `vcpkg.json`
    ```json
    {
      "name": "test",
      "version": "0.0.1",
      "dependencies": [
        {
          "name": "ffmpeg",
          "default-features": false,
          "features": [
            "vorbis"
          ],
          "platform": "windows"
        }
      ]
    }
    ```

    2. Add this line to your own `CMakeLists.txt`
    ```cmake
    find_package(FFmpeg COMPONENTS AVFORMAT AVUTIL AVCODEC SWRESAMPLE)
    ```

    3. See CMake failing with an error similar to this one:
    ```
    CMake Error at REDACTED/vcpkg_installed/x86-windows-static/share/Vorbis/VorbisTargets.cmake:60 (set_target_properties):
      The link interface of target "Vorbis::vorbis" contains:

        Ogg::ogg

      but the target was not found.  Possible reasons include:

        * There is a typo in the target name.
        * A find_package call is missing for an IMPORTED target.
        * An ALIAS target is missing.

    Call Stack (most recent call first):
      REDACTED/vcpkg_installed/x86-windows-static/share/Vorbis/VorbisConfig.cmake:30 (include)
      C:/vcpkg/scripts/buildsystems/vcpkg.cmake:859 (_find_package)
      REDACTED/vcpkg_installed/x86-windows-static/share/ffmpeg/vcpkg-cmake-wrapper.cmake:190 (find_package)
      C:/vcpkg/scripts/buildsystems/vcpkg.cmake:813 (include)
      CMakeLists.txt:1 (find_package)
    ```

    ---------

    Co-authored-by: Kai Pastor <dg0yt@darc.de>

 ports/libvorbis/0004-ogg-find-dependency.patch | 13 +++++++++++++
 ports/libvorbis/portfile.cmake                 |  1 +
 ports/libvorbis/vcpkg.json                     |  2 +-
 versions/baseline.json                         |  2 +-
 versions/l-/libvorbis.json                     |  5 +++++
 5 files changed, 21 insertions(+), 2 deletions(-)

2024-09-22 13:22:33,396 - 147 - INFO - run: git add .
2024-09-22 13:22:33,419 - 147 - INFO - run: git commit -m [libvorbis] Fix libogg find_package (#39067) --author Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
[main 0c096cccc] [libvorbis] Fix libogg find_package (#39067)
 Author: Julian Xhokaxhiu <julianxhokaxhiu@users.noreply.github.com>
 8 files changed, 214 insertions(+)
 create mode 100644 ports/libvorbis/0001-Dont-export-vorbisenc-functions.patch
 create mode 100644 ports/libvorbis/0002-Fixup-pkgconfig-libs.patch
 create mode 100644 ports/libvorbis/0003-def-mingw-compat.patch
 create mode 100644 ports/libvorbis/0004-ogg-find-dependency.patch
 create mode 100644 ports/libvorbis/portfile.cmake
 create mode 100644 ports/libvorbis/usage
 create mode 100644 ports/libvorbis/vcpkg.json
 create mode 100644 versions/l-/libvorbis.json
2024-09-22 13:22:33,484 - 360 - WARNING - copy downloads/vcpkg/ports/alsa -> ./ports/alsa
2024-09-22 13:22:33,486 - 369 - WARNING - copy downloads/vcpkg/versions/a-/alsa.json -> ./versions/a-/alsa.json
2024-09-22 13:22:33,486 - 382 - INFO - alsa
commit 2017886818a9a88d303548b53709f5ef922efb39
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-06-06 09:48:31 +0200

    [alsa,fdk-aac,ffmpeg,libsrt,snappy,x265] Code cleanup, fix and use pkg-config (#39077)

    - Setup and use pkg-config for ffmpeg dependencies.
    https://github.com/microsoft/vcpkg/pull/38011#discussion_r1623174355.
    - Export actual c++ link libraries for fdk-aac via pkg-config. (Same
    pattern as lerc, geos.)
    - Rectify link libraries in pkg-config  for alsa, libsrt, snappy, x265.
    - Burn-in dllimport for libsrt and x265.
    - Pass detected STRIP to ffmpeg. Fixes
    https://github.com/microsoft/vcpkg/issues/36852.

 ports/alsa/libdl.diff                              | 12 +++++
 ports/alsa/portfile.cmake                          |  1 +
 ports/alsa/vcpkg.json                              |  2 +-
 ports/fdk-aac/cxx-linkage-pkgconfig.patch          | 20 ++++++++
 ports/fdk-aac/portfile.cmake                       | 21 +++++---
 ports/fdk-aac/vcpkg.json                           |  2 +-
 ...taticFeatures.patch => 0004-dependencies.patch} | 47 ++++++++++--------
 ports/ffmpeg/0004-fix-debug-build.patch            | 40 ---------------
 ports/ffmpeg/0007-fix-lib-naming.patch             |  6 +--
 ports/ffmpeg/0009-Fix-fdk-detection.patch          | 14 ------
 ports/ffmpeg/0011-Fix-x265-detection.patch         | 15 ------
 ports/ffmpeg/0015-Fix-xml2-detection.patch         | 17 -------
 ports/ffmpeg/0022-fix-iconv.patch                  | 14 ------
 ports/ffmpeg/0023-fix-qsv-init.patch               | 22 --------
 ports/ffmpeg/portfile.cmake                        | 34 ++++++++-----
 ports/ffmpeg/vcpkg.json                            |  2 +-
 ports/libsrt/fix-dependency-install.patch          | 39 ---------------
 ports/libsrt/pkgconfig.diff                        | 16 ++++++
 ports/libsrt/portfile.cmake                        | 30 ++++++++---
 ports/libsrt/vcpkg.json                            |  1 +
 ports/snappy/pkgconfig.diff                        | 23 +++++++++
 ports/snappy/portfile.cmake                        | 18 ++-----
 ports/snappy/snappy.pc.in                          | 11 ++--
 ports/snappy/vcpkg.json                            |  1 +
 ports/x265/disable-install-pdb.patch               | 35 +++++--------
 ports/x265/linkage.diff                            | 18 +++++++
 ports/x265/pkgconfig.diff                          | 58 ++++++++++++++++++++++
 ports/x265/portfile.cmake                          | 32 +++---------
 ports/x265/vcpkg.json                              |  1 +
 versions/a-/alsa.json                              |  5 ++
 versions/baseline.json                             | 12 ++---
 versions/f-/fdk-aac.json                           |  5 ++
 versions/f-/ffmpeg.json                            |  5 ++
 versions/l-/libsrt.json                            |  5 ++
 versions/s-/snappy.json                            |  5 ++
 versions/x-/x265.json                              |  5 ++
 36 files changed, 304 insertions(+), 290 deletions(-)

2024-09-22 13:22:33,487 - 147 - INFO - run: git add .
2024-09-22 13:22:33,509 - 147 - INFO - run: git commit -m [alsa,fdk-aac,ffmpeg,libsrt,snappy,x265] Code cleanup, fix and use pkg-config (#39077) --author Kai Pastor <dg0yt@darc.de>
[main c2bf68b2d] [alsa,fdk-aac,ffmpeg,libsrt,snappy,x265] Code cleanup, fix and use pkg-config (#39077)
 Author: Kai Pastor <dg0yt@darc.de>
 7 files changed, 292 insertions(+)
 create mode 100644 ports/alsa/fix-plugin-dir.patch
 create mode 100644 ports/alsa/libdl.diff
 create mode 100644 ports/alsa/portfile.cmake
 create mode 100644 ports/alsa/usage
 create mode 100644 ports/alsa/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/alsa/vcpkg.json
 create mode 100644 versions/a-/alsa.json
2024-09-22 13:22:33,591 - 360 - WARNING - copy downloads/vcpkg/ports/curl -> ./ports/curl
2024-09-22 13:22:33,596 - 369 - WARNING - copy downloads/vcpkg/versions/c-/curl.json -> ./versions/c-/curl.json
2024-09-22 13:22:33,596 - 382 - INFO - curl
commit 795f2f137e6cf6d985fcc927bffcaf9c0a96e4ac
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-06-11 02:26:53 +0200

    [libpsl,curl,vcpkg-ci-curl] Update suffix list, fix and test curl (#38847)

 ports/curl/0002_fix_uwp.patch               | 24 --------
 ports/curl/0012-fix-dependency-idn2.patch   | 21 -------
 ports/curl/cmake-project-include.cmake      |  4 ++
 ports/curl/dependencies.patch               | 89 +++++++++++++++++++++++------
 ports/curl/mbedtls-ws2_32.patch             | 14 -----
 ports/curl/portfile.cmake                   |  3 -
 ports/curl/vcpkg.json                       |  1 +
 ports/libpsl/portfile.cmake                 | 22 ++++---
 ports/libpsl/vcpkg.json                     |  3 +-
 scripts/test_ports/vcpkg-ci-curl/vcpkg.json |  7 +++
 versions/baseline.json                      |  4 +-
 versions/c-/curl.json                       |  5 ++
 versions/l-/libpsl.json                     |  5 ++
 13 files changed, 111 insertions(+), 91 deletions(-)

2024-09-22 13:22:33,596 - 147 - INFO - run: git add .
2024-09-22 13:22:33,619 - 147 - INFO - run: git commit -m [libpsl,curl,vcpkg-ci-curl] Update suffix list, fix and test curl (#38847) --author Kai Pastor <dg0yt@darc.de>
[main 7d567ab5e] [libpsl,curl,vcpkg-ci-curl] Update suffix list, fix and test curl (#38847)
 Author: Kai Pastor <dg0yt@darc.de>
 12 files changed, 1359 insertions(+)
 create mode 100644 ports/curl/0005_remove_imp_suffix.patch
 create mode 100644 ports/curl/0020-fix-pc-file.patch
 create mode 100644 ports/curl/0022-deduplicate-libs.patch
 create mode 100644 ports/curl/cmake-config.patch
 create mode 100644 ports/curl/cmake-project-include.cmake
 create mode 100644 ports/curl/dependencies.patch
 create mode 100644 ports/curl/export-components.patch
 create mode 100644 ports/curl/portfile.cmake
 create mode 100644 ports/curl/usage
 create mode 100644 ports/curl/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/curl/vcpkg.json
 create mode 100644 versions/c-/curl.json
2024-09-22 13:22:33,683 - 360 - WARNING - copy downloads/vcpkg/ports/leptonica -> ./ports/leptonica
2024-09-22 13:22:33,684 - 369 - WARNING - copy downloads/vcpkg/versions/l-/leptonica.json -> ./versions/l-/leptonica.json
2024-09-22 13:22:33,685 - 382 - INFO - leptonica
commit bc98892fd1e238d4af141da5ed4042f1115c7d98
Author: hesmar <hess@3dvisionlabs.com>
Date:   2024-06-11 21:17:24 +0200

    [leptonica] Reduce required C standard (#39203)

 ports/leptonica/portfile.cmake | 11 +++++++++--
 ports/leptonica/vcpkg.json     |  1 +
 versions/baseline.json         |  2 +-
 versions/l-/leptonica.json     |  5 +++++
 4 files changed, 16 insertions(+), 3 deletions(-)

2024-09-22 13:22:33,685 - 147 - INFO - run: git add .
2024-09-22 13:22:33,707 - 147 - INFO - run: git commit -m [leptonica] Reduce required C standard (#39203) --author hesmar <hess@3dvisionlabs.com>
[main b4fe7d0e7] [leptonica] Reduce required C standard (#39203)
 Author: hesmar <hess@3dvisionlabs.com>
 4 files changed, 233 insertions(+)
 create mode 100644 ports/leptonica/fix-pc-and-config.patch
 create mode 100644 ports/leptonica/portfile.cmake
 create mode 100644 ports/leptonica/vcpkg.json
 create mode 100644 versions/l-/leptonica.json
2024-09-22 13:22:33,832 - 360 - WARNING - copy downloads/vcpkg/ports/snappy -> ./ports/snappy
2024-09-22 13:22:33,836 - 369 - WARNING - copy downloads/vcpkg/versions/s-/snappy.json -> ./versions/s-/snappy.json
2024-09-22 13:22:33,837 - 382 - INFO - snappy
commit 76fc2c5f4bd1b225203bcb615ae1e5c1aacc5999
Author: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
Date:   2024-06-18 11:57:51 -0700

    [snappy] Update to 1.2.1 (#39331)

 ports/snappy/portfile.cmake | 2 +-
 ports/snappy/vcpkg.json     | 3 +--
 versions/baseline.json      | 4 ++--
 versions/s-/snappy.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:22:33,837 - 147 - INFO - run: git add .
2024-09-22 13:22:33,860 - 147 - INFO - run: git commit -m [snappy] Update to 1.2.1 (#39331) --author Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
[main 9972b2056] [snappy] Update to 1.2.1 (#39331)
 Author: Cheney Wang <38240633+Cheney-W@users.noreply.github.com>
 8 files changed, 214 insertions(+)
 create mode 100644 ports/snappy/fix_clang-cl_build.patch
 create mode 100644 ports/snappy/no-werror.patch
 create mode 100644 ports/snappy/pkgconfig.diff
 create mode 100644 ports/snappy/portfile.cmake
 create mode 100644 ports/snappy/snappy.pc.in
 create mode 100644 ports/snappy/usage
 create mode 100644 ports/snappy/vcpkg.json
 create mode 100644 versions/s-/snappy.json
2024-09-22 13:22:33,962 - 360 - WARNING - copy downloads/vcpkg/ports/ffmpeg -> ./ports/ffmpeg
2024-09-22 13:22:33,967 - 369 - WARNING - copy downloads/vcpkg/versions/f-/ffmpeg.json -> ./versions/f-/ffmpeg.json
2024-09-22 13:22:33,968 - 382 - INFO - ffmpeg
commit 6db51d86a9c2796581d74c9a7eb46e52ee8cb7eb
Author: gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
Date:   2024-06-20 07:07:05 +1000

    [vcpkg_replace_string] warn unchanged by call (#34719)

    If a call to `vcpkg_replace_string` makes no changes i.e doesn't
    effectively replace a string, A warning is logged.

    This should also help identify ports that no longer need these calls to
    fix things in `.pc` files etc.

 ports/activemq-cpp/portfile.cmake                  |   2 +-
 ports/activemq-cpp/vcpkg.json                      |   2 +-
 ports/apr/portfile.cmake                           |   8 +-
 ports/apr/vcpkg.json                               |   1 +
 ports/armadillo/portfile.cmake                     |   6 +-
 ports/armadillo/vcpkg.json                         |   1 +
 ports/assimp/portfile.cmake                        |   2 +-
 ports/assimp/vcpkg.json                            |   1 +
 ports/aws-sdk-cpp/portfile.cmake                   |   4 +-
 ports/aws-sdk-cpp/vcpkg.json                       |   2 +-
 ports/blitz/portfile.cmake                         |   8 +-
 ports/blitz/vcpkg.json                             |   2 +-
 ports/botan/portfile.cmake                         |   4 +-
 ports/botan/vcpkg.json                             |   1 +
 ports/ccfits/portfile.cmake                        |   2 +-
 ports/ccfits/vcpkg.json                            |   2 +-
 ports/cfitsio/portfile.cmake                       |   1 +
 ports/cfitsio/vcpkg.json                           |   2 +-
 ports/curl/portfile.cmake                          |   8 +-
 ports/curl/vcpkg.json                              |   2 +-
 ports/dcmtk/portfile.cmake                         |   8 +-
 ports/dcmtk/vcpkg.json                             |   2 +-
 ports/duktape/portfile.cmake                       |   6 +-
 ports/duktape/vcpkg.json                           |   2 +-
 ports/easyhook/portfile.cmake                      |   2 +
 ports/easyhook/vcpkg.json                          |   2 +-
 ports/fbthrift/portfile.cmake                      |   2 +-
 ports/fbthrift/vcpkg.json                          |   1 +
 ports/ffmpeg/portfile.cmake                        |   4 +-
 ports/ffmpeg/vcpkg.json                            |   2 +-
 ports/fontconfig/portfile.cmake                    |  10 +-
 ports/fontconfig/vcpkg.json                        |   2 +-
 ports/freeglut/portfile.cmake                      |   4 +-
 ports/freeglut/vcpkg.json                          |   2 +-
 ports/freerdp/portfile.cmake                       |   6 +-
 ports/freerdp/vcpkg.json                           |   2 +-
 ports/geogram/portfile.cmake                       |   3 +-
 ports/geogram/vcpkg.json                           |   2 +-
 ports/gettext/portfile.cmake                       |   2 +-
 ports/gettext/vcpkg.json                           |   1 +
 ports/glib/portfile.cmake                          |   6 +-
 ports/glib/vcpkg.json                              |   2 +-
 ports/graphqlparser/portfile.cmake                 |   2 +-
 ports/graphqlparser/vcpkg.json                     |   2 +-
 ports/graphviz/portfile.cmake                      |   2 +-
 ports/graphviz/vcpkg.json                          |   2 +-
 ports/guile/portfile.cmake                         |   4 +-
 ports/guile/vcpkg.json                             |   1 +
 ports/gz-common5/portfile.cmake                    |   3 +-
 ports/gz-common5/vcpkg.json                        |   2 +-
 ports/hayai/portfile.cmake                         |   2 +
 ports/hayai/vcpkg.json                             |   2 +-
 ports/hdf5/portfile.cmake                          |   6 +-
 ports/hdf5/vcpkg.json                              |   1 +
 ports/hidapi/portfile.cmake                        |   2 +-
 ports/hidapi/vcpkg.json                            |   1 +
 ports/hpx/portfile.cmake                           |   2 +-
 ports/hpx/vcpkg.json                               |   1 +
 ports/hwloc/portfile.cmake                         |   4 +-
 ports/hwloc/vcpkg.json                             |   1 +
 ports/icu/portfile.cmake                           |   2 +-
 ports/icu/vcpkg.json                               |   2 +-
 ports/intel-mkl/portfile.cmake                     |   4 +-
 ports/intel-mkl/vcpkg.json                         |   2 +-
 ports/libevent/portfile.cmake                      |   1 +
 ports/libevent/vcpkg.json                          |   1 +
 ports/libgeotiff/portfile.cmake                    |   1 -
 ports/libgeotiff/vcpkg.json                        |   1 +
 ports/libheif/portfile.cmake                       |   4 +-
 ports/libheif/vcpkg.json                           |   2 +-
 ports/libjpeg-turbo/portfile.cmake                 |   8 +-
 ports/libjpeg-turbo/vcpkg.json                     |   1 +
 ports/libsigcpp/portfile.cmake                     |   2 +-
 ports/libsigcpp/vcpkg.json                         |   1 +
 ports/libspatialite/portfile.cmake                 |   2 +-
 ports/libspatialite/vcpkg.json                     |   2 +-
 ports/libssh/portfile.cmake                        |   4 +-
 ports/libssh/vcpkg.json                            |   2 +-
 ports/libssh2/portfile.cmake                       |   4 +-
 ports/libssh2/vcpkg.json                           |   2 +-
 ports/libwebsockets/portfile.cmake                 |   4 +-
 ports/libwebsockets/vcpkg.json                     |   1 +
 ports/libxslt/portfile.cmake                       |   2 +-
 ports/libxslt/vcpkg.json                           |   2 +-
 ports/mathgl/portfile.cmake                        |   4 +-
 ports/mathgl/vcpkg.json                            |   2 +-
 ports/mimalloc/portfile.cmake                      |   4 +-
 ports/mimalloc/vcpkg.json                          |   2 +-
 ports/minizip/portfile.cmake                       |   2 +-
 ports/minizip/vcpkg.json                           |   1 +
 ports/monkeys-audio/portfile.cmake                 |   2 +
 ports/monkeys-audio/vcpkg.json                     |   2 +-
 ports/nanomsg/portfile.cmake                       |   1 +
 ports/nanomsg/vcpkg.json                           |   2 +-
 ports/nlohmann-json/portfile.cmake                 |   1 +
 ports/nlohmann-json/vcpkg.json                     |   1 +
 ports/ogre/portfile.cmake                          |   6 +-
 ports/ogre/vcpkg.json                              |   1 +
 ports/omniorb/portfile.cmake                       |   4 +-
 ports/omniorb/vcpkg.json                           |   2 +-
 ports/ompl/portfile.cmake                          |   2 +-
 ports/ompl/vcpkg.json                              |   1 +
 ports/opencv3/portfile.cmake                       |   5 +-
 ports/opencv3/vcpkg.json                           |   2 +-
 ports/opencv4/portfile.cmake                       |   1 +
 ports/opencv4/vcpkg.json                           |   2 +-
 ports/paraview/portfile.cmake                      |   3 +-
 ports/paraview/vcpkg.json                          |   1 +
 ports/pipewire/portfile.cmake                      |   4 +-
 ports/pipewire/vcpkg.json                          |   1 +
 ports/protobuf/portfile.cmake                      |   1 +
 ports/protobuf/vcpkg.json                          |   2 +-
 ports/python3/portfile.cmake                       |   2 +-
 ports/python3/vcpkg.json                           |   2 +-
 ports/qpid-proton/portfile.cmake                   |   2 +-
 ports/qpid-proton/vcpkg.json                       |   2 +-
 ports/qt5-base/cmake/qt_fix_makefile_install.cmake |   2 +-
 ports/qt5-base/vcpkg.json                          |   1 +
 ports/qtapplicationmanager/portfile.cmake          |   2 +-
 ports/qtapplicationmanager/vcpkg.json              |   1 +
 ports/qtbase/cmake/qt_install_submodule.cmake      |   7 +-
 ports/qtbase/portfile.cmake                        |   3 +-
 ports/qtbase/vcpkg.json                            |   1 +
 ports/qtinterfaceframework/portfile.cmake          |   2 +-
 ports/qtinterfaceframework/vcpkg.json              |   1 +
 ports/qtmultimedia/portfile.cmake                  |   2 +-
 ports/qtmultimedia/vcpkg.json                      |   1 +
 ports/ryml/portfile.cmake                          |   2 +-
 ports/ryml/vcpkg.json                              |   1 +
 ports/sail/portfile.cmake                          |   4 +-
 ports/sail/vcpkg.json                              |   1 +
 ports/sdl2/portfile.cmake                          |   8 +-
 ports/sdl2/vcpkg.json                              |   1 +
 ports/shiftmedia-libgcrypt/portfile.cmake          |   2 +
 ports/shiftmedia-libgcrypt/vcpkg.json              |   1 +
 ports/shiftmedia-libgnutls/portfile.cmake          |   2 +
 ports/shiftmedia-libgnutls/vcpkg.json              |   2 +-
 ports/skia/portfile.cmake                          |   2 +-
 ports/skia/vcpkg.json                              |   1 +
 ports/sockpp/portfile.cmake                        |   2 +-
 ports/sockpp/vcpkg.json                            |   1 +
 ports/stxxl/portfile.cmake                         |   1 +
 ports/stxxl/vcpkg.json                             |   2 +-
 ports/symengine/portfile.cmake                     |   1 +
 ports/symengine/vcpkg.json                         |   2 +-
 ports/taglib/portfile.cmake                        |   4 +-
 ports/taglib/vcpkg.json                            |   2 +-
 ports/uthenticode/portfile.cmake                   |   5 -
 ports/uthenticode/vcpkg.json                       |   1 +
 ports/vcpkg-qmake/vcpkg.json                       |   2 +-
 .../vcpkg-qmake/z_vcpkg_qmake_fix_makefiles.cmake  |   3 +-
 ports/vcpkg-tool-meson/vcpkg.json                  |   2 +-
 ports/vcpkg-tool-meson/vcpkg_install_meson.cmake   |   2 +-
 ports/vtk/portfile.cmake                           |   2 +-
 ports/vtk/vcpkg.json                               |   1 +
 ports/wxwidgets/portfile.cmake                     |   4 +-
 ports/wxwidgets/vcpkg.json                         |   1 +
 ports/x264/portfile.cmake                          |   2 +-
 ports/x264/vcpkg.json                              |   1 +
 ports/xcb/portfile.cmake                           |   4 +-
 ports/xcb/vcpkg.json                               |   2 +-
 ports/xmlsec/portfile.cmake                        |   1 +
 ports/xmlsec/vcpkg.json                            |   1 +
 ports/zfp/portfile.cmake                           |   2 +-
 ports/zfp/vcpkg.json                               |   2 +-
 ports/zopfli/portfile.cmake                        |   4 +
 ports/zopfli/vcpkg.json                            |   2 +-
 scripts/cmake/vcpkg_install_meson.cmake            |   2 +-
 scripts/cmake/vcpkg_replace_string.cmake           |  17 ++-
 versions/a-/activemq-cpp.json                      |   5 +
 versions/a-/apr.json                               |   5 +
 versions/a-/armadillo.json                         |   5 +
 versions/a-/assimp.json                            |   5 +
 versions/a-/aws-sdk-cpp.json                       |   5 +
 versions/b-/blitz.json                             |   5 +
 versions/b-/botan.json                             |   5 +
 versions/baseline.json                             | 166 ++++++++++-----------
 versions/c-/ccfits.json                            |   5 +
 versions/c-/cfitsio.json                           |   5 +
 versions/c-/curl.json                              |   5 +
 versions/d-/dcmtk.json                             |   5 +
 versions/d-/duktape.json                           |   5 +
 versions/e-/easyhook.json                          |   5 +
 versions/f-/fbthrift.json                          |   5 +
 versions/f-/ffmpeg.json                            |   5 +
 versions/f-/fontconfig.json                        |   5 +
 versions/f-/freeglut.json                          |   5 +
 versions/f-/freerdp.json                           |   5 +
 versions/g-/geogram.json                           |   5 +
 versions/g-/gettext.json                           |   5 +
 versions/g-/glib.json                              |   5 +
 versions/g-/graphqlparser.json                     |   5 +
 versions/g-/graphviz.json                          |   5 +
 versions/g-/guile.json                             |   5 +
 versions/g-/gz-common5.json                        |   5 +
 versions/h-/hayai.json                             |   5 +
 versions/h-/hdf5.json                              |   5 +
 versions/h-/hidapi.json                            |   5 +
 versions/h-/hpx.json                               |   5 +
 versions/h-/hwloc.json                             |   5 +
 versions/i-/icu.json                               |   5 +
 versions/i-/intel-mkl.json                         |   5 +
 versions/l-/libevent.json                          |   5 +
 versions/l-/libgeotiff.json                        |   5 +
 versions/l-/libheif.json                           |   5 +
 versions/l-/libjpeg-turbo.json                     |   5 +
 versions/l-/libsigcpp.json                         |   5 +
 versions/l-/libspatialite.json                     |   5 +
 versions/l-/libssh.json                            |   5 +
 versions/l-/libssh2.json                           |   5 +
 versions/l-/libwebsockets.json                     |   5 +
 versions/l-/libxslt.json                           |   5 +
 versions/m-/mathgl.json                            |   5 +
 versions/m-/mimalloc.json                          |   5 +
 versions/m-/minizip.json                           |   5 +
 versions/m-/monkeys-audio.json                     |   5 +
 versions/n-/nanomsg.json                           |   5 +
 versions/n-/nlohmann-json.json                     |   5 +
 versions/o-/ogre.json                              |   5 +
 versions/o-/omniorb.json                           |   5 +
 versions/o-/ompl.json                              |   5 +
 versions/o-/opencv3.json                           |   5 +
 versions/o-/opencv4.json                           |   5 +
 versions/p-/paraview.json                          |   5 +
 versions/p-/pipewire.json                          |   5 +
 versions/p-/protobuf.json                          |   5 +
 versions/p-/python3.json                           |   5 +
 versions/q-/qpid-proton.json                       |   5 +
 versions/q-/qt5-base.json                          |   5 +
 versions/q-/qtapplicationmanager.json              |   5 +
 versions/q-/qtbase.json                            |   5 +
 versions/q-/qtinterfaceframework.json              |   5 +
 versions/q-/qtmultimedia.json                      |   5 +
 versions/r-/ryml.json                              |   5 +
 versions/s-/sail.json                              |   5 +
 versions/s-/sdl2.json                              |   5 +
 versions/s-/shiftmedia-libgcrypt.json              |   5 +
 versions/s-/shiftmedia-libgnutls.json              |   5 +
 versions/s-/skia.json                              |   5 +
 versions/s-/sockpp.json                            |   5 +
 versions/s-/stxxl.json                             |   5 +
 versions/s-/symengine.json                         |   5 +
 versions/t-/taglib.json                            |   5 +
 versions/u-/uthenticode.json                       |   5 +
 versions/v-/vcpkg-qmake.json                       |   5 +
 versions/v-/vcpkg-tool-meson.json                  |   5 +
 versions/v-/vtk.json                               |   5 +
 versions/w-/wxwidgets.json                         |   5 +
 versions/x-/x264.json                              |   5 +
 versions/x-/xcb.json                               |   5 +
 versions/x-/xmlsec.json                            |   5 +
 versions/z-/zfp.json                               |   5 +
 versions/z-/zopfli.json                            |   5 +
 253 files changed, 752 insertions(+), 258 deletions(-)

2024-09-22 13:22:33,969 - 147 - INFO - run: git add .
2024-09-22 13:22:33,993 - 147 - INFO - run: git commit -m [vcpkg_replace_string] warn unchanged by call (#34719) --author gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
[main 9b8a6d120] [vcpkg_replace_string] warn unchanged by call (#34719)
 Author: gerard-ryan-immersaview <64181775+gerard-ryan-immersaview@users.noreply.github.com>
 21 files changed, 3404 insertions(+)
 create mode 100644 ports/ffmpeg/0001-create-lib-libraries.patch
 create mode 100644 ports/ffmpeg/0002-fix-msvc-link.patch
 create mode 100644 ports/ffmpeg/0003-fix-windowsinclude.patch
 create mode 100644 ports/ffmpeg/0004-dependencies.patch
 create mode 100644 ports/ffmpeg/0005-fix-nasm.patch
 create mode 100644 ports/ffmpeg/0007-fix-lib-naming.patch
 create mode 100644 ports/ffmpeg/0012-Fix-ssl-110-detection.patch
 create mode 100644 ports/ffmpeg/0013-define-WINVER.patch
 create mode 100644 ports/ffmpeg/0020-fix-aarch64-libswscale.patch
 create mode 100644 ports/ffmpeg/0024-fix-osx-host-c11.patch
 create mode 100644 ports/ffmpeg/0040-ffmpeg-add-av_stream_get_first_dts-for-chromium.patch
 create mode 100644 ports/ffmpeg/0041-add-const-for-opengl-definition.patch
 create mode 100644 ports/ffmpeg/0042-fix-arm64-linux.patch
 create mode 100644 ports/ffmpeg/0043-fix-miss-head.patch
 create mode 100644 ports/ffmpeg/FindFFMPEG.cmake.in
 create mode 100644 ports/ffmpeg/build.sh.in
 create mode 100644 ports/ffmpeg/portfile.cmake
 create mode 100644 ports/ffmpeg/usage
 create mode 100644 ports/ffmpeg/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/ffmpeg/vcpkg.json
 create mode 100644 versions/f-/ffmpeg.json
2024-09-22 13:22:34,058 - 360 - WARNING - copy downloads/vcpkg/ports/x265 -> ./ports/x265
2024-09-22 13:22:34,063 - 369 - WARNING - copy downloads/vcpkg/versions/x-/x265.json -> ./versions/x-/x265.json
2024-09-22 13:22:34,063 - 382 - INFO - x265
commit c6043cde21c993c1f78d2ed20d7c312122ea51cc
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-06-25 03:03:17 +0200

    [x265] Update to 3.6, fix pthread flags, add feature "tools" (#39450)

    Fixes build errors on android due to wrong pthread flags and 32 bit API
    level requirements (`ftello`).

    Alternative to #39314.

 ports/x265/compiler-target.diff | 14 ++++++++++++++
 ports/x265/neon.diff            | 18 ++++++++++++++++++
 ports/x265/pkgconfig.diff       |  9 ---------
 ports/x265/portfile.cmake       | 30 ++++++++++++++++++++++++------
 ports/x265/pthread.diff         | 24 ++++++++++++++++++++++++
 ports/x265/vcpkg.json           | 15 ++++++++++-----
 scripts/ci.baseline.txt         |  3 ---
 versions/baseline.json          |  4 ++--
 versions/x-/x265.json           |  5 +++++
 9 files changed, 97 insertions(+), 25 deletions(-)

2024-09-22 13:22:34,063 - 147 - INFO - run: git add .
2024-09-22 13:22:34,089 - 147 - INFO - run: git commit -m [x265] Update to 3.6, fix pthread flags, add feature "tools" (#39450) --author Kai Pastor <dg0yt@darc.de>
[main a8c18c372] [x265] Update to 3.6, fix pthread flags, add feature "tools" (#39450)
 Author: Kai Pastor <dg0yt@darc.de>
 10 files changed, 361 insertions(+)
 create mode 100644 ports/x265/compiler-target.diff
 create mode 100644 ports/x265/disable-install-pdb.patch
 create mode 100644 ports/x265/linkage.diff
 create mode 100644 ports/x265/neon.diff
 create mode 100644 ports/x265/pkgconfig.diff
 create mode 100644 ports/x265/portfile.cmake
 create mode 100644 ports/x265/pthread.diff
 create mode 100644 ports/x265/vcpkg.json
 create mode 100644 ports/x265/version.patch
 create mode 100644 versions/x-/x265.json
2024-09-22 13:22:34,153 - 360 - WARNING - copy downloads/vcpkg/ports/x264 -> ./ports/x264
2024-09-22 13:22:34,156 - 369 - WARNING - copy downloads/vcpkg/versions/x-/x264.json -> ./versions/x-/x264.json
2024-09-22 13:22:34,156 - 382 - INFO - x264
commit 467f9a6a2704dfae762c0d7d634839fdfbabfeb9
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-06-26 08:26:31 +0200

    [x264] Update to 0.164.3108, use official upstream (#39460)

 ports/x264/configure-as.patch | 10 ----------
 ports/x264/configure.patch    | 40 ++++++++++++++++++++++++++++++++++++++++
 ports/x264/portfile.cmake     | 43 ++++++++++++++++++++++---------------------
 ports/x264/vcpkg.json         | 27 ++++++++++-----------------
 ports/x264/version.diff.in    | 15 +++++++++++++++
 scripts/ci.baseline.txt       |  2 --
 versions/baseline.json        |  4 ++--
 versions/x-/x264.json         |  5 +++++
 8 files changed, 94 insertions(+), 52 deletions(-)

2024-09-22 13:22:34,157 - 147 - INFO - run: git add .
2024-09-22 13:22:34,182 - 147 - INFO - run: git commit -m [x264] Update to 0.164.3108, use official upstream (#39460) --author Kai Pastor <dg0yt@darc.de>
[main c026aa69a] [x264] Update to 0.164.3108, use official upstream (#39460)
 Author: Kai Pastor <dg0yt@darc.de>
 8 files changed, 458 insertions(+)
 create mode 100644 ports/x264/allow-clang-cl.patch
 create mode 100644 ports/x264/configure.patch
 create mode 100644 ports/x264/parallel-install.patch
 create mode 100644 ports/x264/portfile.cmake
 create mode 100644 ports/x264/uwp-cflags.patch
 create mode 100644 ports/x264/vcpkg.json
 create mode 100644 ports/x264/version.diff.in
 create mode 100644 versions/x-/x264.json
2024-09-22 13:22:34,243 - 360 - WARNING - copy downloads/vcpkg/ports/gsasl -> ./ports/gsasl
2024-09-22 13:22:34,244 - 369 - WARNING - copy downloads/vcpkg/versions/g-/gsasl.json -> ./versions/g-/gsasl.json
2024-09-22 13:22:34,245 - 382 - INFO - gsasl
commit 67f5654fe4898cb122e78720c6d5493320873899
Author: talregev <talregev@users.noreply.github.com>
Date:   2024-06-27 00:49:46 +0300

    [gsasl] Add new port (#39247)

 ports/gsasl/fix-windows-compilation.patch    | 14 ++++++++++
 ports/gsasl/portfile.cmake                   | 41 ++++++++++++++++++++++++++++
 ports/gsasl/remove-tests-examples-docs.patch | 13 +++++++++
 ports/gsasl/vcpkg.json                       |  8 ++++++
 versions/baseline.json                       |  4 +++
 versions/g-/gsasl.json                       |  9 ++++++
 6 files changed, 89 insertions(+)

2024-09-22 13:22:34,245 - 147 - INFO - run: git add .
2024-09-22 13:22:34,269 - 147 - INFO - run: git commit -m [gsasl] Add new port (#39247) --author talregev <talregev@users.noreply.github.com>
[main de2f1dc5d] [gsasl] Add new port (#39247)
 Author: talregev <talregev@users.noreply.github.com>
 5 files changed, 85 insertions(+)
 create mode 100644 ports/gsasl/fix-windows-compilation.patch
 create mode 100644 ports/gsasl/portfile.cmake
 create mode 100644 ports/gsasl/remove-tests-examples-docs.patch
 create mode 100644 ports/gsasl/vcpkg.json
 create mode 100644 versions/g-/gsasl.json
2024-09-22 13:22:34,372 - 360 - WARNING - copy downloads/vcpkg/ports/libidn2 -> ./ports/libidn2
2024-09-22 13:22:34,374 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libidn2.json -> ./versions/l-/libidn2.json
2024-09-22 13:22:34,375 - 382 - INFO - libidn2
commit c202ce4d469096bd6d46fe65de74a4737beee01b
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-02 20:49:17 +0200

    [libidn2] Fix patch (#39639)

 ports/libidn2/disable-subdirs.patch | 7 ++++---
 ports/libidn2/vcpkg.json            | 1 +
 versions/baseline.json              | 2 +-
 versions/l-/libidn2.json            | 5 +++++
 4 files changed, 11 insertions(+), 4 deletions(-)

2024-09-22 13:22:34,375 - 147 - INFO - run: git add .
2024-09-22 13:22:34,400 - 147 - INFO - run: git commit -m [libidn2] Fix patch (#39639) --author Kai Pastor <dg0yt@darc.de>
[main 825520d1a] [libidn2] Fix patch (#39639)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 272 insertions(+)
 create mode 100644 ports/libidn2/disable-subdirs.patch
 create mode 100644 ports/libidn2/fix-uwp.patch
 create mode 100644 ports/libidn2/portfile.cmake
 create mode 100644 ports/libidn2/vcpkg.json
 create mode 100644 versions/l-/libidn2.json
2024-09-22 13:22:34,460 - 360 - WARNING - copy downloads/vcpkg/ports/libass -> ./ports/libass
2024-09-22 13:22:34,462 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libass.json -> ./versions/l-/libass.json
2024-09-22 13:22:34,463 - 382 - INFO - libass
commit 49ac2134b31b95b0ddf29d56873dcd24392691df
Author: Kadir <kadir_altindag@outlook.com>
Date:   2024-07-04 15:53:17 +0300

    [libass] Update to version 0.17.3 (#39678)

 ports/libass/portfile.cmake | 2 +-
 ports/libass/vcpkg.json     | 2 +-
 versions/baseline.json      | 2 +-
 versions/l-/libass.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:34,463 - 147 - INFO - run: git add .
2024-09-22 13:22:34,488 - 147 - INFO - run: git commit -m [libass] Update to version 0.17.3 (#39678) --author Kadir <kadir_altindag@outlook.com>
[main ea3caf8a4] [libass] Update to version 0.17.3 (#39678)
 Author: Kadir <kadir_altindag@outlook.com>
 6 files changed, 293 insertions(+)
 create mode 100644 ports/libass/CMakeLists.txt
 create mode 100644 ports/libass/config.h.in
 create mode 100644 ports/libass/libass.def
 create mode 100644 ports/libass/portfile.cmake
 create mode 100644 ports/libass/vcpkg.json
 create mode 100644 versions/l-/libass.json
2024-09-22 13:22:34,588 - 360 - WARNING - copy downloads/vcpkg/ports/libssh -> ./ports/libssh
2024-09-22 13:22:34,590 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libssh.json -> ./versions/l-/libssh.json
2024-09-22 13:22:34,590 - 382 - INFO - libssh
commit 2bc6ff38d1a5ffd4333680d9b00d6db36e88ecac
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-08 16:25:27 +0200

    [libssh] Update, fix, cleanup (#39734)

 ports/libssh/0001-export-pkgconfig-file.patch      | 83 +++++++++++++++-------
 ports/libssh/0002-mingw_for_Android.patch          | 13 ----
 ..._unix_only.patch => 0003-no-source-write.patch} | 15 ++--
 ports/libssh/portfile.cmake                        | 46 ++++--------
 ports/libssh/usage                                 |  4 --
 ports/libssh/vcpkg.json                            | 21 +++++-
 versions/baseline.json                             |  4 +-
 versions/l-/libssh.json                            |  5 ++
 8 files changed, 103 insertions(+), 88 deletions(-)

2024-09-22 13:22:34,590 - 147 - INFO - run: git add .
2024-09-22 13:22:34,616 - 147 - INFO - run: git commit -m [libssh] Update, fix, cleanup (#39734) --author Kai Pastor <dg0yt@darc.de>
[main 2c2b13fbd] [libssh] Update, fix, cleanup (#39734)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 374 insertions(+)
 create mode 100644 ports/libssh/0001-export-pkgconfig-file.patch
 create mode 100644 ports/libssh/0003-no-source-write.patch
 create mode 100644 ports/libssh/0004-file-permissions-constants.patch
 create mode 100644 ports/libssh/portfile.cmake
 create mode 100644 ports/libssh/vcpkg.json
 create mode 100644 versions/l-/libssh.json
2024-09-22 13:22:34,678 - 360 - WARNING - copy downloads/vcpkg/ports/libsrt -> ./ports/libsrt
2024-09-22 13:22:34,680 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libsrt.json -> ./versions/l-/libsrt.json
2024-09-22 13:22:34,680 - 382 - INFO - libsrt
commit a715fc59a44d3a9509e7770fbbe8a325bde82443
Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
Date:   2024-07-09 19:18:55 +0200

    [libsrt] use right var (#39777)

 ports/libsrt/portfile.cmake | 2 +-
 ports/libsrt/vcpkg.json     | 2 +-
 versions/baseline.json      | 2 +-
 versions/l-/libsrt.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:34,680 - 147 - INFO - run: git add .
2024-09-22 13:22:34,706 - 147 - INFO - run: git commit -m [libsrt] use right var (#39777) --author autoantwort <41973254+autoantwort@users.noreply.github.com>
[main f870aa1a6] [libsrt] use right var (#39777)
 Author: autoantwort <41973254+autoantwort@users.noreply.github.com>
 5 files changed, 190 insertions(+)
 create mode 100644 ports/libsrt/fix-static.patch
 create mode 100644 ports/libsrt/pkgconfig.diff
 create mode 100644 ports/libsrt/portfile.cmake
 create mode 100644 ports/libsrt/vcpkg.json
 create mode 100644 versions/l-/libsrt.json
2024-09-22 13:22:34,809 - 360 - WARNING - copy downloads/vcpkg/ports/libmodplug -> ./ports/libmodplug
2024-09-22 13:22:34,811 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libmodplug.json -> ./versions/l-/libmodplug.json
2024-09-22 13:22:34,812 - 382 - INFO - libmodplug
commit f00e89ae1903b95301065da48c84fbaf1cb680ce
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-15 20:02:16 +0200

    [vcpkg-ci-ffmpeg, ffmpeg] Require CI pass on all triplets, fix dependencies (#39703)

 ports/ffmpeg/0004-dependencies.patch          | 21 ++++++++++----
 ports/ffmpeg/FindFFMPEG.cmake.in              | 31 ++++++++++++---------
 ports/ffmpeg/portfile.cmake                   |  8 ++++++
 ports/ffmpeg/vcpkg-cmake-wrapper.cmake        | 17 ++++++++++--
 ports/ffmpeg/vcpkg.json                       |  2 +-
 ports/libmodplug/004-export-pkgconfig.patch   | 40 +++++++++++++++------------
 ports/libmodplug/portfile.cmake               |  2 +-
 ports/libmodplug/vcpkg.json                   |  2 +-
 ports/libopenmpt/CMakeLists.txt               | 12 +++++++-
 ports/libopenmpt/vcpkg.json                   |  1 +
 scripts/ci.baseline.txt                       |  5 ++++
 scripts/test_ports/vcpkg-ci-ffmpeg/vcpkg.json | 24 ++++++++++------
 versions/baseline.json                        |  6 ++--
 versions/f-/ffmpeg.json                       |  5 ++++
 versions/l-/libmodplug.json                   |  5 ++++
 versions/l-/libopenmpt.json                   |  5 ++++
 16 files changed, 133 insertions(+), 53 deletions(-)

2024-09-22 13:22:34,812 - 147 - INFO - run: git add .
2024-09-22 13:22:34,837 - 147 - INFO - run: git commit -m [vcpkg-ci-ffmpeg, ffmpeg] Require CI pass on all triplets, fix dependencies (#39703) --author Kai Pastor <dg0yt@darc.de>
[main c1193c00d] [vcpkg-ci-ffmpeg, ffmpeg] Require CI pass on all triplets, fix dependencies (#39703)
 Author: Kai Pastor <dg0yt@darc.de>
 8 files changed, 255 insertions(+)
 create mode 100644 ports/libmodplug/001-automagically-define-modplug-static.patch
 create mode 100644 ports/libmodplug/002-detect_sinf.patch
 create mode 100644 ports/libmodplug/003-use-static-cast-for-ctype.patch
 create mode 100644 ports/libmodplug/004-export-pkgconfig.patch
 create mode 100644 ports/libmodplug/005-fix-install-paths.patch
 create mode 100644 ports/libmodplug/portfile.cmake
 create mode 100644 ports/libmodplug/vcpkg.json
 create mode 100644 versions/l-/libmodplug.json
2024-09-22 13:22:34,900 - 360 - WARNING - copy downloads/vcpkg/ports/nettle -> ./ports/nettle
2024-09-22 13:22:34,905 - 369 - WARNING - copy downloads/vcpkg/versions/n-/nettle.json -> ./versions/n-/nettle.json
2024-09-22 13:22:34,906 - 382 - INFO - nettle
commit 9d0213c34c1b9ca14febab2894d518a0483e8afb
Author: talregev <talregev@users.noreply.github.com>
Date:   2024-07-23 03:20:03 +0300

    [nettle, shiftmedia-libgnutls] nettle update to 3.10, shiftmedia-libgnutls update to 3.8.4 (#40015)

 ports/nettle/ccas.patch                            | 26 +++++++++++-----------
 ports/nettle/hogweed-arm.def                       | 12 ++++++++--
 ports/nettle/hogweed-arm64.def                     | 12 ++++++++--
 ports/nettle/hogweed-x64.def                       | 12 ++++++++--
 ports/nettle/hogweed-x86.def                       | 12 ++++++++--
 ports/nettle/host-tools.patch                      | 24 ++++++++++----------
 ports/nettle/portfile.cmake                        |  4 ++--
 ports/nettle/subdirs.patch                         |  8 +++----
 ports/nettle/vcpkg.json                            |  2 +-
 ports/shiftmedia-libgnutls/portfile.cmake          |  3 ++-
 .../ssize_t_already_define.patch                   | 14 ++++++++++++
 ports/shiftmedia-libgnutls/vcpkg.json              |  2 +-
 versions/baseline.json                             |  4 ++--
 versions/n-/nettle.json                            |  5 +++++
 versions/s-/shiftmedia-libgnutls.json              |  5 +++++
 15 files changed, 101 insertions(+), 44 deletions(-)

2024-09-22 13:22:34,906 - 147 - INFO - run: git add .
2024-09-22 13:22:34,932 - 147 - INFO - run: git commit -m [nettle, shiftmedia-libgnutls] nettle update to 3.10, shiftmedia-libgnutls update to 3.8.4 (#40015) --author talregev <talregev@users.noreply.github.com>
[main eaa381234] [nettle, shiftmedia-libgnutls] nettle update to 3.10, shiftmedia-libgnutls update to 3.8.4 (#40015)
 Author: talregev <talregev@users.noreply.github.com>
 20 files changed, 4208 insertions(+)
 create mode 100644 ports/nettle/ccas.patch
 create mode 100644 ports/nettle/compile.patch
 create mode 100644 ports/nettle/fix-libdir.patch
 create mode 100644 ports/nettle/hogweed-arm.def
 create mode 100644 ports/nettle/hogweed-arm64.def
 create mode 100644 ports/nettle/hogweed-x64.def
 create mode 100644 ports/nettle/hogweed-x86.def
 create mode 100644 ports/nettle/host-tools.patch
 create mode 100644 ports/nettle/lib-to-def.cmake
 create mode 100644 ports/nettle/libname-windows.patch
 create mode 100644 ports/nettle/msvc-support.patch
 create mode 100644 ports/nettle/nettle-arm.def
 create mode 100644 ports/nettle/nettle-arm64.def
 create mode 100644 ports/nettle/nettle-x64.def
 create mode 100644 ports/nettle/nettle-x86.def
 create mode 100644 ports/nettle/portfile.cmake
 create mode 100644 ports/nettle/subdirs.patch
 create mode 100644 ports/nettle/vcpkg.json
 create mode 100644 ports/nettle/yasm.patch
 create mode 100644 versions/n-/nettle.json
2024-09-22 13:22:34,995 - 360 - WARNING - copy downloads/vcpkg/ports/mp3lame -> ./ports/mp3lame
2024-09-22 13:22:34,999 - 369 - WARNING - copy downloads/vcpkg/versions/m-/mp3lame.json -> ./versions/m-/mp3lame.json
2024-09-22 13:22:35,000 - 382 - INFO - mp3lame
commit 04f9031885529040f9643eaf1f01099ce93d1139
Author: derekcyruschow-catapult <7149253+derekcyruschow-catapult@users.noreply.github.com>
Date:   2024-07-24 01:47:27 +0100

    [mp3lame] decouple executable as 'frontend' non-default feature (#39969)

    Co-authored-by: Derek Cyrus-Chow <derek.chow@catapult.com>

 ports/mp3lame/portfile.cmake | 35 +++++++++++++++++++++++++++++------
 ports/mp3lame/vcpkg.json     | 15 +++++++++++++--
 versions/baseline.json       |  2 +-
 versions/m-/mp3lame.json     |  5 +++++
 4 files changed, 48 insertions(+), 9 deletions(-)

2024-09-22 13:22:35,000 - 147 - INFO - run: git add .
2024-09-22 13:22:35,029 - 147 - INFO - run: git commit -m [mp3lame] decouple executable as 'frontend' non-default feature (#39969) --author derekcyruschow-catapult <7149253+derekcyruschow-catapult@users.noreply.github.com>
[main 877483866] [mp3lame] decouple executable as 'frontend' non-default feature (#39969)
 Author: derekcyruschow-catapult <7149253+derekcyruschow-catapult@users.noreply.github.com>
 9 files changed, 1454 insertions(+)
 create mode 100644 ports/mp3lame/00001-msvc-upgrade-solution-up-to-vc11.patch
 create mode 100644 ports/mp3lame/Config.cmake.in
 create mode 100644 ports/mp3lame/add-macos-universal-config.patch
 create mode 100644 ports/mp3lame/fix-mingw-w64-compatibility.patch
 create mode 100644 ports/mp3lame/portfile.cmake
 create mode 100644 ports/mp3lame/remove_lame_init_old_from_symbol_list.patch
 create mode 100644 ports/mp3lame/usage
 create mode 100644 ports/mp3lame/vcpkg.json
 create mode 100644 versions/m-/mp3lame.json
2024-09-22 13:22:35,091 - 360 - WARNING - copy downloads/vcpkg/ports/lz4 -> ./ports/lz4
2024-09-22 13:22:35,093 - 369 - WARNING - copy downloads/vcpkg/versions/l-/lz4.json -> ./versions/l-/lz4.json
2024-09-22 13:22:35,094 - 382 - INFO - lz4
commit 853e515b2b512953a536f411d38f053a89de5b33
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-25 22:34:56 +0200

    [lz4] Update to 1.10.0, use official CMake build system (#40052)

    Co-authored-by: Theodore Tsirpanis <theodore.tsirpanis@tiledb.com>

 ports/librdkafka/lz4.patch      | 55 +++++++++++++++++++-------------------
 ports/librdkafka/portfile.cmake |  8 +++---
 ports/librdkafka/vcpkg.json     |  2 +-
 ports/lz4/CMakeLists.txt        | 58 -----------------------------------------
 ports/lz4/portfile.cmake        | 34 +++++++++++++++++++-----
 ports/lz4/target-lz4-lz4.diff   | 17 ++++++++++++
 ports/lz4/usage                 |  8 ++++++
 ports/lz4/vcpkg.json            | 11 +++++---
 ports/vtk/FindLZ4.patch         |  2 +-
 ports/vtk/vcpkg.json            |  2 +-
 versions/baseline.json          |  8 +++---
 versions/l-/librdkafka.json     |  5 ++++
 versions/l-/lz4.json            |  5 ++++
 versions/v-/vtk.json            |  5 ++++
 14 files changed, 113 insertions(+), 107 deletions(-)

2024-09-22 13:22:35,094 - 147 - INFO - run: git add .
2024-09-22 13:22:35,119 - 147 - INFO - run: git commit -m [lz4] Update to 1.10.0, use official CMake build system (#40052) --author Kai Pastor <dg0yt@darc.de>
[main a96eba15d] [lz4] Update to 1.10.0, use official CMake build system (#40052)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 234 insertions(+)
 create mode 100644 ports/lz4/portfile.cmake
 create mode 100644 ports/lz4/target-lz4-lz4.diff
 create mode 100644 ports/lz4/usage
 create mode 100644 ports/lz4/vcpkg.json
 create mode 100644 versions/l-/lz4.json
2024-09-22 13:22:35,180 - 360 - WARNING - copy downloads/vcpkg/ports/openldap -> ./ports/openldap
2024-09-22 13:22:35,184 - 369 - WARNING - copy downloads/vcpkg/versions/o-/openldap.json -> ./versions/o-/openldap.json
2024-09-22 13:22:35,184 - 382 - INFO - openldap
commit ed2899e6ef2d72327c6dab2002277cb48485dcd4
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-26 09:15:25 +0200

    [openldap] Update to 2.5.18 (#40093)

 ports/openldap/openssl.patch  | 15 +++++++++++----
 ports/openldap/portfile.cmake |  3 +--
 ports/openldap/usage          |  6 ------
 ports/openldap/vcpkg.json     |  3 +--
 versions/baseline.json        |  4 ++--
 versions/o-/openldap.json     |  5 +++++
 6 files changed, 20 insertions(+), 16 deletions(-)

2024-09-22 13:22:35,184 - 147 - INFO - run: git add .
2024-09-22 13:22:35,209 - 147 - INFO - run: git commit -m [openldap] Update to 2.5.18 (#40093) --author Kai Pastor <dg0yt@darc.de>
[main 5c384152d] [openldap] Update to 2.5.18 (#40093)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 206 insertions(+)
 create mode 100644 ports/openldap/m4.patch
 create mode 100644 ports/openldap/openssl.patch
 create mode 100644 ports/openldap/portfile.cmake
 create mode 100644 ports/openldap/subdirs.patch
 create mode 100644 ports/openldap/vcpkg.json
 create mode 100644 versions/o-/openldap.json
2024-09-22 13:22:35,292 - 360 - WARNING - copy downloads/vcpkg/ports/opencl -> ./ports/opencl
2024-09-22 13:22:35,293 - 369 - WARNING - copy downloads/vcpkg/versions/o-/opencl.json -> ./versions/o-/opencl.json
2024-09-22 13:22:35,294 - 382 - INFO - opencl
commit 752799690be680e3b16ceb8e5a4db2f683af6ae3
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-31 02:39:19 +0200

    [opencl] Update, add Utility lib (#40122)

 .../0001-include-unistd-for-gete-ug-id.patch       | 27 ------
 ports/opencl/portfile.cmake                        | 99 ++++++++++++----------
 ports/opencl/usage                                 | 24 +++---
 ports/opencl/vcpkg.json                            |  9 +-
 versions/baseline.json                             |  4 +-
 versions/o-/opencl.json                            |  5 ++
 6 files changed, 79 insertions(+), 89 deletions(-)

2024-09-22 13:22:35,294 - 147 - INFO - run: git add .
2024-09-22 13:22:35,320 - 147 - INFO - run: git commit -m [opencl] Update, add Utility lib (#40122) --author Kai Pastor <dg0yt@darc.de>
[main fe853c0be] [opencl] Update, add Utility lib (#40122)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 246 insertions(+)
 create mode 100644 ports/opencl/portfile.cmake
 create mode 100644 ports/opencl/usage
 create mode 100644 ports/opencl/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/opencl/vcpkg.json
 create mode 100644 versions/o-/opencl.json
2024-09-22 13:22:35,384 - 360 - WARNING - copy downloads/vcpkg/ports/krb5 -> ./ports/krb5
2024-09-22 13:22:35,387 - 369 - WARNING - copy downloads/vcpkg/versions/k-/krb5.json -> ./versions/k-/krb5.json
2024-09-22 13:22:35,388 - 382 - INFO - krb5
commit 2d27533fd797fd2b3e9874015a3a266a7457c1c6
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-07-31 21:18:48 +0200

    [cyrus-sasl,krb5] Fix dependencies (#40117)

 ports/cyrus-sasl/configure.diff | 81 +++++++++++++++++++++++++++++++++++++
 ports/cyrus-sasl/portfile.cmake | 89 +++++++++++++++++++++++++++++++++--------
 ports/cyrus-sasl/vcpkg.json     | 10 ++---
 ports/krb5/static-deps.diff     | 16 +++++++-
 ports/krb5/vcpkg.json           |  1 +
 versions/baseline.json          |  4 +-
 versions/c-/cyrus-sasl.json     |  5 +++
 versions/k-/krb5.json           |  5 +++
 8 files changed, 185 insertions(+), 26 deletions(-)

2024-09-22 13:22:35,388 - 147 - INFO - run: git add .
2024-09-22 13:22:35,413 - 147 - INFO - run: git commit -m [cyrus-sasl,krb5] Fix dependencies (#40117) --author Kai Pastor <dg0yt@darc.de>
[main 2567cdc63] [cyrus-sasl,krb5] Fix dependencies (#40117)
 Author: Kai Pastor <dg0yt@darc.de>
 9 files changed, 267 insertions(+)
 create mode 100644 ports/krb5/define-des-zeroblock.diff
 create mode 100644 ports/krb5/portfile.cmake
 create mode 100644 ports/krb5/static-deps.diff
 create mode 100644 ports/krb5/vcpkg.json
 create mode 100644 ports/krb5/windows_pc_files/krb5-gssapi.pc.in
 create mode 100644 ports/krb5/windows_pc_files/krb5.pc.in
 create mode 100644 ports/krb5/windows_pc_files/mit-krb5-gssapi.pc.in
 create mode 100644 ports/krb5/windows_pc_files/mit-krb5.pc.in
 create mode 100644 versions/k-/krb5.json
2024-09-22 13:22:35,476 - 360 - WARNING - copy downloads/vcpkg/ports/libsystemd -> ./ports/libsystemd
2024-09-22 13:22:35,478 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libsystemd.json -> ./versions/l-/libsystemd.json
2024-09-22 13:22:35,479 - 382 - INFO - libsystemd
commit fa4c3826619405d540197889e022ad8b05244e8b
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-08-05 20:38:06 +0200

    [libsystemd] Update to 256.4 (#40274)

 ports/libsystemd/portfile.cmake | 2 +-
 ports/libsystemd/vcpkg.json     | 2 +-
 versions/baseline.json          | 2 +-
 versions/l-/libsystemd.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:35,479 - 147 - INFO - run: git add .
2024-09-22 13:22:35,504 - 147 - INFO - run: git commit -m [libsystemd] Update to 256.4 (#40274) --author Kai Pastor <dg0yt@darc.de>
[main 2c7df9712] [libsystemd] Update to 256.4 (#40274)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 247 insertions(+)
 create mode 100644 ports/libsystemd/disable-warning-nonnull.patch
 create mode 100644 ports/libsystemd/only-libsystemd.patch
 create mode 100644 ports/libsystemd/pkgconfig.patch
 create mode 100644 ports/libsystemd/portfile.cmake
 create mode 100644 ports/libsystemd/vcpkg.json
 create mode 100644 versions/l-/libsystemd.json
2024-09-22 13:22:35,566 - 360 - WARNING - copy downloads/vcpkg/ports/abseil -> ./ports/abseil
2024-09-22 13:22:35,568 - 369 - WARNING - copy downloads/vcpkg/versions/a-/abseil.json -> ./versions/a-/abseil.json
2024-09-22 13:22:35,568 - 382 - INFO - abseil
commit 4327b9c40ad4cc726377b7d4bec6ac16ae218458
Author: c8ef <c8ef@outlook.com>
Date:   2024-08-07 05:22:36 +0800

    [abseil] update to 20240722.0 (#40297)

 ...nteger-to-string-conversion-optimizations.patch | 1313 --------------------
 ...-include-random-for-std-uniform_int_distr.patch |   29 -
 ports/abseil/779a356-test-allocator.diff           |   12 -
 ports/abseil/portfile.cmake                        |   18 +-
 ports/abseil/vcpkg.json                            |    3 +-
 versions/a-/abseil.json                            |    5 +
 versions/baseline.json                             |    4 +-
 7 files changed, 18 insertions(+), 1366 deletions(-)

2024-09-22 13:22:35,568 - 147 - INFO - run: git add .
2024-09-22 13:22:35,593 - 147 - INFO - run: git commit -m [abseil] update to 20240722.0 (#40297) --author c8ef <c8ef@outlook.com>
[main ef51801e8] [abseil] update to 20240722.0 (#40297)
 Author: c8ef <c8ef@outlook.com>
 3 files changed, 473 insertions(+)
 create mode 100644 ports/abseil/portfile.cmake
 create mode 100644 ports/abseil/vcpkg.json
 create mode 100644 versions/a-/abseil.json
2024-09-22 13:22:35,657 - 360 - WARNING - copy downloads/vcpkg/ports/libpng -> ./ports/libpng
2024-09-22 13:22:35,660 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libpng.json -> ./versions/l-/libpng.json
2024-09-22 13:22:35,661 - 382 - INFO - libpng
commit f5398d978f8843c03ed466c7fdb8a54167cd5f51
Author: Andrew Kaster <andrewdkaster@gmail.com>
Date:   2024-08-07 22:39:15 -0600

    [libpng] Remove -DPNG_PREFIX=a option when apng feature enabled (#40280)

 ports/libpng/portfile.cmake | 3 ---
 ports/libpng/vcpkg.json     | 2 +-
 versions/baseline.json      | 2 +-
 versions/l-/libpng.json     | 5 +++++
 4 files changed, 7 insertions(+), 5 deletions(-)

2024-09-22 13:22:35,661 - 147 - INFO - run: git add .
2024-09-22 13:22:35,687 - 147 - INFO - run: git commit -m [libpng] Remove -DPNG_PREFIX=a option when apng feature enabled (#40280) --author Andrew Kaster <andrewdkaster@gmail.com>
[main be828ee48] [libpng] Remove -DPNG_PREFIX=a option when apng feature enabled (#40280)
 Author: Andrew Kaster <andrewdkaster@gmail.com>
 10 files changed, 485 insertions(+)
 create mode 100644 ports/libpng/cmake.patch
 create mode 100644 ports/libpng/fix-export-targets.patch
 create mode 100644 ports/libpng/fix-msa-support-for-mips.patch
 create mode 100644 ports/libpng/libm.patch
 create mode 100644 ports/libpng/pkgconfig.patch
 create mode 100644 ports/libpng/portfile.cmake
 create mode 100644 ports/libpng/usage
 create mode 100644 ports/libpng/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/libpng/vcpkg.json
 create mode 100644 versions/l-/libpng.json
2024-09-22 13:22:35,748 - 360 - WARNING - copy downloads/vcpkg/ports/libdeflate -> ./ports/libdeflate
2024-09-22 13:22:35,750 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libdeflate.json -> ./versions/l-/libdeflate.json
2024-09-22 13:22:35,750 - 382 - INFO - libdeflate
commit 8db6e1924cf7a0dbdb0e55a81adecbdf59845f6f
Author: SunBlack <SunBlack@users.noreply.github.com>
Date:   2024-08-10 11:22:04 +0200

    [libdeflate] Update to v1.21 (#40357)

 ports/libdeflate/fix_gcc.patch  | 21 ---------------------
 ports/libdeflate/portfile.cmake |  3 +--
 ports/libdeflate/vcpkg.json     |  3 +--
 versions/baseline.json          |  4 ++--
 versions/l-/libdeflate.json     |  5 +++++
 5 files changed, 9 insertions(+), 27 deletions(-)

2024-09-22 13:22:35,750 - 147 - INFO - run: git add .
2024-09-22 13:22:35,775 - 147 - INFO - run: git commit -m [libdeflate] Update to v1.21 (#40357) --author SunBlack <SunBlack@users.noreply.github.com>
[main c696cf04a] [libdeflate] Update to v1.21 (#40357)
 Author: SunBlack <SunBlack@users.noreply.github.com>
 5 files changed, 140 insertions(+)
 create mode 100644 ports/libdeflate/portfile.cmake
 create mode 100644 ports/libdeflate/remove_wrong_c_flags_modification.diff
 create mode 100644 ports/libdeflate/usage
 create mode 100644 ports/libdeflate/vcpkg.json
 create mode 100644 versions/l-/libdeflate.json
2024-09-22 13:22:35,839 - 360 - WARNING - copy downloads/vcpkg/ports/libxml2 -> ./ports/libxml2
2024-09-22 13:22:35,841 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libxml2.json -> ./versions/l-/libxml2.json
2024-09-22 13:22:35,841 - 382 - INFO - libxml2
commit 0f8b6ddf49fa8ae66a7826234e9ba3fda5f46d3c
Author: jim wang <122244446+jimwang118@users.noreply.github.com>
Date:   2024-08-12 23:36:17 +0000

    [libxml2] Update to 2.11.9 (#40375)

 ports/libxml2/portfile.cmake | 2 +-
 ports/libxml2/vcpkg.json     | 2 +-
 versions/baseline.json       | 2 +-
 versions/l-/libxml2.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:35,841 - 147 - INFO - run: git add .
2024-09-22 13:22:35,867 - 147 - INFO - run: git commit -m [libxml2] Update to 2.11.9 (#40375) --author jim wang <122244446+jimwang118@users.noreply.github.com>
[main 8fbf99bda] [libxml2] Update to 2.11.9 (#40375)
 Author: jim wang <122244446+jimwang118@users.noreply.github.com>
 7 files changed, 486 insertions(+)
 create mode 100644 ports/libxml2/disable-docs.patch
 create mode 100644 ports/libxml2/fix_cmakelist.patch
 create mode 100644 ports/libxml2/portfile.cmake
 create mode 100644 ports/libxml2/usage
 create mode 100644 ports/libxml2/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/libxml2/vcpkg.json
 create mode 100644 versions/l-/libxml2.json
2024-09-22 13:22:36,009 - 360 - WARNING - copy downloads/vcpkg/ports/mfx-dispatch -> ./ports/mfx-dispatch
2024-09-22 13:22:36,010 - 369 - WARNING - copy downloads/vcpkg/versions/m-/mfx-dispatch.json -> ./versions/m-/mfx-dispatch.json
2024-09-22 13:22:36,011 - 382 - INFO - mfx-dispatch
commit 330dddb4f047c24d17849eb210da4416f7df7fe0
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-08-17 10:46:09 +0200

    [mfx-dispatch] Fix non-msvc (#40460)

 ports/mfx-dispatch/portfile.cmake             | 41 +++++++++++++++------------
 ports/mfx-dispatch/vcpkg.json                 |  7 +++--
 scripts/ci.baseline.txt                       |  3 --
 scripts/test_ports/vcpkg-ci-ffmpeg/vcpkg.json |  8 ++++++
 versions/baseline.json                        |  2 +-
 versions/m-/mfx-dispatch.json                 |  5 ++++
 6 files changed, 41 insertions(+), 25 deletions(-)

2024-09-22 13:22:36,011 - 147 - INFO - run: git add .
2024-09-22 13:22:36,036 - 147 - INFO - run: git commit -m [mfx-dispatch] Fix non-msvc (#40460) --author Kai Pastor <dg0yt@darc.de>
[main 6c7c3a688] [mfx-dispatch] Fix non-msvc (#40460)
 Author: Kai Pastor <dg0yt@darc.de>
 5 files changed, 181 insertions(+)
 create mode 100644 ports/mfx-dispatch/fix-pkgconf.patch
 create mode 100644 ports/mfx-dispatch/fix-unresolved-symbol.patch
 create mode 100644 ports/mfx-dispatch/portfile.cmake
 create mode 100644 ports/mfx-dispatch/vcpkg.json
 create mode 100644 versions/m-/mfx-dispatch.json
2024-09-22 13:22:36,101 - 360 - WARNING - copy downloads/vcpkg/ports/dav1d -> ./ports/dav1d
2024-09-22 13:22:36,102 - 369 - WARNING - copy downloads/vcpkg/versions/d-/dav1d.json -> ./versions/d-/dav1d.json
2024-09-22 13:22:36,103 - 382 - INFO - dav1d
commit 1203d7c0eb9f17701b0925872078ebed70693336
Author: Clinton Ingram <clinton.ingram@outlook.com>
Date:   2024-08-19 09:47:54 -0700

    [dav1d] Update to 1.4.3 (#40518)

 ports/dav1d/portfile.cmake | 2 +-
 ports/dav1d/vcpkg.json     | 3 +--
 versions/baseline.json     | 4 ++--
 versions/d-/dav1d.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:22:36,103 - 147 - INFO - run: git add .
2024-09-22 13:22:36,127 - 147 - INFO - run: git commit -m [dav1d] Update to 1.4.3 (#40518) --author Clinton Ingram <clinton.ingram@outlook.com>
[main 49a72f9ed] [dav1d] Update to 1.4.3 (#40518)
 Author: Clinton Ingram <clinton.ingram@outlook.com>
 4 files changed, 143 insertions(+)
 create mode 100644 ports/dav1d/portfile.cmake
 create mode 100644 ports/dav1d/usage
 create mode 100644 ports/dav1d/vcpkg.json
 create mode 100644 versions/d-/dav1d.json
2024-09-22 13:22:36,189 - 360 - WARNING - copy downloads/vcpkg/ports/libgnutls -> ./ports/libgnutls
2024-09-22 13:22:36,190 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libgnutls.json -> ./versions/l-/libgnutls.json
2024-09-22 13:22:36,192 - 382 - INFO - libgnutls
commit 5f307bfca6210be4a530ea1ab2bf4ee6720286eb
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-08-19 18:56:00 +0200

    [libgnutls] Update to 3.8.7.1 (#40472)

 ports/libgnutls/compression-libs.diff   | 21 +++++++++++++++
 ports/libgnutls/link-zlib.patch         | 48 ---------------------------------
 ports/libgnutls/portfile.cmake          |  8 ++++--
 ports/libgnutls/use-gmp-pkgconfig.patch | 12 ++-------
 ports/libgnutls/vcpkg.json              |  3 +--
 versions/baseline.json                  |  4 +--
 versions/l-/libgnutls.json              |  5 ++++
 7 files changed, 37 insertions(+), 64 deletions(-)

2024-09-22 13:22:36,192 - 147 - INFO - run: git add .
2024-09-22 13:22:36,217 - 147 - INFO - run: git commit -m [libgnutls] Update to 3.8.7.1 (#40472) --author Kai Pastor <dg0yt@darc.de>
[main 821eea6d5] [libgnutls] Update to 3.8.7.1 (#40472)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 227 insertions(+)
 create mode 100644 ports/libgnutls/ccasflags.patch
 create mode 100644 ports/libgnutls/compression-libs.diff
 create mode 100644 ports/libgnutls/portfile.cmake
 create mode 100644 ports/libgnutls/use-gmp-pkgconfig.patch
 create mode 100644 ports/libgnutls/vcpkg.json
 create mode 100644 versions/l-/libgnutls.json
2024-09-22 13:22:36,280 - 360 - WARNING - copy downloads/vcpkg/ports/libcap -> ./ports/libcap
2024-09-22 13:22:36,282 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libcap.json -> ./versions/l-/libcap.json
2024-09-22 13:22:36,283 - 382 - INFO - libcap
commit 84cd873d8092ccd8a1e05d400b2c4d99ba57d8ca
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-08-26 10:00:02 +0200

    [libcap] Update to 2.70 (#40600)

 ports/libcap/portfile.cmake | 2 +-
 ports/libcap/vcpkg.json     | 3 +--
 versions/baseline.json      | 4 ++--
 versions/l-/libcap.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:22:36,283 - 147 - INFO - run: git add .
2024-09-22 13:22:36,309 - 147 - INFO - run: git commit -m [libcap] Update to 2.70 (#40600) --author Kai Pastor <dg0yt@darc.de>
[main 63f5db268] [libcap] Update to 2.70 (#40600)
 Author: Kai Pastor <dg0yt@darc.de>
 4 files changed, 136 insertions(+)
 create mode 100644 ports/libcap/configure
 create mode 100644 ports/libcap/portfile.cmake
 create mode 100644 ports/libcap/vcpkg.json
 create mode 100644 versions/l-/libcap.json
2024-09-22 13:22:36,371 - 360 - WARNING - copy downloads/vcpkg/ports/mpg123 -> ./ports/mpg123
2024-09-22 13:22:36,372 - 369 - WARNING - copy downloads/vcpkg/versions/m-/mpg123.json -> ./versions/m-/mpg123.json
2024-09-22 13:22:36,373 - 382 - INFO - mpg123
commit a1f4ba49f751f6f042d63339fee69194bdca8df7
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-09-03 20:55:42 +0200

    [mpg123] Update, cleanup (#40741)

 ports/mpg123/fix-checktypesize.patch               | 14 --------------
 ports/mpg123/fix-modulejack.patch                  | 13 -------------
 ports/mpg123/fix-modules-cmake-cflags.patch        | 19 -------------------
 ports/mpg123/{fix-m1-build.patch => have-fpu.diff} | 14 +++++++-------
 ports/mpg123/portfile.cmake                        |  9 ++++-----
 ports/mpg123/vcpkg.json                            |  3 +--
 versions/baseline.json                             |  4 ++--
 versions/m-/mpg123.json                            |  5 +++++
 8 files changed, 19 insertions(+), 62 deletions(-)

2024-09-22 13:22:36,373 - 147 - INFO - run: git add .
2024-09-22 13:22:36,399 - 147 - INFO - run: git commit -m [mpg123] Update, cleanup (#40741) --author Kai Pastor <dg0yt@darc.de>
[main cfef94c4a] [mpg123] Update, cleanup (#40741)
 Author: Kai Pastor <dg0yt@darc.de>
 4 files changed, 257 insertions(+)
 create mode 100644 ports/mpg123/have-fpu.diff
 create mode 100644 ports/mpg123/portfile.cmake
 create mode 100644 ports/mpg123/vcpkg.json
 create mode 100644 versions/m-/mpg123.json
2024-09-22 13:22:36,460 - 360 - WARNING - copy downloads/vcpkg/ports/shiftmedia-libgnutls -> ./ports/shiftmedia-libgnutls
2024-09-22 13:22:36,462 - 369 - WARNING - copy downloads/vcpkg/versions/s-/shiftmedia-libgnutls.json -> ./versions/s-/shiftmedia-libgnutls.json
2024-09-22 13:22:36,463 - 382 - INFO - shiftmedia-libgnutls
commit 3f929a1bdfaddedde88b2d88da52298670794c89
Author: talregev <talregev@users.noreply.github.com>
Date:   2024-09-03 21:56:21 +0300

    [shiftmedia-libgnutls] Fix mkdir too many arguments (#40739)

 ports/shiftmedia-libgnutls/mkdir.patch    | 13 +++++++++++++
 ports/shiftmedia-libgnutls/portfile.cmake |  1 +
 ports/shiftmedia-libgnutls/vcpkg.json     |  2 +-
 versions/baseline.json                    |  2 +-
 versions/s-/shiftmedia-libgnutls.json     |  5 +++++
 5 files changed, 21 insertions(+), 2 deletions(-)

2024-09-22 13:22:36,463 - 147 - INFO - run: git add .
2024-09-22 13:22:36,490 - 147 - INFO - run: git commit -m [shiftmedia-libgnutls] Fix mkdir too many arguments (#40739) --author talregev <talregev@users.noreply.github.com>
[main 11dd0afb9] [shiftmedia-libgnutls] Fix mkdir too many arguments (#40739)
 Author: talregev <talregev@users.noreply.github.com>
 9 files changed, 421 insertions(+)
 create mode 100644 ports/shiftmedia-libgnutls/external-libtasn1.patch
 create mode 100644 ports/shiftmedia-libgnutls/fix-warnings.patch
 create mode 100644 ports/shiftmedia-libgnutls/mkdir.patch
 create mode 100644 ports/shiftmedia-libgnutls/pkgconfig.patch
 create mode 100644 ports/shiftmedia-libgnutls/portfile.cmake
 create mode 100644 ports/shiftmedia-libgnutls/ssize_t_already_define.patch
 create mode 100644 ports/shiftmedia-libgnutls/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/shiftmedia-libgnutls/vcpkg.json
 create mode 100644 versions/s-/shiftmedia-libgnutls.json
2024-09-22 13:22:36,552 - 360 - WARNING - copy downloads/vcpkg/ports/c-ares -> ./ports/c-ares
2024-09-22 13:22:36,554 - 369 - WARNING - copy downloads/vcpkg/versions/c-/c-ares.json -> ./versions/c-/c-ares.json
2024-09-22 13:22:36,555 - 382 - INFO - c-ares
commit 52f11d7a88e931c0a6ba02d35bad011832d1604d
Author: Mikael Lindemann <359941+mikaellindemann@users.noreply.github.com>
Date:   2024-09-03 22:36:04 +0200

    [c-ares] Update port to 1.33.1 (#40646)

 ports/c-ares/portfile.cmake | 2 +-
 ports/c-ares/vcpkg.json     | 2 +-
 versions/baseline.json      | 2 +-
 versions/c-/c-ares.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:36,555 - 147 - INFO - run: git add .
2024-09-22 13:22:36,580 - 147 - INFO - run: git commit -m [c-ares] Update port to 1.33.1 (#40646) --author Mikael Lindemann <359941+mikaellindemann@users.noreply.github.com>
[main a38255f7d] [c-ares] Update port to 1.33.1 (#40646)
 Author: Mikael Lindemann <359941+mikaellindemann@users.noreply.github.com>
 5 files changed, 217 insertions(+)
 create mode 100644 ports/c-ares/avoid-docs.patch
 create mode 100644 ports/c-ares/portfile.cmake
 create mode 100644 ports/c-ares/usage
 create mode 100644 ports/c-ares/vcpkg.json
 create mode 100644 versions/c-/c-ares.json
2024-09-22 13:22:36,643 - 360 - WARNING - copy downloads/vcpkg/ports/fontconfig -> ./ports/fontconfig
2024-09-22 13:22:36,645 - 369 - WARNING - copy downloads/vcpkg/versions/f-/fontconfig.json -> ./versions/f-/fontconfig.json
2024-09-22 13:22:36,646 - 382 - INFO - fontconfig
commit fd4c30b55e0991ce2f71e4bde02b30a986e2c0e8
Author: Osyotr <Osyotr@users.noreply.github.com>
Date:   2024-09-03 22:38:18 +0300

    [fontconfig/freetype/fribidi] Update versions (#40668)

 ports/fontconfig/fix-preprocessor-clang-cl.patch | 13 ------
 ports/fontconfig/libgetopt.patch                 |  4 +-
 ports/fontconfig/no-etc-symlinks.patch           |  2 +-
 ports/fontconfig/portfile.cmake                  |  4 +-
 ports/fontconfig/vcpkg.json                      |  8 ++--
 ports/freetype/portfile.cmake                    | 13 +++---
 ports/freetype/vcpkg.json                        |  3 +-
 ports/fribidi/portfile.cmake                     |  2 +-
 ports/fribidi/vcpkg.json                         |  3 +-
 ports/ftgl/01_disable_doxygen.patch              | 30 -------------
 ports/ftgl/fix-cmake.diff                        | 12 +++++
 ports/ftgl/fix-gl-flags.diff                     | 26 +++++++++++
 ports/ftgl/freetype-usage.diff                   | 56 ++++++++++++++++++++++++
 ports/ftgl/install-pkgconfig.diff                | 30 +++++++++++++
 ports/ftgl/portfile.cmake                        | 27 ++++++++----
 ports/ftgl/vcpkg.json                            |  9 ++--
 ports/opencascade/fix-freetype.diff              | 13 ++++++
 ports/opencascade/portfile.cmake                 |  1 +
 ports/opencascade/vcpkg.json                     |  1 +
 versions/baseline.json                           | 16 +++----
 versions/f-/fontconfig.json                      |  5 +++
 versions/f-/freetype.json                        |  5 +++
 versions/f-/fribidi.json                         |  5 +++
 versions/f-/ftgl.json                            |  5 +++
 versions/o-/opencascade.json                     |  5 +++
 25 files changed, 218 insertions(+), 80 deletions(-)

2024-09-22 13:22:36,646 - 147 - INFO - run: git add .
2024-09-22 13:22:36,673 - 147 - INFO - run: git commit -m [fontconfig/freetype/fribidi] Update versions (#40668) --author Osyotr <Osyotr@users.noreply.github.com>
[main e41983d54] [fontconfig/freetype/fribidi] Update versions (#40668)
 Author: Osyotr <Osyotr@users.noreply.github.com>
 7 files changed, 531 insertions(+)
 create mode 100644 ports/fontconfig/libgetopt.patch
 create mode 100644 ports/fontconfig/no-etc-symlinks.patch
 create mode 100644 ports/fontconfig/portfile.cmake
 create mode 100644 ports/fontconfig/usage
 create mode 100644 ports/fontconfig/vcpkg-cmake-wrapper.cmake.in
 create mode 100644 ports/fontconfig/vcpkg.json
 create mode 100644 versions/f-/fontconfig.json
2024-09-22 13:22:36,755 - 360 - WARNING - copy downloads/vcpkg/ports/mbedtls -> ./ports/mbedtls
2024-09-22 13:22:36,757 - 369 - WARNING - copy downloads/vcpkg/versions/m-/mbedtls.json -> ./versions/m-/mbedtls.json
2024-09-22 13:22:36,758 - 382 - INFO - mbedtls
commit 15958906f3205b64138969d7c06194c781998237
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-09-08 21:04:08 +0200

    [mbedtls] Update to 3.6.1 (#40687)

 ports/mbedtls/enable-pthread.patch      | 136 +++++++++++---------------------
 ports/mbedtls/portfile.cmake            |  40 ++++++----
 ports/mbedtls/usage                     |  18 +++++
 ports/mbedtls/vcpkg-cmake-wrapper.cmake |  50 ++++++------
 ports/mbedtls/vcpkg.json                |   7 +-
 ports/oatpp-mbedtls/find-mbedtls.patch  | 120 +---------------------------
 ports/oatpp-mbedtls/mbedtls-3.patch     |  44 +++++++++++
 ports/oatpp-mbedtls/portfile.cmake      |  24 ++++--
 ports/oatpp-mbedtls/vcpkg.json          |   4 +-
 ports/openvpn3/dependencies.diff        |  13 +--
 ports/openvpn3/vcpkg.json               |   1 +
 versions/baseline.json                  |   6 +-
 versions/m-/mbedtls.json                |   5 ++
 versions/o-/oatpp-mbedtls.json          |   5 ++
 versions/o-/openvpn3.json               |   5 ++
 15 files changed, 204 insertions(+), 274 deletions(-)

2024-09-22 13:22:36,758 - 147 - INFO - run: git add .
2024-09-22 13:22:36,784 - 147 - INFO - run: git commit -m [mbedtls] Update to 3.6.1 (#40687) --author Kai Pastor <dg0yt@darc.de>
[main 1122526a4] [mbedtls] Update to 3.6.1 (#40687)
 Author: Kai Pastor <dg0yt@darc.de>
 6 files changed, 266 insertions(+)
 create mode 100644 ports/mbedtls/enable-pthread.patch
 create mode 100644 ports/mbedtls/portfile.cmake
 create mode 100644 ports/mbedtls/usage
 create mode 100644 ports/mbedtls/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/mbedtls/vcpkg.json
 create mode 100644 versions/m-/mbedtls.json
2024-09-22 13:22:36,849 - 360 - WARNING - copy downloads/vcpkg/ports/opus -> ./ports/opus
2024-09-22 13:22:36,850 - 369 - WARNING - copy downloads/vcpkg/versions/o-/opus.json -> ./versions/o-/opus.json
2024-09-22 13:22:36,850 - 382 - INFO - opus
commit 4ed66755acdd1a634609dae3afef930ff8983284
Author: Jiangjie <gaojiangjie@live.com>
Date:   2024-09-09 02:52:43 +0800

    [opus] update to v1.5.2 (#40768) (#40771)

 ports/opus/portfile.cmake | 6 +++++-
 ports/opus/vcpkg.json     | 2 +-
 versions/baseline.json    | 2 +-
 versions/o-/opus.json     | 5 +++++
 4 files changed, 12 insertions(+), 3 deletions(-)

2024-09-22 13:22:36,850 - 147 - INFO - run: git add .
2024-09-22 13:22:36,877 - 147 - INFO - run: git commit -m [opus] update to v1.5.2 (#40768) (#40771) --author Jiangjie <gaojiangjie@live.com>
[main 1df326d1a] [opus] update to v1.5.2 (#40768) (#40771)
 Author: Jiangjie <gaojiangjie@live.com>
 4 files changed, 195 insertions(+)
 create mode 100644 ports/opus/fix-pkgconfig-version.patch
 create mode 100644 ports/opus/portfile.cmake
 create mode 100644 ports/opus/vcpkg.json
 create mode 100644 versions/o-/opus.json
2024-09-22 13:22:36,958 - 360 - WARNING - copy downloads/vcpkg/ports/sdl2 -> ./ports/sdl2
2024-09-22 13:22:36,961 - 369 - WARNING - copy downloads/vcpkg/versions/s-/sdl2.json -> ./versions/s-/sdl2.json
2024-09-22 13:22:36,962 - 382 - INFO - sdl2
commit 274247e63737579340883164b4ac735ab7ddf58e
Author: Oleg Derevenetz <oleg-derevenetz@yandex.ru>
Date:   2024-09-10 06:29:05 +0300

    [sdl2] Update to 2.30.7 (#40843)

 ports/sdl2/poll-fix.patch | 13 -------------
 ports/sdl2/portfile.cmake |  3 +--
 ports/sdl2/vcpkg.json     |  3 +--
 versions/baseline.json    |  4 ++--
 versions/s-/sdl2.json     |  5 +++++
 5 files changed, 9 insertions(+), 19 deletions(-)

2024-09-22 13:22:36,962 - 147 - INFO - run: git add .
2024-09-22 13:22:36,988 - 147 - INFO - run: git commit -m [sdl2] Update to 2.30.7 (#40843) --author Oleg Derevenetz <oleg-derevenetz@yandex.ru>
[main b6f5ff9eb] [sdl2] Update to 2.30.7 (#40843)
 Author: Oleg Derevenetz <oleg-derevenetz@yandex.ru>
 7 files changed, 649 insertions(+)
 create mode 100644 ports/sdl2/alsa-dep-fix.patch
 create mode 100644 ports/sdl2/cxx-linkage-pkgconfig.diff
 create mode 100644 ports/sdl2/deps.patch
 create mode 100644 ports/sdl2/portfile.cmake
 create mode 100644 ports/sdl2/usage
 create mode 100644 ports/sdl2/vcpkg.json
 create mode 100644 versions/s-/sdl2.json
2024-09-22 13:22:37,072 - 360 - WARNING - copy downloads/vcpkg/ports/tesseract -> ./ports/tesseract
2024-09-22 13:22:37,075 - 369 - WARNING - copy downloads/vcpkg/versions/t-/tesseract.json -> ./versions/t-/tesseract.json
2024-09-22 13:22:37,076 - 382 - INFO - tesseract
commit b8a9371ae5a920b021132f443cc5658e82ac7551
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-09-11 23:03:28 +0200

    [curl] Update to 8.10.0 (#40903)

 ports/curl/0020-fix-pc-file.patch      |   8 +-
 ports/curl/0022-deduplicate-libs.patch |  18 ++--
 ports/curl/dependencies.patch          | 152 +++++++++++++++++----------------
 ports/curl/export-components.patch     |  12 +--
 ports/curl/gnutls.patch                |  20 -----
 ports/curl/portfile.cmake              |   6 +-
 ports/curl/vcpkg.json                  |   3 +-
 ports/curlcpp/obsolete-curlopt.diff    |  14 +++
 ports/curlcpp/portfile.cmake           |   1 +
 ports/curlcpp/vcpkg.json               |   1 +
 ports/curlpp/obsolete-curlopt.diff     |  14 +++
 ports/curlpp/portfile.cmake            |   1 +
 ports/curlpp/vcpkg.json                |   2 +-
 ports/tesseract/portfile.cmake         |   1 +
 ports/tesseract/target-curl.diff       |  13 +++
 ports/tesseract/vcpkg.json             |   1 +
 versions/baseline.json                 |  10 +--
 versions/c-/curl.json                  |   5 ++
 versions/c-/curlcpp.json               |   5 ++
 versions/c-/curlpp.json                |   5 ++
 versions/t-/tesseract.json             |   5 ++
 21 files changed, 173 insertions(+), 124 deletions(-)

2024-09-22 13:22:37,076 - 147 - INFO - run: git add .
2024-09-22 13:22:37,101 - 147 - INFO - run: git commit -m [curl] Update to 8.10.0 (#40903) --author Kai Pastor <dg0yt@darc.de>
[main 0f2bc846e] [curl] Update to 8.10.0 (#40903)
 Author: Kai Pastor <dg0yt@darc.de>
 7 files changed, 403 insertions(+)
 create mode 100644 ports/tesseract/fix-link-include-path.patch
 create mode 100644 ports/tesseract/fix-share-build.patch
 create mode 100644 ports/tesseract/fix_static_link_icu.patch
 create mode 100644 ports/tesseract/portfile.cmake
 create mode 100644 ports/tesseract/target-curl.diff
 create mode 100644 ports/tesseract/vcpkg.json
 create mode 100644 versions/t-/tesseract.json
2024-09-22 13:22:37,164 - 360 - WARNING - copy downloads/vcpkg/ports/libjpeg-turbo -> ./ports/libjpeg-turbo
2024-09-22 13:22:37,167 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libjpeg-turbo.json -> ./versions/l-/libjpeg-turbo.json
2024-09-22 13:22:37,169 - 382 - INFO - libjpeg-turbo
commit 20d1b77877b2902722effc7480eda3a78c99ea7f
Author: Clinton Ingram <clinton.ingram@outlook.com>
Date:   2024-09-16 12:45:13 -0700

    [libjpeg-turbo] Update to 3.0.4 (#40991)

 ports/libjpeg-turbo/portfile.cmake | 2 +-
 ports/libjpeg-turbo/vcpkg.json     | 3 +--
 versions/baseline.json             | 4 ++--
 versions/l-/libjpeg-turbo.json     | 5 +++++
 4 files changed, 9 insertions(+), 5 deletions(-)

2024-09-22 13:22:37,169 - 147 - INFO - run: git add .
2024-09-22 13:22:37,194 - 147 - INFO - run: git commit -m [libjpeg-turbo] Update to 3.0.4 (#40991) --author Clinton Ingram <clinton.ingram@outlook.com>
[main c08a43178] [libjpeg-turbo] Update to 3.0.4 (#40991)
 Author: Clinton Ingram <clinton.ingram@outlook.com>
 7 files changed, 616 insertions(+)
 create mode 100644 ports/libjpeg-turbo/add-options-for-exes-docs-headers.patch
 create mode 100644 ports/libjpeg-turbo/portfile.cmake
 create mode 100644 ports/libjpeg-turbo/usage
 create mode 100644 ports/libjpeg-turbo/vcpkg-cmake-wrapper.cmake
 create mode 100644 ports/libjpeg-turbo/vcpkg.json
 create mode 100644 ports/libjpeg-turbo/workaround_cmake_system_processor.patch
 create mode 100644 versions/l-/libjpeg-turbo.json
2024-09-22 13:22:37,255 - 360 - WARNING - copy downloads/vcpkg/ports/wolfssl -> ./ports/wolfssl
2024-09-22 13:22:37,256 - 369 - WARNING - copy downloads/vcpkg/versions/w-/wolfssl.json -> ./versions/w-/wolfssl.json
2024-09-22 13:22:37,257 - 382 - INFO - wolfssl
commit d09d531b03596fc9bc9b1fca6ce40a3c560b2b3d
Author: Matti Regenhardt <69171776+MattiRegenhardt@users.noreply.github.com>
Date:   2024-09-16 21:35:53 +0200

    [wolfssl] Add 'asio' feature flag (#40967)

 ports/wolfssl/portfile.cmake | 7 +++++++
 ports/wolfssl/vcpkg.json     | 5 ++++-
 versions/baseline.json       | 2 +-
 versions/w-/wolfssl.json     | 5 +++++
 4 files changed, 17 insertions(+), 2 deletions(-)

2024-09-22 13:22:37,257 - 147 - INFO - run: git add .
2024-09-22 13:22:37,283 - 147 - INFO - run: git commit -m [wolfssl] Add 'asio' feature flag (#40967) --author Matti Regenhardt <69171776+MattiRegenhardt@users.noreply.github.com>
[main 2b91cd512] [wolfssl] Add 'asio' feature flag (#40967)
 Author: Matti Regenhardt <69171776+MattiRegenhardt@users.noreply.github.com>
 4 files changed, 202 insertions(+)
 create mode 100644 ports/wolfssl/increase-max-alt-names.patch
 create mode 100644 ports/wolfssl/portfile.cmake
 create mode 100644 ports/wolfssl/vcpkg.json
 create mode 100644 versions/w-/wolfssl.json
2024-09-22 13:22:37,345 - 360 - WARNING - copy downloads/vcpkg/ports/libarchive -> ./ports/libarchive
2024-09-22 13:22:37,348 - 369 - WARNING - copy downloads/vcpkg/versions/l-/libarchive.json -> ./versions/l-/libarchive.json
2024-09-22 13:22:37,348 - 382 - INFO - libarchive
commit d8613d01132c94ad48f1d23d83689d63af113450
Author: Mostyn Bramley-Moore <mostyn@antipode.se>
Date:   2024-09-16 21:41:16 +0200

    [libarchive] Update to 3.7.5 (#40998)

 ports/libarchive/portfile.cmake | 2 +-
 ports/libarchive/vcpkg.json     | 2 +-
 versions/baseline.json          | 2 +-
 versions/l-/libarchive.json     | 5 +++++
 4 files changed, 8 insertions(+), 3 deletions(-)

2024-09-22 13:22:37,348 - 147 - INFO - run: git add .
2024-09-22 13:22:37,375 - 147 - INFO - run: git commit -m [libarchive] Update to 3.7.5 (#40998) --author Mostyn Bramley-Moore <mostyn@antipode.se>
[main db97d5f6b] [libarchive] Update to 3.7.5 (#40998)
 Author: Mostyn Bramley-Moore <mostyn@antipode.se>
 9 files changed, 866 insertions(+)
 create mode 100644 ports/libarchive/disable-warnings.patch
 create mode 100644 ports/libarchive/fix-buildsystem.patch
 create mode 100644 ports/libarchive/fix-cpu-set.patch
 create mode 100644 ports/libarchive/fix-deps.patch
 create mode 100644 ports/libarchive/portfile.cmake
 create mode 100644 ports/libarchive/usage
 create mode 100644 ports/libarchive/vcpkg-cmake-wrapper.cmake.in
 create mode 100644 ports/libarchive/vcpkg.json
 create mode 100644 versions/l-/libarchive.json
2024-09-22 13:22:37,435 - 360 - WARNING - copy downloads/vcpkg/ports/tiff -> ./ports/tiff
2024-09-22 13:22:37,438 - 369 - WARNING - copy downloads/vcpkg/versions/t-/tiff.json -> ./versions/t-/tiff.json
2024-09-22 13:22:37,438 - 382 - INFO - tiff
commit eaca68dee685acb55b8cff9b97a9ef2ff325a448
Author: Kai Pastor <dg0yt@darc.de>
Date:   2024-09-18 21:25:20 +0200

    [tiff] Do not use CMAKE_FIND_PACKAGE_PREFER_CONFIG (#40932)

 ports/tiff/portfile.cmake                   |  2 +-
 ports/tiff/prefer-config.diff               | 42 +++++++++++++++++++++++++++++
 ports/tiff/vcpkg.json                       |  2 +-
 scripts/test_ports/vcpkg-ci-gdal/vcpkg.json |  9 +++++++
 versions/baseline.json                      |  2 +-
 versions/t-/tiff.json                       |  5 ++++
 6 files changed, 59 insertions(+), 3 deletions(-)

2024-09-22 13:22:37,438 - 147 - INFO - run: git add .
2024-09-22 13:22:37,465 - 147 - INFO - run: git commit -m [tiff] Do not use CMAKE_FIND_PACKAGE_PREFER_CONFIG (#40932) --author Kai Pastor <dg0yt@darc.de>
[main 3e362e7eb] [tiff] Do not use CMAKE_FIND_PACKAGE_PREFER_CONFIG (#40932)
 Author: Kai Pastor <dg0yt@darc.de>
 8 files changed, 629 insertions(+)
 create mode 100644 ports/tiff/FindCMath.patch
 create mode 100644 ports/tiff/portfile.cmake
 create mode 100644 ports/tiff/prefer-config.diff
 create mode 100644 ports/tiff/requires-lerc.patch
 create mode 100644 ports/tiff/usage
 create mode 100644 ports/tiff/vcpkg-cmake-wrapper.cmake.in
 create mode 100644 ports/tiff/vcpkg.json
 create mode 100644 versions/t-/tiff.json
```
