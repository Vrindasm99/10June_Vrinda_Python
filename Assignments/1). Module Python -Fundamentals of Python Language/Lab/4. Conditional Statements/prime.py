# ----------------------------------------
# Practical Example 6: Check if a Number is Prime Using if-else
# ----------------------------------------

# A prime number is a number greater than 1
# that has no positive divisors other than 1 and itself

# Ask the user to enter a number
number = int(input("\nEnter a number to check if it's prime: "))

# Check if the number is greater than 1
if number > 1:
    # Assume it is prime unless we find a divisor
    is_prime = True

    # Check for factors from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break  # No need to check further if one divisor is found

    # Display the result
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print(f"{number} is not a prime number (prime numbers are greater than 1).")
