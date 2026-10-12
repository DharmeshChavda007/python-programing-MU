#9. Write a program to read and write data into a file using different file modes.
# write mode
f = open("demo.txt", "w")
f.write("i am negan!\n")
f.write("lil pig lil pig ! let me in !")
f.close()

# read mode
f = open("demo.txt", "r")
print("File content:")
print(f.read())
f.close()

# append mode
f = open("demo.txt", "a")
f.write("\nezzy pezzy lemon sqezzy")
f.close()

# Reading the updated file
f = open("demo.txt", "r")
print("\nUpdated file content:")
print(f.read())
f.close()
