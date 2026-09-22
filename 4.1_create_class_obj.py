#1. Write a program to create a class and object in Python.
class gretting():
    a = 10         #variable
    
    def lilpig_lilpig(self):    #method
        print('let me in !')
        
obj = gretting()        #object of greeting class
print(obj.a)            #access variable through object
obj.lilpig_lilpig()     #access method through object
