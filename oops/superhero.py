


class SuperHero:

    def __init__(self,name):

        self.name=name

    def super_powers(self):

        print("super power")



class Spiderman(SuperHero):

    def __init__(self, name):
        super().__init__(name)

    def super_powers(self):
        
        print(self.name,"web","jump")

    
class MinnalMurali(SuperHero):

    def __init__(self,name):
        super().__init__(name)

    def super_powers(self):
        print(self.name,"")


    

spiderman_instance1=Spiderman("spiderman")

spiderman_instance1.super_powers()


minnal_murali_instance=MinnalMurali("minnal murali")

minnal_murali_instance.super_powers()




    