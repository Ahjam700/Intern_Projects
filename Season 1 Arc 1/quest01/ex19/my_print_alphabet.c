#include <stdio.h>

// Function to print the alphabet in lowercase (a-z)
void my_print_alphabet() {
    // Loop through the lowercase alphabet (from 'a' to 'z')
    for (char ch = 'a'; ch <= 'z'; ch++) {
        // Print each character
        putchar(ch);
    }
    // Print a newline after the alphabet
    putchar('\n');
}

