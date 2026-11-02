#1. Write a program to create and import a userdefined module. 
import calculator as c
print(c.add(5,5))
print(c.sub(10,5))
print(c.mul(20,10))
print(c.div(20,2))


# User-defined Calculator Module

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
