#7. Write a program to illustrate method resolution order and magic methods.

#MRO-method resolution order
class TWD:
    def alexandria(self):
        print("Rick from alexandria ")

class kingdom(TWD):
    def alexandria(self):
        print("this is king ezikial from kingdom")

class hilltop(kingdom):
    def alexandria(self):
        print("This is maggie from hilltop")


glen = hilltop()
glen.alexandria()   #it will start seraching for method in the main class from the object is created if it not found in that class then it will find in parent clas

# magic fuctions
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
