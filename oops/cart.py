
class Cart:

    #name,price,quantity

    def __init__(self,user):

        self.user=user

        self.basket=[] #list

    def add_basket_item(self,**kwargs):

        self.basket.append(kwargs)

        print("item has been added to cart")

    def remove_basket_item(self,id):

        for bi in self.basket:
            if bi.get("id")==id:
                self.basket.remove(bi)

    def cart_summary(self):

        print("cart summary")

        for bi in self.basket:


            print(f"id={bi.get('id')} Title={bi.get('title')} Qty={bi.get('qty')} Price={bi.get('price')} Total={bi.get('price')*bi.get('qty')}")
        
        basket_total=sum([bi.get("qty") * bi.get("price")  for bi in self.basket])

        print("BASKET TOTAL",basket_total)
      

                
cart_instance1=Cart("vijil")

cart_instance1.add_basket_item(id=1,title="iphone16",qty=1,price=100000)

cart_instance1.add_basket_item(id=2,title="s24",qty=1,price=85000)

cart_instance1.add_basket_item(id=3,title="boatnirvana",qty=2,price=2500)

cart_instance1.cart_summary()


    


