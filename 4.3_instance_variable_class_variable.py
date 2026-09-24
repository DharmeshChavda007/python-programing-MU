# 3. Write a program to illustrate instance variables and class variables.

#instance variable

class student:
    university_Name = "Marwadi University"          #class variable
    def info(self,name,age):    #instance method
        self.name = name    #instance variable
        self.age = age
        print("name is :",self.name,"age is :",self.age)


t1 = student()
t1.info("Dharmesh",18)
print(student.university_Name)      #class variable access through class name

