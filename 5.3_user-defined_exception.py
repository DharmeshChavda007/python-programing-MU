# Program to define and raise a user-defined exception

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("You are eligible to vote")

except AgeError as e:
    print("User-defined Exception:", e)

except ValueError:
    print("Please enter a valid number")
