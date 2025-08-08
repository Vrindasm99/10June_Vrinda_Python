

sample = "   welcome To PYTHON world!   "

print("\nOriginal string with spaces:", repr(sample))

# Remove leading and trailing whitespace
print("strip()         :", sample.strip())

# Convert to lowercase
print("lower()         :", sample.lower())

# Convert to uppercase
print("upper()         :", sample.upper())

# Replace a word
print("replace()       :", sample.replace("PYTHON", "Java"))

# Count how many times a character appears
print("count('o')      :", sample.count('o'))

# Check if the string starts with 'welcome'
print("startswith('welcome'):", sample.strip().startswith('welcome'))

# Split the string into words
print("split()         :", sample.strip().split())

# Capitalize the first letter
print("capitalize()    :", sample.strip().capitalize())

# Title case (capitalize first letter of each word)
print("title()         :", sample.strip().title())
