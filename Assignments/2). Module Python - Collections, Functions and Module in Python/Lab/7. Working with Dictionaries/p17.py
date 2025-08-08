a = ["a", "b", "c"]
b = [1, 2, 3]

combined_dict = {}
for i in range(len(a)):
    combined_dict[a[i]] = b[i]

print("Combined dictionary:", combined_dict)
