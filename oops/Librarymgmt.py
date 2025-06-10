
# constructor and special methods
class Library:

    def add_book(self,title,author):

        self.title=title

        self.author=author

        self.is_available=True

    def issue(self):

        if self.is_available==False:

            raise Exception("not available")
        
        else:

            print("book issued")

            self.is_available=False

    def return_book(self):

        self.is_available=True

        print(f"{self.title} is now available")

    def status(self):

        print(f"{self.title} status is  {self.is_available}")

lib_instance1=Library()

lib_instance1.add_book("rich dad","author")

lib_instance1.issue()

lib_instance1.return_book()

lib_instance1.status()
    



