

class Calculator:

    def __init__(self,*args):

        self.numbers=args

    def add(self):

        return sum(self.numbers)
    
    def sub(self):

        result=0

        for num in self.numbers:

            result=num-result

        return result
    
   

cal_instance1=Calculator(10,2,12,13,14)

print(cal_instance1.add())

print(cal_instance1.sub())

