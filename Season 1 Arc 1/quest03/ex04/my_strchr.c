#include <stdio.h>
#include <string.h>

char* my_strchr( const char str[], char ch ) 
{
    while ( *str && *str != ch ) ++str;

    return ( char * )( ch == *str ? str : 0 );  
}