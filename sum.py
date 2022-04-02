class Sum:
    def __init__(self,a,b):
        self.firstNo = a
        self.secondNo = b

    def addTwoNo(self):
        print(f"Sum of the two numbers {self.firstNo} and {self.secondNo} is {self.firstNo + self.secondNo}.")

subash = Sum(10,20)
subash.addTwoNo()