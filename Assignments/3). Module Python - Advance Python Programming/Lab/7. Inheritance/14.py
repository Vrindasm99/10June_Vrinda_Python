# Practical Example 14: Write a Python program to show multilevel inheritance.
# Grandparent -> Parent -> Child (three levels)

# 1. Grandparent Class
class Equipment:
    def power_on(self):
        print("Equipment is powered ON.")

# 2. Parent Class (inherits from Equipment)
class Computer(Equipment):
    def run_software(self):
        print("Computer is running software.")

# 3. Child Class (inherits from Computer)
class Laptop(Computer):
    def portability(self):
        print("Laptop is easy to carry.")

# Create a Laptop object
my_laptop = Laptop()

print("--- Multilevel Inheritance ---")
my_laptop.portability()     # From Laptop
my_laptop.run_software()    # From Computer
my_laptop.power_on()        # From Equipment (Grandparent)
