name = "Muhammed"
num1 = 1
num2 = 3

def myName():
    print("Muhammed Essa")


class Person:
    def __init__(self,name="Hassan",lname="Omer",age=0,salary=0):
        self.name = name
        self.lname = lname
        self.age = age
        self.salary = salary

    def personfullInfo(self):
        print("Person full information is : {} {} {} {}"
              .format(self.name, self.lname,self.age,self.salary))

    def personfullName(self):
        print("Person full name is : {} {}"
              .format(self.name,self.lname))

    def firstName(self):
        print("Person first name is : {}".format(self.name))

    def personlName(self):
        print("Person last name is : {}".format(self.lname))


