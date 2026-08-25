#7. Write a program to copy move and delete files using shut il module.
import shutil
import os

# Copy a file
source = "sample.txt"
copy_file = "copy_sample.txt"

shutil.copy(source, copy_file)
print("File copied successfully.")

# Move the copied file
move_file = "moved_sample.txt"

shutil.move(copy_file, move_file)
print("File moved successfully.")

# Delete the moved file
os.remove(move_file)
print("File deleted successfully.")
