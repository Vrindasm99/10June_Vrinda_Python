
filename = "students.txt"
file = open(filename, 'a')

# Ask the user how many students they want to enter
num_students = int(input("Enter the number of students: "))

# Loop to collect and save student data
for i in range(num_students):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    city = input("Enter city: ")
    
    # Print the details
    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"ID: {student_id}")
    print(f"City: {city}")
    
"""# Write the details to the file
    file.write(f"Name: {name}, ID: {student_id}, City: {city}\n")

# Close the file after writing all entries
file.close()

print(f"\nAll student details saved successfully to '{filename}'.")"""
