#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// Top and bottom lines
void top_and_bottom(int x, int y) {
    
    int i;

    if (x > 0) {
        printf("o");
        for (i = 0; i < x - 2; i++) // This prints dash("-")
        {
            printf("-");
        }
        if (x > 1) {
            printf("o");
        }
    }
}

// The middle lines
void print_middle_line(int x, int y, int newLines) {
    
    int i;

    while (newLines > 0) {
        printf("|");
        for (i = 0; i < x - 2; i++) {
            printf(" "); // space between each vertical line
        }
        if (x > 1) {
            printf("|");
        }
        printf("\n");
        newLines--; // decrease number of newlines space
    }
}

int main(int ac, char **av) {
    if (ac != 3) {
        return 0;  // 3 command line arguments expected here. anthing less or above return 0
    }

    int x = atoi(av[1]); // base lenght
    int y = atoi(av[2]); // height

    // check for incorrect inputs
    if (x <= 0 || y <= 0) {
        return 0;
    }

    // if x & y = 1 (a single 'o')
    if (x == 1 && y == 1) {
        printf("o\n");
        return 0;
    }

    // if x = 1, y = 0, just print vertical bars
    if (x == 1) {
        for (int i = 0; i < y; i++) {
            printf("o\n");
        }
        return 0;
    }

    // if y = 1, x = 0, print top and bottom line only
    if (y == 1) {
        top_and_bottom(x, y);
        printf("\n");
        return 0;
    }

    // Printing of the top line
    top_and_bottom(x, y);
    printf("\n");

    // Printing the middle lines
    int newLines = y - 2;  // excluding the first and last line
    print_middle_line(x, y, newLines);

    // Printing the bottom line
    top_and_bottom(x, y);
    printf("\n");

    return 0;
}
