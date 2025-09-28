import sys

# Check if any arguments were provided
if len(sys.argv) > 1:
    # Print each argument received
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("No arguments provided.")
