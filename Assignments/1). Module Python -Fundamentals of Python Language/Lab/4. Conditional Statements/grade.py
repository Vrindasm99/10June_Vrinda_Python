# ----------------------------------------
# Practical Example 7: Calculate Grades Using if-else Ladder
# ----------------------------------------

# Ask the user to enter the percentage
percentage = float(input("\nEnter your percentage: "))

# Use if-else ladder to determine grade
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
elif percentage >= 35:
    grade = 'E'
else:
    grade = 'F'  # Fail

# Display the result
print(f"Your percentage: {percentage}%")
print(f"Your grade: {grade}")
