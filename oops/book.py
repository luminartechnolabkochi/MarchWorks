

class Books:

    title:str

    author:str

    price:int

    genre:str

    pages:int

    def set_book(self,title,author,price,genre,pages):
        
        # initalizing instance  variable

        self.title=title

        self.author=author

        self.price=price

        self.genre=genre

        self.pages=pages

    def display_book(self):

        print(self.title,self.author,self.price,self.pages,self.genre)

# reference_name=className()
book_instance1=Books()

book_instance1.set_book("The Power of Your Subconscious Mind","joseph",350,500,"fiction")

book_instance1.display_book()

    

