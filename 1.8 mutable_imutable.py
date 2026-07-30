'''8. Write a program to explain mutable and
immutable objects in Python.'''

#mutable
#list

roll_no = [1,2,3]
print(roll_no)
# change the value
roll_no[2] = 4
print(roll_no)

#imuatble
#tuple

ages = (20,21,30,40)
print(ages)
ages[1] = 10 # throws error
print(ages)
