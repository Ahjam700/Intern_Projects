#include <stdio.h>

void my_putstr(char* param_1) {
    // Loop through the string until we reach the null terminator
    while (*param_1 != '\0') {
        putchar(*param_1);  // Print the current character
        param_1++;          // Move to the next character in the string
    }
}
