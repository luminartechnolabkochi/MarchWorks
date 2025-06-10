
class Person:

    # name,age,gender

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display_person(self):

        print(self.name,self.age,self.gender)

    def __str__(self):

        return self.name
    
class Employee(Person):


    def __init__(self, name, age, gender,company,salary,department):
            # super()
            # self=> refer current class instance
            #super()=> refer parent

            super().__init__(name,age,gender)#calling parent class constructor

            self.company=company

            self.salary=salary

            self.department=department

    def display_employee(self):
         
         super().display_person()

         print(self.company,self.salary,self.department)

     
         



employee_instance=Employee("hari","34","male","lum",34000,"hr")

employee_instance.display_employee()




    



