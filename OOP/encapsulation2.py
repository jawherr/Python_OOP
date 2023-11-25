class Person:
    def __init__(self,**kwargs):
        self.infos = kwargs


    def  setName(self, lname):
        self.infos['lname'] = lname
    def getName(self ):
        return  self.infos.get('lname',"no name")

    def  setsalary(self, salary):
        self.infos['salary'] = salary
    def getsalary(self ):
        return  self.infos.get('salary',"no salary")

    def  setdept(self, dept):
        self.infos['dept'] = dept
    def getdept(self ):
        return  self.infos.get('dept',"no dept")

usama = Person(lname="Ahmed",salary=3000,dept="IT")
#usama = Person(lnames="Ahmed" )
print(usama.getName())

usama.setName('Wisam')

print(usama.getName())

print(usama.getsalary())
print(usama.getdept())

usama.setdept("Programming Python")

print(usama.getdept())