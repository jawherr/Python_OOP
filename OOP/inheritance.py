class Person:
    def personName(self):
        print("this is person name")
    def personEyeColor(self):
        print("Eye color is blue")
    def personAge(self):
        print("age is 33")
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

muh = muhammed()
muh.personName()
muh.personAge()
muh.personEyeColor()
muh.personHeight()