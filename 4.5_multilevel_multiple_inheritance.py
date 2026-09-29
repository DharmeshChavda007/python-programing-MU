#5. Write a program to implement single multilevel and multiple inheritance.

#Multilevel inheritance
class TWD:
    def negan(self):
        print("lil pig ! lil pig ! let me in !")
class Governor(TWD):
    def Rick(self):
        print("we can all live togather !");
class Daryl(Governor):
    def morgan(self):
        print("i see red ! i see red !")

walker = Daryl()  #object of Daryl Class
walker.negan()
walker.Rick()
walker.morgan()

#Multiple inheritance

class calc1():
    def sum(self,a,b):
        return a + b
class calc2():
    def mul(self,a,b):
        return a * b
class calc3():
    def sub(self,a,b):
        return a - b
class calc4(calc1,calc2,calc3):
    def div(self,a,b):
        return a / b

obj = calc4()
print(obj.sum(5,5))
print(obj.mul(5,5))
print(obj.sub(5,5))
print(obj.div(5,5))

