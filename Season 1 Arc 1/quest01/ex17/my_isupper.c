#include <stdio.h>

// Function to check if the character is an uppercase letter (A-Z)
int my_isupper(char param_1) {
    // Check if the character is between 'A' and 'Z'
    if (param_1 >= 'A' && param_1 <= 'Z') {
        return 1;  // The character is an uppercase letter
    }
    else {
        return 0;  // The character is not an uppercase letter
    }
}

