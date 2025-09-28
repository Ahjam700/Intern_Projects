# Welcome to My Printf
This project is a custom implementation of the printf function in C. The goal is to mimic the functionality of the
standard printf by processing format specifiers, handling variable arguments, and printing the result to the console.

## Task
What is the problem? And where is the challenge?
The problem is to create a custom printf function from scratch, replicating key features like variable argument
handling and specific format specifiers. The challenge lies in managing different data types, handling edge cases,
and implementing efficient output.

## Description
How have you solved the problem?
I solved the problem by utilizing va_list for handling variable arguments, va_start, and va_end to manage the
argument list. Each format specifier %d , %x , %s, etc. was processed individually, formatting and printing data
accordingly.

## Installation
How to install your project? npm install? make? make re?
To install and compile the project, clone the repository and run gcc my_printf.c -o my_printf. This project doesnt
require npm install or make commands. Simply use a C compiler to build it.

## Usage
How does it work?
The function reads the format string and processes it character by character. When encountering a format specifier,
it uses va_arg to extract the corresponding argument, formats it, and outputs the result using write.

```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
