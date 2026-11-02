#6. Write a program to perform file and directory operations using os and sys modules.
import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
os.mkdir("MyFolder")
print("Directory Created Successfully")

# Create a file
file = open("MyFolder/demo.txt", "w")
file.write("Welcome to Python Programming")
file.close()
print("File Created Successfully")

# Display files and directories
print("Directory Contents:", os.listdir("MyFolder"))

# Rename the file
os.rename("MyFolder/demo.txt", "MyFolder/newdemo.txt")
print("File Renamed Successfully")

# Display Python version using sys module
print("Python Version:", sys.version)

# Display platform information
print("Operating System:", sys.platform)
