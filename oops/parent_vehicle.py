

class Parent:

    def __init__(self):

        self.vehilces=["passion pro","swift","alto"]

    def get_vehicles(self):

        return self.vehilces


class Child(Parent):


    def __init__(self):
        super().__init__()

    def get_vehicles(self):
        
        self.vehicles=super().get_vehicles()

        self.vehicles.append("benz")

        self.vehicles.append("triumph")

        return self.vehicles  

   
child_instance=Child()

print(child_instance.get_vehicles())
    




    