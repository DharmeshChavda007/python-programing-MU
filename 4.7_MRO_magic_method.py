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
glen.alexandria()   #it will start seraching for method in the main class from the object is created if it not found in that class then it will find in parent class

