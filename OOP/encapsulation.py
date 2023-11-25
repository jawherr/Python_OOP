class Person:
    def __init__(self,name="Hassan",lname="Omer",age=0,salary=0):
        self.name = name
        self.lname = lname
        self.age = age
        self.salary = salary

    def  setName(self, name):
        self.name = name
    def getName(self ):
        return  self.name

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




# muhammed = Person("muhammed","Ghassan")
# muhammed.personfullName()
# muhammed.name = "Muhammed"
# muhammed.personfullName()Name()
# print(muhammed.name)

#usama = Person("Muhammed","Essa",22,1000)
# usama.firstName()
# usama.personlName()
# usama.personfullName()
usama = Person()
usama.personfullInfo()
#
# usama.salary=200
# usama.personfullInfo()

usama.setName('Wisam')

print(usama.getName())