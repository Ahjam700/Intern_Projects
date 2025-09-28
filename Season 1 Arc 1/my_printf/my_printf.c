#include <unistd.h>
#include <stdarg.h>
#include <stdio.h>
#include <string.h>

int my_printf(const char *format, ...) {
    va_list args_list;

    va_start(args_list, format);

    int total_chars_written = 0;
    while (*format) {
        if (*format == '%') {
            format++; 
            char current_char = *format;
            
            switch (current_char) { 
                case 'd': {
                    int value = va_arg(args_list, int); 
                    if (value < 0) { 
                        total_chars_written += write(1, "-", 1);
                        value = -value;
                    } 
                    
                    if (value == 0) { 
                        total_chars_written += write(1, "0", 1);
                        break;
                    }
                    char num_buffer[32];
                    char *num_ptr = num_buffer + 31;
                    *num_ptr = '\0';
                    while (value > 0) { 
                        *--num_ptr = value % 10 + '0';
                        value /= 10;
                    }
                    total_chars_written += write(1, num_ptr, strlen(num_ptr)); 
                    break;
                }
                case 'o': { 
                    unsigned int oct_value = va_arg(args_list, unsigned int); 
                    char oct_buffer[32];
                    char *oct_ptr = oct_buffer + 31;
                    *oct_ptr = '\0';
                    while (oct_value > 0) { 
                        *--oct_ptr = oct_value % 8 + '0';
                        oct_value /= 8;
                    }
                    total_chars_written += write(1, oct_ptr, strlen(oct_ptr)); 
                    break;
                }
                case 'u': { 
                    unsigned int unsigned_val = va_arg(args_list, unsigned int); 
                    char unsigned_buffer[32];
                    char *unsigned_ptr = unsigned_buffer + 31;
                    *unsigned_ptr = '\0';
                    while (unsigned_val > 0) { 
                        *--unsigned_ptr = unsigned_val % 10 + '0';
                        unsigned_val /= 10;
                    }
                    total_chars_written += write(1, unsigned_ptr, strlen(unsigned_ptr)); 
                    break;
                }
                case 'x': { 
                    unsigned int hex_val = va_arg(args_list, unsigned int); 
                    char hex_buffer[32];
                    char *hex_ptr = hex_buffer + 31;
                    *hex_ptr = '\0';
                    while (hex_val > 0) { 
                        char hex_digit = hex_val % 16;
                        if (hex_digit < 10) {
                            *--hex_ptr = hex_digit + '0';
                        } else {
                            *--hex_ptr = hex_digit - 10 + 'A'; 
                        }
                        hex_val /= 16;
                    }
                    total_chars_written += write(1, hex_ptr, strlen(hex_ptr)); 
                    break;
                }
                case 'c': {
                    char char_val = va_arg(args_list, int);
                    total_chars_written += write(1, &char_val, 1);
                    break;
                }
                case 's' : {
                    const char *str_val = va_arg(args_list, const char*);
                    if (str_val == NULL) {
                        total_chars_written += write(1, "(null)", 6);
                    } else {
                        total_chars_written += write(1, str_val, strlen(str_val));
                    }
                    break;
                }
                case 'p' : {
                    void *ptr_val = va_arg(args_list, void*);
                    unsigned long long address_val = (unsigned long long)ptr_val;
                    char address_buffer[32];
                    char *address_ptr = address_buffer + 31;
                    *address_ptr = '\0';
                    while (address_val > 0) {
                        char address_digit = address_val % 16;
                        if (address_digit < 10) {
                            *--address_ptr = address_digit + '0';
                        } else {
                            *--address_ptr = address_digit - 10 + 'a';
                        }
                        address_val /= 16;
                    }
                    total_chars_written += write(1, "0x", 2);
                    total_chars_written += write(1, address_ptr, strlen(address_ptr));
                    break;
                }
            }
        } else {
            total_chars_written += write(1, format, 1);
        }
        format++;
    }

    va_end(args_list);
    return total_chars_written;
}
