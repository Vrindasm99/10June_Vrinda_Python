a=open("Student_data.txt","a")

"""filename = "students.txt"
file = open(filename, 'a')"""

n=int(input("Enter the number of students :"))

for i in range(n):
    print(f"Enter details for {i + 1} : ")
    sid=input("Enter the id: ")
    name=input("Enter the name: ")
    city=input("Enter the city: ")
    a.write(F"\niD: {sid}" )
    a.write(F"\nNAME: {name}" )
    a.write(F"\nCITY: {city}" )

    

#print("\n\n\n--------------------------------")

for i in a:
    print(i)
    


print("\n\n YOUR DATA HAS BEEN SAVED...")


