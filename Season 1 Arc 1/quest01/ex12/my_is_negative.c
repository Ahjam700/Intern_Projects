#include <stdio.h>

// Function to check if the number is negative or non-negative
int my_is_negative(int param_1) {
    if (param_1 < 0) {
        return 0;  // Return 0 if the number is negative
    }
    else {
        return 1;  // Return 1 if the number is positive or zero
    }
}


