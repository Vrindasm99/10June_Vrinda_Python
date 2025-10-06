# Practical Example 7: Write a Python program to handle exceptions in a simple calculator (division by zero).

def simple_divide(a, b):
    # Use a try block for code that might cause an error
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    
    # Use an except block to catch a specific error (ZeroDivisionError)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")

print("--- Calculator Exception Handling ---")
simple_divide(10, 5) # Works fine
simple_divide(10, 0) # Causes the exception
