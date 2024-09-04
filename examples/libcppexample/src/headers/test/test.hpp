#pragma once


#ifndef BUILD_SHARED_LIBS
    #define LIBCPPEXAMPLE_API
#else
    #ifdef _WIN32
        #ifdef LIBCPPEXAMPLE_EXPORTS
            #define LIBCPPEXAMPLE_API __declspec(dllexport)
        #else
            #define LIBCPPEXAMPLE_API __declspec(dllimport)
        #endif
    #elif defined(__GNUC__) || defined(__clang__)
        #define LIBCPPEXAMPLE_API __attribute__((visibility("default")))
    #else
        #define LIBCPPEXAMPLE_API
    #endif
#endif


class LIBCPPEXAMPLE_API TestClass {
public:
    TestClass();
    ~TestClass();

    void test_func();
};
