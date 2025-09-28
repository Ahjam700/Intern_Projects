#include <stdio.h>

// Function that prints the detonation message with seconds left
void detonation_in(int seconds_left) {
    printf("detonation in... %d seconds.\n", seconds_left);
}

int main() {
    int timer = 10;

    // Loop will run as long as timer is greater than 0
    while (timer > 0) {
        detonation_in(timer);  // Call the function with current timer value
        timer--;  // Decrement the timer
    }

    return 0;
}
