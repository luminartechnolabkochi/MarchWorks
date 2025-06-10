
# same method name different number of parameters

class Calculator:

    def add(self,num1,num2):

        return num1+num2
    
    def add(self,num1,num2,num3):

        return num1+num2+num3

    def add(self,num1,num2,num3,num4):

        return num1+num2+num3+num4
    

calculator_instance1=Calculator()

print(calculator_instance1.add(10,20,30,40))
    
