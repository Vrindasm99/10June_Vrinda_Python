# Practical Example 15: Write a Python program to show multiple inheritance.
# Child inherits from two or more separate Parent classes.

# Parent Class 1
class Swimmer:
    def ability_a(self):
        return "I can swim."

# Parent Class 2
class Walker:
    def ability_b(self):
        return "I can walk."

# Child Class (inherits from both Swimmer and Walker)
class Human(Swimmer, Walker):
    def describe(self):
        # Access methods from both parents
        print(f"A human. {self.ability_a()} and {self.ability_b()}")

# Create a Human object
person = Human()

print("--- Multiple Inheritance ---")
person.describe()
