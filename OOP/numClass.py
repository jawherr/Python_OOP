class mathOperator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def div(self):
        print(self.num1/self.num2)
    def multi(self):
        print(self.num1*self.num2)

mathO = mathOperator(4,2)
mathO1 = mathOperator(3,6)
mathO.sum()
mathO1.sum()
mathO.div()
mathO.sub()
mathO.multi()