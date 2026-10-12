#10.Write a program to perform file pointer operations using seek and tell methods.
# Writing data into a file
f = open("demo.txt", "w")
f.write("we can all live together")
f.close()

# Performing file pointer operations
f = open("demo.txt", "r")

print("Current position:", f.tell())

f.seek(6)
print("Position after seek:", f.tell())

print("Data from current position:", f.read())

f.close()
