#2. Write a program to demonstrate constructor and destructor usage.

class demo():
    def __init__(self,name):     #this is the constructor
        self.name = name
        print("constructor calld !")


    def __del__(self):          #distructor
        print("distructor is calld !",self.name)

obj1=demo('Dhamreh')        #when the object is crated then the constructor is called implicitly

del obj1   


    
