#include <stdio.h>

// Function to print the alphabet in lowercase in descending order (z-a)
void my_print_reverse_alphabet() {
    // Loop from 'z' to 'a'
    for (char ch = 'z'; ch >= 'a'; ch--) {
        // Print each character
        putchar(ch);
    }
    // Print a newline after the alphabet
    putchar('\n');
}

