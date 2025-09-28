#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

#define LENGTH_OF_CODE 4
#define DEFAULT_ATTEMPTS 10
#define ASCII_0 '0'
#define BUFFER_SIZE 256

// Function declarations
void generate_random_code(char *code);
int validate_input(const char *input);
void calculate_feedback(const char *guess, const char *code, int *wellplaced, int *misplaced);
void start_game(const char *code, int attempts);
void parse_arguments(int argc, char **argv, char *code, int *attempts);

// Function to generate a random code of digits 0-8, with no repeats
void generate_random_code(char *code) {
    int used[9] = {0};
    int i = 0;

    while (i < LENGTH_OF_CODE) {
        int num = rand() % 9;
        if (!used[num]) {
            code[i++] = ASCII_0 + num;
            used[num] = 1;
        }
    }
    code[LENGTH_OF_CODE] = '\0';
}

// Function to validate user input
int validate_input(const char *input) {
    if (strlen(input) != LENGTH_OF_CODE) {
        return 0;
    }
    for (int i = 0; i < LENGTH_OF_CODE; i++) {
        if (input[i] < '0' || input[i] > '8') {
            return 0;
        }
    }
    return 1;
}

// Function to calculate feedback: well-placed and misplaced digits
void calculate_feedback(const char *guess, const char *code, int *wellplaced, int *misplaced) {
    *wellplaced = 0;
    *misplaced = 0;

    // Arrays to track which digits in both guess and code have been checked
    int checked_code[LENGTH_OF_CODE] = {0};
    int checked_guess[LENGTH_OF_CODE] = {0};

    // First pass: Find well-placed digits
    for (int i = 0; i < LENGTH_OF_CODE; i++) {
        if (guess[i] == code[i]) {
            (*wellplaced)++;
            checked_code[i] = checked_guess[i] = 1; // Mark as checked
        }
    }

    // Second pass: Find misplaced digits
    for (int i = 0; i < LENGTH_OF_CODE; i++) {
        if (!checked_guess[i]) {
            // Search for this guess digit in the code
            for (int j = 0; j < LENGTH_OF_CODE; j++) {
                if (!checked_code[j] && guess[i] == code[j]) {
                    (*misplaced)++;
                    checked_code[j] = 1; // Mark this code digit as checked
                    break; // Move to the next guess digit
                }
            }
        }
    }
}

// Function to start the game
void start_game(const char *code, int attempts) {
    // Display introductory message
    printf("Will you find the secret code?\n");
    printf("Please enter a valid guess\n");

    char guess[BUFFER_SIZE];
    int round = 0;
    char c;

    // Game looping
    while (round < attempts) {
        int valid_input = 0;
        printf("Round %d\n> ", round + 1);

        // Reset guess buffer
        memset(guess, 0, sizeof(guess));

        // Read user input one character at a time
        while (read(STDIN_FILENO, &c, 1) > 0 && c != '\n' && valid_input < LENGTH_OF_CODE) {
            if (c >= '0' && c <= '8') {
                guess[valid_input++] = c;  // Only accept digits between '0' and '8'
            }
        }

        // Handle EOF (Ctrl + D) - exit the game if no input
        if (valid_input == 0) {
            printf("\nGame ended normally (EOF).\n");
            return;
        }

        // Null-terminate the guess string
        guess[valid_input] = '\0';

        // Validate the guess
        if (!validate_input(guess)) {
            // Clear input buffer in case of invalid input
            while (c != '\n' && read(STDIN_FILENO, &c, 1) > 0);
            printf("Please enter a valid guess\n");  // Prompt the user for a valid input
            continue;  // Skip to the next round for a new guess
        }

        // Calculate feedback (well-placed and misplaced digits)
        int wellplaced = 0, misplaced = 0;
        calculate_feedback(guess, code, &wellplaced, &misplaced);

        // Checks if the guess is correct
        if (wellplaced == LENGTH_OF_CODE) {
            printf("Congratz! You did it!\n");  // Success message
            return;  // Game ends when the correct code is guessed
        } else {
            // Provide feedback for the current guess
            printf("Well placed pieces: %d\n", wellplaced);
            printf("Misplaced pieces: %d\n", misplaced);
        }

        // Move to the next round
        round++;
    }

    // End of game, after the maximum number of attempts
    printf("Game over! The secret code was %s\n", code);
}

// Helper function to process command-line arguments
void parse_arguments(int argc, char **argv, char *code, int *attempts) {
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) {
            // Set the specific code passed via -c flag
            strncpy(code, argv[i + 1], LENGTH_OF_CODE);
            code[LENGTH_OF_CODE] = '\0';  // Ensure null-termination
            i++;  // Skip the next argument since it has been processed
        } else if (strcmp(argv[i], "-t") == 0 && i + 1 < argc) {
            // Set the number of attempts via -t flag
            *attempts = atoi(argv[i + 1]);
            i++;  // Skip the next argument as it's already processed
        }
    }
}

// Main function
int main(int argc, char **argv) {
    char code[LENGTH_OF_CODE + 1] = {0};
    int attempts = DEFAULT_ATTEMPTS;

    // Initialize random number generator
    srand((unsigned int) time(NULL));

    // Process command line arguments using the helper function
    parse_arguments(argc, argv, code, &attempts);

    // If no code was provided, generate a random code
    if (code[0] == '\0') {
        generate_random_code(code);
    }

    // Start the game with the chosen code and number of attempts
    start_game(code, attempts);

    return 0;
}


