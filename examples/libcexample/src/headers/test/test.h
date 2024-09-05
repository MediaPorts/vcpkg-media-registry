#pragma once


#ifndef BUILD_SHARED_LIBS
    #define LIBCEXAMPLE_API
#else
    #ifdef _WIN32
        #ifdef LIBCEXAMPLE_EXPORTS
            #define LIBCEXAMPLE_API __declspec(dllexport)
        #else
            #define LIBCEXAMPLE_API __declspec(dllimport)
        #endif
    #elif defined(__GNUC__) || defined(__clang__)
        #define LIBCEXAMPLE_API __attribute__((visibility("default")))
    #else
        #define LIBCEXAMPLE_API
    #endif
#endif


#ifdef __cplusplus
extern "C" {
#endif

LIBCEXAMPLE_API void test_func();

#ifdef __cplusplus
}
#endif
