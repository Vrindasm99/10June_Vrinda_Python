input_str = "hello world"
char_count = {}

for char in input_str:
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1

print("Character frequency:", char_count)
