# Practical Example 16: Write a Python program to show hierarchical inheritance.
# One Parent class is inherited by multiple Child classes.

# Parent Class
class Shape:
    def dimensions(self):
        return "I have height and width."

# Child Class 1 (inherits from Shape)
class Square(Shape):
    def four_sides(self):
        print("I am a square with four equal sides. " + self.dimensions())

# Child Class 2 (inherits from Shape)
class Triangle(Shape):
    def three_sides(self):
        print("I am a triangle with three sides. " + self.dimensions())

# Create objects
my_square = Square()
my_triangle = Triangle()

print("--- Hierarchical Inheritance ---")
my_square.four_sides()
my_triangle.three_sides()
