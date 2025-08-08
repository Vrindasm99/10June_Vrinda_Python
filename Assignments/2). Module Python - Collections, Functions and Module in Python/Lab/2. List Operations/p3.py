
list = []
n = int(input("How many elements do you want to append? "))
for i in range(n):
    val = input(f"Enter element {i+1} to append: ")
    list.append(val)

# Take input to insert an element at a specific position
insert_val = input("Enter a value to insert: ")
insert_pos = int(input("Enter the index position to insert at: "))

# Insert the value
list.insert(insert_pos, insert_val)
print("UPDATED LIST:- :", list)
