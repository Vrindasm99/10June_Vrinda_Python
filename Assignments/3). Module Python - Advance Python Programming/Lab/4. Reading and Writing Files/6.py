# Practical Example 6: Write a Python program to check the current position of the file cursor using tell().

FILE_NAME = "cursor_test.txt"

# 1. Setup: Write some data to the file first
with open(FILE_NAME, 'w') as file:
    file.write("ABCDEFGHIJ")

# 2. Read and tell
with open(FILE_NAME, 'r') as file:
    
    # Check current position (should be 0)
    print(f"Initial position: {file.tell()}")
    
    # Read the first 4 characters
    data_read = file.read(4)
    print(f"Read 4 chars: '{data_read}'")
    
    # Check current position (should be 4)
    print(f"Position after reading 4 chars: {file.tell()}")

    # Move cursor to the beginning (position 0)
    file.seek(0) 
    print(f"Position after using seek(0): {file.tell()}")
