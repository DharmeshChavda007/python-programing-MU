'''
2. Write a program to demonstrate different
import mechanisms in Python.
'''

from calculator import add #this will only import the add funcaiton the rest of the functions are not accessible

print(add(80,90))

import calculator  # this will import the whole modual and every functions

print(calculator.sub(60,50))

import calculator as c # we can access the every funcaitons using the modulas alies name c.

print(c.mul(50,30))
