
from datetime import datetime

class Bank:

    def create_account(self,acno,cutomer_name,balance,ac_type):

        self.acno=acno

        self.customer_name=cutomer_name

        self.balance=balance

        self.ac_type=ac_type

    def deposit(self,amount):

        self.balance+=amount

        print(f"your bank ac {self.acno} has been credited with amount{amount} on {datetime.now()} avl bal is {self.balance} ")

    
    def withdraw(self,amount):

        if amount> self.balance:

            raise Exception("insufficient balnce")
        
        else:

            self.balance-=amount

            print(f"your bank ac {self.acno} has been debited with amount{amount} on {datetime.now()} avl bal is {self.balance} ")


    def balance_enqiry(self):

        print(f"your bank ac {self.acno} cur bal {self.balance}")




bank_instance1=Bank()

bank_instance1.create_account("989345678","hari",3000,"savings")

bank_instance1.deposit(30000)


bank_instance1.withdraw(10000)

bank_instance1.balance_enqiry()