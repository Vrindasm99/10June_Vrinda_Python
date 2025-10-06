# Practical Example 10: Write a Python program to print custom exceptions.

# 1. Define a simple custom exception class
# It must inherit from the base 'Exception' class.
class NegativeInputError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Error: Input value cannot be negative. Got: {value}")


def process_value(number):
    if number < 0:
        # 2. Raise the custom exception
        raise NegativeInputError(number)
    else:
        print(f"Success: Processing positive value {number}")


print("--- Custom Exception Demonstration ---")
# Test 1: Success
process_value(10) 

# Test 2: Failure (raises custom exception)
try:
    process_value(-5)
except NegativeInputError as e:
    # 3. Print the custom exception message
    print(f"\nCaught Exception: {e}")
