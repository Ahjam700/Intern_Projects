#include <stdio.h>


int my_strlen(char* param_1) {
    int length = 0;
    
    // Loop through the string until we encounter the null terminator
    while (param_1[length] != '\0') {
        length++;
    }
    
    return length;
}

