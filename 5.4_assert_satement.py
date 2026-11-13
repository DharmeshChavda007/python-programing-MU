# Write a program to demonstrate the use of assert statement.

try:
    age = int(input("Enter your age: "))

    assert age >= 18, "Age must be 18 or above"

    print("You are eligible to vote")

except AssertionError as e:
    print("Assertion Error:", e)

except ValueError:
    print("Please enter a valid number")
