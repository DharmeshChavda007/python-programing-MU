'''Write a program to generate a multiplication
table using a for loop. '''

n = int(input('Enter value for n :'))

i = 1
for i in range(1,11):
    print(n,'*',i,'=',n*i)
    i += 1
