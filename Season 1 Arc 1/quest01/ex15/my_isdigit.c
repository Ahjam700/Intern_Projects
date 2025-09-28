#include <stdio.h>

// Function to check if the character is a digit (0-9)
int my_isdigit(char param_1) {
    // Check if the character is between '0' and '9'
    if (param_1 >= '0' && param_1 <= '9') {
        return 1;  // The character is a digit
    }
    else {
        return 0;  // The character is not a digit
    }
}
