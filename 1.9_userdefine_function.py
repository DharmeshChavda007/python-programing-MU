'''
9. Write a program to define and use user-defined
functions with different types of arguments. 
'''
def welcome():
    print("Welcome to Python")

def add(a, b):
    print("Addition =", a + b)

def student(name, age):
    print("Name =", name)
    print("Age =", age)

def greet(name="Harsh"):
    print("Hello", name)

def total(*numbers):
    print("Total =", sum(numbers))

welcome()
add(10, 20)
student(age=21, name="Harsh")
greet()
greet("Rahul")
total(10, 20, 30, 40)
