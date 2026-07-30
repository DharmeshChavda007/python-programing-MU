'''Write a program to create and manipulate lists
using indexing slicing and list comprehensions'''

numbers = [10, 20, 30, 40, 50, 60]
print("List:", numbers)

print("\nIndexing:")
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])

# Slicing

print("\nSlicing:")
print("Elements from index 1 to 3:", numbers[1:4])
print("First three elements:", numbers[:3])
print("Elements from index 3 to end:", numbers[3:])
print("Complete list:", numbers[:])
print("Reverse list:", numbers[::-1])

# List Comprehensions

# Create a list of squares
squares = [x ** 2 for x in numbers]
print("\nSquares of all elements:", squares)

# Create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Create a list by adding 5 to each element
add_five = [x + 5 for x in numbers]
print("Each element +5:", add_five)

