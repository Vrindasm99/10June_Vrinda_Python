# Practical Example 20: Write a Python program to show method overriding.
# Child class defines a method with the exact same name as the Parent class.

class Animal:
    def make_sound(self):
        # Base implementation
        return "Generic animal noise."

class Cat(Animal):
    def make_sound(self):
        # Overridden implementation (replaces the parent's method)
        return "Meow!"

class Dog(Animal):
    def make_sound(self):
        # Overridden implementation
        return "Woof woof!"

# Create objects
animal = Animal()
cat = Cat()
dog = Dog()

print("--- Method Overriding ---")
print(f"Animal sound: {animal.make_sound()}")
print(f"Cat sound: {cat.make_sound()}")
print(f"Dog sound: {dog.make_sound()}")
