# Variables
CC = gcc
CFLAGS = -Wall -Wextra -Werror
TARGET = my_ngram
SRC = my_ngram.c
OBJ = $(SRC:.c=.o)

# Rules
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

$(OBJ): $(SRC)
	$(CC) $(CFLAGS) -c $(SRC)

clean:
	rm -f *.o

fclean: clean
	rm -f $(TARGET)

re: fclean all
