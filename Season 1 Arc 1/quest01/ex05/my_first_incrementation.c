#include <stdio.h>

int main() {
  int my_index = 0;

  // increment
  my_index++;  
  printf("%d\n", my_index);
  
  // decrement
  my_index--;  
  // decrement again
  my_index--;  
  printf("%d\n", my_index);

  // increment
  my_index++;  
  // increment again
  my_index++;  
  // increment one more time
  my_index++;  
  printf("%d\n", my_index);

  return 0;
}
