# Practical Example 3 & 4: Write a Python program to create a file and write a string into it.

FILE_NAME = "my_single_message.txt"

# The 'w' mode means "write" (it creates the file or overwrites existing content).
# 'with open' is the simplest and safest way to open and close a file.
with open(FILE_NAME, 'w') as file:
    file.write("This is the required string written to the file.\n")
    
print(f"Successfully wrote a single string to {FILE_NAME}")

