# Practical Example 9: Write a Python program to handle file exceptions and use the finally block for closing the file.

# Using a standard open/close is better for demonstrating 'finally' than 'with open'

file_handle = None # Initialize outside the try block

try:
    # This will fail
    file_handle = open("temp_log.txt", "r")
    content = file_handle.read()

except FileNotFoundError:
    print("Caught FileNotFoundError: File was not opened.")

finally:
    # The code in finally ALWAYS runs, whether an error occurred or not.
    # This guarantees the file is closed if it was successfully opened.
    if file_handle:
        file_handle.close()
        print("Finally block executed: File closed successfully.")
    else:
        print("Finally block executed: File handle was never opened.")
