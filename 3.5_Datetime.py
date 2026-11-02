'''
5. Write a program to display current date and
time using date time module.
'''
import datetime

# Get current date and time
x = datetime.datetime.now()

print("Current Date and Time:", x)
print("Current Year:", x.year)
print("Current Month:", x.month)
print("Current Day:", x.day)
print("Current Time:", x.strftime("%H:%M:%S"))
print("Day Name:", x.strftime("%A"))
