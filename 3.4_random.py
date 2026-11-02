'''
4. Write a program to generate random numbers
using random module.
'''
import random

# Generate random integer between 20 and 100
print("Random Integer:", random.randint(20, 100))

# Generate random number between 0 and 1
print("Random Number:", random.random())

# Generate random number from a given range
print("Random Range:", random.randrange(1, 50))

# Select random element from a list
numbers = [10, 20, 30, 40, 50]
print("Random Choice:", random.choice(numbers))
