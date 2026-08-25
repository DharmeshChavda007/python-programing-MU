#8. Write a program to demonstrate basic regular expression pattern matching.
import re

text = "My phone number is 8200842477"

pattern = r"\d{10}"

result = re.search(pattern, text)

if result:
    print("Pattern matched!")
    print("Found:", result.group())
else:
    print("Pattern not matched.")
