# Practical Example 24: Write a Python program to match a word in a string using re.match().
import re

text = "Python is fun to learn."
pattern_match = r"Python"     # This is at the start
pattern_no_match = r"is"      # This is NOT at the start

print("--- re.match() Demonstration ---")

# 1. Match at the start (Success)
result_1 = re.match(pattern_match, text)
if result_1:
    print(f"Match successful for '{pattern_match}' at the beginning.")
else:
    print(f"Match failed for '{pattern_match}'.")

# 2. Match not at the start (Failure)
result_2 = re.match(pattern_no_match, text)
if result_2:
    print(f"Match successful for '{pattern_no_match}'. (Shouldn't happen)")
else:
    # re.match() only looks at index 0.
    print(f"Match failed for '{pattern_no_match}', because it is not at the beginning.")
