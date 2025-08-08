a=open("loop1_to_100","w")

for i in range(1,101):
    print(str(i))

    a.write(f"{str(i)} \n")
