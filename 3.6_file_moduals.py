#6. Write a program to perform file and directory operations using os and sys modules.
import os

path = "/home/user/documents/sample.txt"

print(os.path.isfile(path))   # True if path is a file
print(os.path.isdir(path))    # True if path is a directory
print(os.path.isabs(path))    # True if path is an absolute path
print(os.path.dirname(path))  # Returns the directory part
print(os.path.basename(path)) # Returns the file name
