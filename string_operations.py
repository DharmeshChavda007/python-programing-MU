#string operations

string1 = "Dharmesh"
string2 = "Chavda"
string3 = " marwadi university "

# Concatenation
print(string1+" "+string2)
# Repetition
print("Dharmesh" * 3)
# Indexing
print(string1[1])
# slicing
print(string1[0:4])
# Length
print(len(string1))
# Uppercase
print("uppercase :",string1.upper())
# Lowercase
print("lowercase :",string1.lower())

#Converts first letter of each word to uppercase
print(string3.title())

#Converts first letter to uppercase
print(string3.capitalize())

#Removes spaces from both ends
print(string3.strip())

#Replaces a substring
print(string1.replace("D","R"))

#Finds the position of a substring
print(string1.find('m'))

#Counts occurrences of a substring
print(string2.count('a'))

#Checks if the string starts with a substring

print(string3.startswith(' ma'))

#Checks if the string starts with a substring

print(string3.endswith('sity '))
