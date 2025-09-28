#include <stdio.h>

// Function to check if the character is a lowercase letter (a-z)
int my_islower(char param_1) {
    // Check if the character is between 'a' and 'z'
    if (param_1 >= 'a' && param_1 <= 'z') {
        return 1;  // The character is a lowercase letter
    }
    else {
        return 0;  // The character is not a lowercase letter
    }
}

