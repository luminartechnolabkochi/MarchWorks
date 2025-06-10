

class Vehicle:

    def __init__(self,name):

        self.name=name


class Car(Vehicle):#car is a Vehicle

    def __init__(self, name,seating_capacity,tyres,fuel_type):

        super().__init__(name)

        self.seating_capacity=seating_capacity

        self.tyres=tyres

        self.fuel_type=fuel_type

    def display_car(self):

        print(self.name,self.seating_capacity,self.tyres,self.fuel_type)

car_instance1=Car("baleno","5","5","petrol")

car_instance1.display_car()



# super() => is a function in python
# #  used to give access to method and properties of a parent class from child class

