#7. Write a program to illustrate method resolution order and magic methods.

# Demonstrating Method Resolution Order (MRO)

class A:
    def show(self):
        print("Class A method")

class B(A):
    def show(self):
        print("Class B method")

class C(A):
    def show(self):
        print("Class C method")

class D(B, C):
    pass


print("Method Resolution Order:")
obj = D()
obj.show()

print(D.mro())


# Demonstrating Magic Methods

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print("Student object destroyed")


print("\nMagic Methods:")
s1 = Student("Rahul", 21)

print("Student Details:", s1)
print("Length of Name:", len(s1))

del s1
