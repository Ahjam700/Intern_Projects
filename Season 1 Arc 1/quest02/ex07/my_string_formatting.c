#include <stdio.h>
#include <string.h>

void my_string_formatting(char* param_1, char* param_2, int param_3) {
    int len1 = strlen(param_1);      // Length of param_1
    int len2 = strlen(param_2);      // Length of param_2

    // Ensure param_3 is not larger than the length of param_2
    int num_chars_to_add = (param_3 < len2) ? param_3 : len2;

    // Append the first 'param_3' characters of param_2 to param_1
    for (int i = 0; i < num_chars_to_add; i++) {
        param_1[len1 + i] = param_2[i];
    }

    // Null-terminate the new string
    param_1[len1 + num_chars_to_add] = '\0';
}

