# ----------------------------------------
# Practical Example 1: Python Code Structure
# ----------------------------------------

# This is the main starting point of the code.
# Python executes code line-by-line, top to bottom.

print("Welcome to the Python Variable Demo!")

# ----------------------------------------
# Practical Example 2: Creating Variables and Using Different Data Types
# ----------------------------------------

# Integer variable
age = 25

# Float variable
height = 5.7

# String variable
name = "Alice"

# Boolean variable
is_student = True

# Display the variables
print("\nStored Values:")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Height     : {height}")
print(f"Is Student : {is_student}")

# ----------------------------------------
# Practical Example 3: Taking User Input Using input()
# ----------------------------------------

# Asking for user's favorite color
favorite_color = input("\nWhat is your favorite color? ")

# Asking for user's birth year and converting it to integer
birth_year = int(input("Enter your birth year: "))

# Calculating age based on current year
current_year = 2025
calculated_age = current_year - birth_year

print(f"You like {favorite_color}, and you are around {calculated_age} years old.")

# ----------------------------------------
# Practical Example 4: Checking the Type of Variables Using type()
# ----------------------------------------

print("\nData Types of Variables:")
print(f"type(name)           : {type(name)}")
print(f"type(age)            : {type(age)}")
print(f"type(height)         : {type(height)}")
print(f"type(is_student)     : {type(is_student)}")
print(f"type(favorite_color) : {type(favorite_color)}")
print(f"type(birth_year)     : {type(birth_year)}")
print(f"type(calculated_age) : {type(calculated_age)}")
