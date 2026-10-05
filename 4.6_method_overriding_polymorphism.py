#6. Write a program to demonstrate method overriding and polymorphism.

#method overriding

class textbooks:
    def content(self):
        print("this is the textbook class")

class subject(textbooks):
    def content(self):
        super().content()
        print("this is the subject class")
        
class maths(subject):
    def content(self,a,b):
        super().content()
        print("content of maths class",a+b)

obj1=maths()
obj1.content(10,20)



#-----------------------------------------------

#polymorphism

