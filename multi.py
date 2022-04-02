class Multiplication:
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        self.total = self.firstNumber * self.secondNumber

    def multiTwoNumber(self):
        print(f"The multiplication of the two numbers {self.firstNumber} and {self.secondNumber} is {self.total}.")

liza = Multiplication(2,3)
liza.multiTwoNumber()