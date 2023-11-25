class animal:
    def __init__(self,nameValue):
        self.nameValue = nameValue


    def sound(self):
        print("this is {} sound".format(self.nameValue))

    def runAnimmal(self):
        print(" {} is running".format(self.nameValue))

    def sum(self):
        print(self.nameValue+4)


dog = animal("Dog")
cat = animal("cat")
myNum = animal(2)

myNum.sum()
dog.sound()
cat.sound()
dog.runAnimmal()
cat.runAnimmal()