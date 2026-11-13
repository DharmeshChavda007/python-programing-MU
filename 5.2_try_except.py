# 2. Write a program to handle exceptions using try except else and finally blocks.

a = 10
b = 2

try:
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

else:
    print("No exception occurred")

finally:
    print("This block is always executed")
