cmake_minimum_required(VERSION 3.20)

project(testregistry CXX)


#######################################################################################################################
# Configure Visual Studio
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
# Check
#######################################################################################################################
# version
set(TEST_REGISTRY_VERSION_MAJOR 0)
set(TEST_REGISTRY_VERSION_MINOR 0)
set(TEST_REGISTRY_VERSION_MICRO 1)
set(TEST_REGISTRY_VERSION "${TEST_REGISTRY_VERSION_MAJOR}.${TEST_REGISTRY_VERSION_MINOR}.${TEST_REGISTRY_VERSION_MICRO}")

# check headers
include(CheckIncludeFiles)
check_include_files("stdlib.h" HAVE_STDLIB_H)

# check types
include(CheckTypeSize)
# check_type_size(size_t SIZE_T)

# check functions
include(CheckFunctionExists)
check_function_exists(gettimeofday HAVE_GETTIMEOFDAY)

# check symbols
include(CheckSymbolExists)
check_symbol_exists(O_BINARY "fcntl.h" HAVE_O_BINARY)


#######################################################################################################################
# Package
#######################################################################################################################
include(CMakePackageConfigHelpers)
set(PACKAGE ${PROJECT_NAME})
set(PACKAGE_NAME ${PROJECT_NAME})
set(PACKAGE_STRING "${PROJECT_NAME} ${TEST_REGISTRY_VERSION}")
set(PACKAGE_TARNAME ${PROJECT_NAME})
set(PACKAGE_URL "http://192.168.3.198/vcpkg_wtoe_registry/examples/testregistry")
set(PACKAGE_VERSION ${TEST_REGISTRY_VERSION})
set(STDC_HEADERS 1)
set(SUPPORT_ATTRIBUTE_VISIBILITY_DEFAULT 1)
set(SUPPORT_FLAG_VISIBILITY 1)
set(VERSION ${TEST_REGISTRY_VERSION})


#######################################################################################################################
# Generate platform config and version header according to check results
#######################################################################################################################
# platform config.h
configure_file(${CMAKE_SOURCE_DIR}/src/config.h.cm ${CMAKE_BINARY_DIR}/config.h)

# version.h
configure_file(${CMAKE_SOURCE_DIR}/src/version.h.in ${CMAKE_BINARY_DIR}/version.h @ONLY)


#######################################################################################################################
# Sources
#######################################################################################################################
# glob headers and sources
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
# classify
SOURCE_GROUP("headers/conf" FILES ${HEADER_FILES_CONF})
SOURCE_GROUP("headers/test" FILES ${HEADER_FILES_TEST})
SOURCE_GROUP("sources/test" FILES ${SOURCE_FILES_TEST})
SOURCE_GROUP("sources/main" FILES ${SOURCE_FILES_MAIN})

# find deps
find_package(libcexample CONFIG REQUIRED)
find_package(libcppexample CONFIG REQUIRED)

# generate executable
add_executable(${PROJECT_NAME}
    ${HEADER_FILES_CONF}
    ${HEADER_FILES_TEST}
    ${SOURCE_FILES_TEST}
    ${SOURCE_FILES_MAIN}
)

# set include paths
target_include_directories(${PROJECT_NAME}
  PRIVATE
  "src/headers"
  ${CMAKE_CURRENT_BINARY_DIR}
)

# link libraries
target_link_libraries(
        ${PROJECT_NAME}
        PRIVATE
        libcexample::libcexample
        libcppexample::libcppexample
)

if(MSVC)
  # defines
  add_definitions(-DPATH_MAX=1024)
  add_definitions(-D_CRT_SECURE_NO_WARNINGS)

  # fix windows uwp link errors
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
# Support CMake find-package
#######################################################################################################################
# install bin
install(
    TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}-targets
    RUNTIME DESTINATION bin
)

