


class Calculator:

    def __init__(self,num1,num2):

        self.num1=num1

        self.num2=num2

    def add(self):

        return self.num1+self.num2
    
    def sub(self):

        return self.num1-self.num2
    
    def mul(self):

        return self.num1* self.num2
    

calc_instance1=Calculator(100,80)

print(calc_instance1.add())
print(calc_instance1.sub())
print(calc_instance1.mul())
