#include <stdio.h>
#include <stdlib.h>
#define MAX_ARRAY_SIZE 128

// update the frequency array after processing a single string  
void update_frequency(int array[], const char *str) {
    while (*str != '\0') {  // Loop through the end of the string
        if (*str != '"') {  // Skip all double-quote characters found
            array[(unsigned char)*str]++; // add the frequency of the character
        }
        str++;  // move to the next char/letter
    }
}

// printing characters with their frequencies
void display_frequency(const int array[]) {
    for (int i = 0; i < MAX_ARRAY_SIZE; i++) {
        if (array[i] > 0) {  // print available characters present
            printf("%c:%d\n", i, array[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    int frequency[MAX_ARRAY_SIZE] = {0}; // Frequency array initialized to zero

    // Process each command-line argument
    for (int i = 1; i < argc; i++) {
        update_frequency(frequency, argv[i]);
    }

    // show the frequencies of the characters
    display_frequency(frequency);

    return EXIT_SUCCESS;
}
