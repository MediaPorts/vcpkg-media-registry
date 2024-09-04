# CMake最低版本要求
cmake_minimum_required(VERSION 3.20)

# 项目名称，编程语言
project(testexample CXX)


#######################################################################################################################
# Visual Studio配置
#######################################################################################################################
if(MSVC)
    # utf-8 source code encoding
    add_compile_options("$<$<C_COMPILER_ID:MSVC>:/utf-8>")
    add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>")

    # Visual Stuido - Properity - C/C++ - General - Debug Informat Format > Program Database (/Zi)
    set(CMAKE_CXX_FLAGS_DEBUUG "${CMAKE_CXX_FLAGS_DEBUG} /Zi /Od")  # Disable Optimization
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /Zi /O1")  # Favor Size

    # Visual Stuido - Properity - Linker - Debugging - Generate Debug Info > Generate Debug Information (/Debug)
    set(CMAKE_EXE_LINKER_FLAGS_DEBUUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} /DEBUG /OPT:REF /OPT:ICF")
    set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} /DEBUG /OPT:REF /OPT:ICF")

    # Visual Stuido - Properity - Linker - Debugging - Generate Debug Info > Generate Debug Information (/Debug)
    set(CMAKE_SHARED_LINKER_FLAGS_DEBUUG "${CMAKE_SHARED_LINKER_FLAGS_DEBUG} /DEBUG /OPT:REF /OPT:ICF")
    set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} /DEBUG /OPT:REF /OPT:ICF")
endif(MSVC)


#######################################################################################################################
# 检查 (类型于configure脚本)
#######################################################################################################################
# 项目版本
set(TEST_EXAMPLE_VERSION_MAJOR 0)
set(TEST_EXAMPLE_VERSION_MINOR 0)
set(TEST_EXAMPLE_VERSION_MICRO 1)
set(TEST_EXAMPLE_VERSION "${TEST_EXAMPLE_VERSION_MAJOR}.${TEST_EXAMPLE_VERSION_MINOR}.${TEST_EXAMPLE_VERSION_MICRO}")

set(TEST_EXAMPLE_GIT_COMMIT_HASH "aaaa")
set(TEST_EXAMPLE_GIT_COMMIT_DATE_TIME "bbbbb")
set(TEST_EXAMPLE_GIT_COMMIT_MESSAGE "ccccc")
set(TEST_EXAMPLE_BUILD_DATETIME "ddddd")

# 导入CMake头文件检查
include(CheckIncludeFiles)
# 检查stdlib.h是否存在
check_include_files("stdlib.h" HAVE_STDLIB_H)

# 导入CMake数据类型长度检查
include(CheckTypeSize)
# # 检查size_t长度并设置set_t类型
# check_type_size(size_t SIZE_T)
# if(NOT HAVE_SIZE_T)
#   if("${CMAKE_SIZEOF_VOID_P}" EQUAL 8)
#     set(size_t "uint64_t")
#   else("${CMAKE_SIZEOF_VOID_P}" EQUAL 8)
#     set(size_t   "uint32_t")
#   endif("${CMAKE_SIZEOF_VOID_P}" EQUAL 8)
# endif(NOT HAVE_SIZE_T)

# 导入CMake函数检查
include(CheckFunctionExists)
# 检查gettimeofday是否存在
check_function_exists(gettimeofday HAVE_GETTIMEOFDAY)

# 导入CMake符号检查
include(CheckSymbolExists)
# 检查O_BINARY是否存在
check_symbol_exists(O_BINARY "fcntl.h" HAVE_O_BINARY)


#######################################################################################################################
# 包
#######################################################################################################################
# 导入CMake包生成辅助
include(CMakePackageConfigHelpers)
# 配置包
set(PACKAGE ${PROJECT_NAME})
set(PACKAGE_NAME ${PROJECT_NAME})
set(PACKAGE_STRING "${PROJECT_NAME} ${TEST_EXAMPLE_VERSION}")
set(PACKAGE_TARNAME ${PROJECT_NAME})
set(PACKAGE_URL "http://192.168.3.198/vcpkg_wtoe_registry/examples/c_cpp_bin")
set(PACKAGE_VERSION ${TEST_EXAMPLE_VERSION})
set(STDC_HEADERS 1)
set(SUPPORT_ATTRIBUTE_VISIBILITY_DEFAULT 1)
set(SUPPORT_FLAG_VISIBILITY 1)
set(VERSION ${TEST_EXAMPLE_VERSION})


#######################################################################################################################
# 填充跨平台条件检查头文件和版本头文件
#######################################################################################################################
# 根据上面的configure结果和模板生成config.h
configure_file(${CMAKE_SOURCE_DIR}/src/config.h.cm ${CMAKE_BINARY_DIR}/config.h)

# 根据定义的版本和模板生成version.h
configure_file(${CMAKE_SOURCE_DIR}/src/version.h.in ${CMAKE_BINARY_DIR}/version.h @ONLY)


#######################################################################################################################
# 源码
#######################################################################################################################
# 源码搜集
FILE(GLOB_RECURSE HEADER_FILES_CONF
    ${CMAKE_BINARY_DIR}/config.h
    ${CMAKE_BINARY_DIR}/version.h
)
FILE(GLOB_RECURSE HEADER_FILES_TEST
    "src/headers/test/*.hpp"
)
FILE(GLOB_RECURSE SOURCE_FILES_TEST
    "src/sources/test/*.cpp"
)
FILE(GLOB_RECURSE SOURCE_FILES_MAIN
    "src/*.cpp"
)
# 源码归类
SOURCE_GROUP("headers/conf" FILES ${HEADER_FILES_CONF})
SOURCE_GROUP("headers/test" FILES ${HEADER_FILES_TEST})
SOURCE_GROUP("sources/test" FILES ${SOURCE_FILES_TEST})
SOURCE_GROUP("sources/main" FILES ${SOURCE_FILES_MAIN})

# 查找依赖
find_package(libcexample CONFIG REQUIRED)
find_package(libcppexample CONFIG REQUIRED)

# 生成可执行文件
add_executable(${PROJECT_NAME}
    ${HEADER_FILES_CONF}
    ${HEADER_FILES_TEST}
    ${SOURCE_FILES_TEST}
    ${SOURCE_FILES_MAIN}
)

# 指定头文件搜索位置
target_include_directories(${PROJECT_NAME}
  PRIVATE
  "src/headers"
  ${CMAKE_CURRENT_BINARY_DIR}
)

# 链接指定库
target_link_libraries(
        ${PROJECT_NAME}
        PRIVATE
        libcexample::libcexample
        libcppexample::libcppexample
)

if(MSVC)
  # 宏定义
  target_compile_definitions(${PROJECT_NAME}
    PRIVATE 
      _CRT_SECURE_NO_WARNINGS
      PATH_MAX=1024
  )
  # Windows UWP库链接支持
  if(CMAKE_SYSTEM_NAME STREQUAL WindowsStore)
    set_target_properties(${PROJECT_NAME}
        PROPERTIES
          LINK_FLAGS_DEBUG "/defaultlib:vccorlibd.lib /defaultlib:msvcrtd.lib"
          LINK_FLAGS_RELEASE "/defaultlib:vccorlib.lib /defaultlib:msvcrt.lib"
          LINK_FLAGS_RELWITHDEBINFO "/defaultlib:vccorlib.lib /defaultlib:msvcrt.lib"
    )
  endif()
endif()


#######################################################################################################################
# 安装
#######################################################################################################################
# 安装lib和bin位置
install(
    TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}-targets
    RUNTIME DESTINATION bin
)

