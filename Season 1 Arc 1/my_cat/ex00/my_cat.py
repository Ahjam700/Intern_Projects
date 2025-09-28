import sys

for filename in sys.argv[1:]:
    with open(filename, "r") as file:
        sys.stdout.write(file.read())

