# Practical Example 3 & 4: Write a Python program to create a file and write a string into it.

FILE_NAME = "my_single_message.txt"

# The 'w' mode means "write" (it creates the file or overwrites existing content).
# 'with open' is the simplest and safest way to open and close a file.
with open(FILE_NAME, 'w') as file:
    file.write("This is the required string written to the file.\n")
    
print(f"Successfully wrote a single string to {FILE_NAME}")


# Lab Task: Write multiple strings into a file.

FILE_NAME = "my_multiple_messages.txt"

lines = [
    "First line of my list.",
    "Second line about Python.",
    "Third and final line."
]

# 'w' mode creates/overwrites the file.
with open(FILE_NAME, 'w') as file:
    for line in lines:
        file.write(line + '\n')
    
print(f"Successfully wrote {len(lines)} lines to {FILE_NAME}")
