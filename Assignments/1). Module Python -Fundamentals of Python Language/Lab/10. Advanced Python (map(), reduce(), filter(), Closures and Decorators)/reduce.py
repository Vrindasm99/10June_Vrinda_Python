from functools import reduce  

numbers = [1, 2, 3, 4, 5, 6]
# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Apply reduce
product = reduce(multiply, numbers)
print("Product of all numbers using reduce():", product)

