#include <stdio.h>

// Function to check if the character is a letter (A-Z or a-z)
int my_isalpha(char param_1) {
    // Check if the character is between 'A' and 'Z' or between 'a' and 'z'
    if ((param_1 >= 'A' && param_1 <= 'Z') || (param_1 >= 'a' && param_1 <= 'z')) {
        return 1;  // The character is a letter
    }
    else {
        return 0;  // The character is not a letter
    }
}


