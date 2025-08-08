from functools import reduce  # Import required for reduce()

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Define a function to check for odd numbers
def is_odd(num):
    return num % 2 != 0

# Apply filter
odd_numbers = list(filter(is_odd, numbers))
print("Odd Numbers using filter():", odd_numbers)
