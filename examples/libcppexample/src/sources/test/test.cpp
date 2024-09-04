// self
#include <test/test.hpp>

// c
#include <stdio.h>



TestClass::TestClass() {

}


TestClass::~TestClass() {

}


void TestClass::test_func() {
    printf("func: %s, line: %d\n", __FUNCTION__, __LINE__);
}
