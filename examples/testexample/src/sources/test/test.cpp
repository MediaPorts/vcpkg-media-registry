// self
#include <test/test.hpp>

// c
#include <stdio.h>



void my_test_func() {
    printf("func: %s, line: %d\n", __FUNCTION__, __LINE__);
}



MyTestClass::MyTestClass() {

}


MyTestClass::~MyTestClass() {

}


void MyTestClass::my_test_func() {
    printf("func: %s, line: %d\n", __FUNCTION__, __LINE__);
}
