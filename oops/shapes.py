

class Shape:

    def __init__(self,name,color):

        self.name=name

        self.color=color

class Circle(Shape):

    def __init__(self, name, color,radius):

        super().__init__(name,color)

        self.radius=radius

    def area(self):

        print(f"area of a {self.name} with color {self.color} = {3.14*self.radius**2}")

circle_instance1=Circle("circle","red",6)

circle_instance1.area()