'''Write a program to check whether a number is
positive negative or zero using nested
conditions.'''

n = int(input('Enter the value for n :'))

if (n >= 0):
    if (n == 0):
        print('number is zero')
    else:
        print('number is positive')
else:
    print('number is negative')
