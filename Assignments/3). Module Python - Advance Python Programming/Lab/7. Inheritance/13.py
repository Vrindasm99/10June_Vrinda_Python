# Practical Example 13: Write a Python program to show single inheritance.

# Parent Class
class Animal:
    def eat(self):
        print("This animal is eating.")

# Child Class (Dog inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("The dog barks: Woof!")

# Create a Dog object
my_dog = Dog()

print("--- Single Inheritance ---")
# Dog can use its own method
my_dog.bark()

# Dog can use the inherited method from Animal
my_dog.eat()
