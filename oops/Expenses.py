

# 


class Expense:

    def __init__(self,user):

        self.user=user

        self.transactions=[]

    
    def add_expense(self,**kwargs):

        self.transactions.append(kwargs)

        print("transaction has been added")

    def delete_expense(self,id):

        for t in self.transactions:

            if t.get("id")==id:

                self.transactions.remove(t)

                print("transaction has been removed!!!!!")

    def update_transactions(self,id,**kwargs):

        for t in self.transactions:

            if t.get("id")==id:

                t.update(kwargs)

                print("transaction hasbeen updated")

    def summary(self):

        self.total_expense=sum([t.get("amount") for t in self.transactions])

        print(self.total_expense)

        self.category_summary={}#foos:120

        for t in self.transactions:

            if t.get("category") in self.category_summary:
                self.category_summary[t.get("category")]+=t.get("amount")

            else:
                self.category_summary[t.get("category")]=t.get("amount")

        print(self.category_summary)

        print(max(self.category_summary,key=self.category_summary.get))



expense_instance=Expense("divya")

expense_instance.add_expense(id=1,title="breakfast",amount=120,category="food",date="2025-05-17")
expense_instance.add_expense(id=2,title="bus ticket",amount=100,category="transportation",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="bills",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="bills",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="transportation",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="food",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="food",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="bills",date="2025-05-17")
expense_instance.add_expense(id=3,title="phone recharge",amount=147,category="transportation",date="2025-05-17")
print(expense_instance.transactions)

expense_instance.update_transactions(id=3,amount=157)
expense_instance.update_transactions(id=2,amount=150,date="2025-05-12")

print(expense_instance.transactions)

expense_instance.summary()



# polymorphism
    #method overloading
    #method overriding
    #abstraction
        #