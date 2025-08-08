a = []

n = int(input("How many elements do you want to insert into the list? "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("Updated list:", a)
