''' Write a program to create a dictionary and
demonstrate dictionary methods and iteration. '''

student = {
    "Name": "Dharmesh",
    "Age": 22,
    "Course": "MCA",
    "City": "Rajkot"
}

# Display dictionary
print("Original Dictionary:", student)

# Accessing values
print("Name:", student["Name"])

# Dictionary methods
print("\nDictionary Methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Adding a new item
student["College"] = "Saurashtra University"
print("After Adding College:", student)

# Updating a value
student["Age"] = 23
print("After Updating Age:", student)

# Removing an item
student.pop("City")
print("After Removing City:", student)

# Iteration through dictionary
print("\nDictionary Iteration:")
for key, value in student.items():
    print(key, ":", value)

