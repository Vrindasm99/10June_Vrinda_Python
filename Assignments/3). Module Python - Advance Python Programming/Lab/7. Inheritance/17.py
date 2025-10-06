# Practical Example 17: Write a Python program to show hybrid inheritance.
# This is a combination of two or more types (e.g., Multilevel + Multiple).

# 1. Base (Top of Multilevel)
class Vehicle:
    def drive(self):
        return "Vehicle is moving."

# 2. Mid-level (Multilevel branch)
class Car(Vehicle):
    def four_wheels(self):
        return "Car has four wheels."

# 3. Separate Base (Multiple branch)
class Electric:
    def zero_emissions(self):
        return "Electric has zero emissions."

# 4. Child (inherits from Car and Electric)
class Tesla(Car, Electric):
    """Hybrid: Multilevel (Vehicle->Car) combined with Multiple (Car + Electric -> Tesla)"""
    def info(self):
        print(f"Tesla info: {self.drive()}, {self.four_wheels()}, and {self.zero_emissions()}")

my_tesla = Tesla()

print("--- Hybrid Inheritance ---")
my_tesla.info()
