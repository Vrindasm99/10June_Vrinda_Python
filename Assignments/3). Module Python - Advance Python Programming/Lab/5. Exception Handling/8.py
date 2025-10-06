# Practical Example 8: Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def handle_errors(mode):
    try:
        if mode == "file":
            # This line causes a FileNotFoundError
            file = open("non_existent_file.txt", "r")
            file.close() 
            
        elif mode == "math":
            # This line causes a ZeroDivisionError
            result = 10 / 0 
            
        elif mode == "type":
            # This line causes a TypeError
            result = "hello" + 5
            
    # Handle specific exceptions
    except FileNotFoundError:
        print("Error: File not found!")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        
    # Handle other exceptions generally
    except Exception as e:
        print(f"Caught a general error: {e}")

print("--- Handling Multiple Exceptions ---")
handle_errors("file")
handle_errors("math")
handle_errors("type")
