#1. Write a program to demonstrate different types of errors and exceptions in Python.

# 1. ZeroDivisionError
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# 2. ValueError
try:
    num = int("hello")
except ValueError:
    print("Error: Invalid value")

# 3. TypeError
try:
    result = 10 + "Python"
except TypeError:
    print("Error: Invalid data types")

# 4. IndexError
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Error: List index out of range")

# 5. KeyError
try:
    student = {"name": "Rahul", "age": 21}
    print(student["course"])
except KeyError:
    print("Error: Key not found")

# 6. ImportError
try:
    from math import abc
except ImportError:
    print("Error: Unable to import module")

print("Program completed")
