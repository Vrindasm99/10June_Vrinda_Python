# Practical Example 23: Write a Python program to search for a word in a string using re.search().
import re

text = "The cat sat on the mat."
pattern = r"sat" # We are searching for this word

# re.search() checks the ENTIRE string for the first match.
result = re.search(pattern, text)

print("--- re.search() Demonstration ---")

if result:
    print(f"Found the word '{result.group()}'!")
    print(f"It starts at position: {result.start()}")
else:
    print("Word not found in the string.")
