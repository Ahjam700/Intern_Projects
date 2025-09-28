#include <stdio.h>

// Function to return the absolute value of an integer
int my_abs(int param_1) {
    if (param_1 < 0) {
        return -param_1;  // If negative, return positive value by negating
    }
    else {
        return param_1;   // If positive or zero, return the number as is
    }
}

