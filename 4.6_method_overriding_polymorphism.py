#6. Write a program to demonstrate method overriding and polymorphism.
# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds")


# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
a1 = Dog()
a2 = Cat()

# Method Overriding
print("Method Overriding:")
a1.sound()
a2.sound()


# Polymorphism
print("\nPolymorphism:")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()






