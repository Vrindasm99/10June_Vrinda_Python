# Practical Example 18: Write a Python program to demonstrate the use of super() in inheritance.
# super() calls the method/constructor of the immediate parent class.

class Parent:
    def __init__(self, message):
        self.message = message
        print(f"Parent __init__ called with: {message}")
        
    def announce(self):
        return f"Parent: {self.message}"

class Child(Parent):
    def __init__(self, message, number):
        # 1. Use super() to call the Parent's __init__
        super().__init__(message) 
        self.number = number

    def announce(self):
        # 2. Use super() to call the Parent's method and add to it
        parent_msg = super().announce()
        return f"{parent_msg} | Child: My number is {self.number}."

# Create a Child object
my_child = Child("Initializing Child Class", 42)

print("--- super() Demonstration ---")
print(my_child.announce())
