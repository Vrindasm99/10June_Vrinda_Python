# Practical Example 5: Write a Python program to read a file and print the data on the console.

FILE_NAME = "my_single_message.txt" # This file should exist from example 3/4

# 'r' mode means "read".
try:
    with open(FILE_NAME, 'r') as file:
        # read() reads the entire content of the file into a single string.
        file_content = file.read()
        
        print(f"--- Contents of {FILE_NAME} ---")
        print(file_content)
        
except FileNotFoundError:
    print(f"Error: The file {FILE_NAME} was not found. Please run the file-writing examples first.")
