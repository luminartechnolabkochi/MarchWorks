


# 3 types of method
    # 1.instance method
    #2.class method
    #3.static method


# 2class method


class ClassMethodDemo:

    @classmethod
    def class_method(cls):

        print("insdide class method")


# ClassMethodDemo.class_method()



# class method example2

class Student:

    instituion_name="luminar"

    def __init__(self,name,rolnum):

        self.name=name

        self.rolnum=rolnum

    def display_student(self):

        print(self.name,self.rolnum)

    @classmethod
    def show_institution_name(cls):
        
        print(cls.instituion_name)
    
    @staticmethod
    def utility_method(a,b):

        print(a+b)

Student.show_institution_name()
Student.utility_method(100,200)

student_instance1=Student("ajay",123)

student_instance1.display_student()

