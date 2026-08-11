'''
8. Write a program to illustrate variable scope
using local global and nonlocal variables.
'''
x = 10

def fun1():
     y = 20

     def fun2():
         z = 30
         print('globle variable x :',x)
         print('localvariable z :',z)
         nonlocal y
         print('nonlocal variable y :',y)
         y = 40
         print('updated nonlocal variable y :',y)
     fun2()

fun1()
