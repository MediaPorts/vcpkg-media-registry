// test
#include <test/test.hpp>

// libcexample
#include <libcexample/test.h>

// libcppexample
#include <libcppexample/test.hpp>


int main(int argc, char **argv)
{
    my_test_func();
    MyTestClass().my_test_func();

    test_func();

    TestClass().test_func();
}
