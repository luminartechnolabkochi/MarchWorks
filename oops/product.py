

# Product 
# code,title,price,category

class Product:

    def __init__(self,code,title,price,category):

        self.code=code

        self.title=title

        self.price=price

        self.category=category

    def display_product(self):

        print(self.title,self.code,self.price,self.category)

    def __str__(self):

        return self.title

product_instance1=Product("pc123","stripedshirt",1300,"shirt")
product_instance2=Product("pc231","tshirt",1000,"shirt")

print(product_instance1)

# __str__ is a special method in python used to define string representation of an object

#it is called automatically when you use print(object)




