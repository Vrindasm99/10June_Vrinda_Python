# Practical Example 19: Write a Python program to show method overloading.
# Python does not support true method overloading, so we use default arguments to simulate it.

class Calculator:
    
    # We define one function that can accept 1, 2, or 3 arguments using default values (b=0, c=0).
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print("--- Method Overloading (Simulated) ---")
# Call 1: One argument (b=0, c=0 are used)
print(f"Add (10): {calc.add(10)}")

# Call 2: Two arguments (c=0 is used)
print(f"Add (10, 5): {calc.add(10, 5)}")

# Call 3: Three arguments
print(f"Add (10, 5, 2): {calc.add(10, 5, 2)}")
