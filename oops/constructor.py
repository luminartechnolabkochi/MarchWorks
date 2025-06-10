

# a constructor is a special method that is used for initializing instance variables

# constructor name is always __init__()

# constructor automatically invoked during object creation


class Student:

    def __init__(self,name,rol,course):

        self.name=name

        self.roll_number=rol

        self.course=course

    def display_student(self):

        print(self.name,self.roll_number,self.course)

    def __str__(self):

        return self.name


student_instance1=Student("jibin","1234","mca")

student_instance1.display_student()

student_instance2=Student("vipin","4567","bca")

student_instance2.display_student()

print(student_instance1)


    