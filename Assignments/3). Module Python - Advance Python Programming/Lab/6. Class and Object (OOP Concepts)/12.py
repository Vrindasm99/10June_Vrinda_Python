# Practical Example 12: Write a Python program to demonstrate the use of local and global variables in a class.

class Calculator:
    # 1. Global/Class Variable (Shared by all objects)
    VERSION = 1.0 
    
    def __init__(self, starting_value):
        # Instance Variable (Unique to each object)
        self.current_value = starting_value

    def add(self, num1, num2):
        # 2. Local Variable (Only exists inside this method)
        sum_result = num1 + num2
        
        # Accessing the instance variable and updating it
        self.current_value = self.current_value + sum_result
        
        # Accessing the Class Variable
        print(f"--- Calculation Complete (v{Calculator.VERSION}) ---")
        print(f"Local Sum: {sum_result}")
        print(f"New Instance Value: {self.current_value}")


calc_obj = Calculator(100)
calc_obj.add(5, 3) 
