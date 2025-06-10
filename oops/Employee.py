

# Employee
#name,dep,salary

class Employee:

    def set_employee(self,name,dept,salary):

        self.name=name

        self.dept=dept

        self.salary=salary

    def get_name(self):

        print(self.name)

    def display_employee(self):

        print(self.name,self.dept,self.salary)

emp_instance1=Employee()

emp_instance2=Employee()

emp_instance1.set_employee("aldo","qa",35000)

emp_instance1.get_name()
emp_instance1.display_employee()
emp_instance2.set_employee("devanand","qa",35000)
emp_instance2.get_name()