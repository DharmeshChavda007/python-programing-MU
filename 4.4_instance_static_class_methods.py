#4. Write a program to demonstrate instance methods class methods and static methods.
class Student:
    college = "Marwadi University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class method
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    # Static method
    @staticmethod
    def is_pass(marks):
        return marks >= 40


# Creating an object
s1 = Student("Dharmesh", 75)

# Calling instance method
s1.display()

# Calling class method
Student.change_college("XYZ College")
print("College:", Student.college)

# Calling static method
print("Pass:", Student.is_pass(75))
