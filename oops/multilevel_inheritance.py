


class A:

    def m1(self):

        print("m1 method inside class A")


class B:

    def m2(self):

        print("m2 method inside class B")



class C(B,A):

    def m3(self):

        print("m3 method inside class C")


c_instance=C()

c_instance.m3()

c_instance.m2()

c_instance.m1()



