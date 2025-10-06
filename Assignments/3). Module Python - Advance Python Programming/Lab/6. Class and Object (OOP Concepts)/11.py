# Practical Example 11: Write a Python program to create a class and access the properties of the class using an object.

# 1. Define the class
class Person:
    # The __init__ method is the constructor. It sets up the properties (variables) of the object.
    def __init__(self, name, job):
        self.name = name  # Instance property 1
        self.job = job    # Instance property 2

# 2. Create an object (instance) of the class
employee = Person("Alice", "Engineer")

# 3. Access the properties using the object (dot notation)
print("--- Class Property Access ---")
print(f"Object Name: {employee.name}")
print(f"Object Job: {employee.job}")

# You can also change properties later
employee.job = "Senior Engineer"
print(f"New Job: {employee.job}")
