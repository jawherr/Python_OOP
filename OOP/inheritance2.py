class Person:
    def personName(self):
        print("this is person name")
    def personEyeColor(self):
        pass
    def personAge(self):
        pass
    def personHeight(self):
        print("person height 180 cm")

class muhammed(Person):

    def personName(self):
        print("this is Muhammed Essa")
    def personEyeColor(self):
        print("Eye color is Black")
    def personAge(self):
        print("age is 33")
    def personHeight(self):
        print("person height 178 cm")

class Usama(Person):
    def name(self):
        super().personName()
        print("this is Usama name")


class Ahmed(Person):
    pass


ah = Ahmed()
ah.personName()
ah.personHeight()
print("------")
usam = Usama()
usam.name()

muh = muhammed()
muh.personName()
muh.personAge()
muh.personEyeColor()
muh.personHeight()