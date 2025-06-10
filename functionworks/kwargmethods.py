


def calculator(*args):

    print(args)




calculator(10,20,30,"+")
calculator(10,20,40,"-")
calculator(10,20,40,"*")
calculator(10,20,"*")


def display_employee(*args):#args=("hari","hr",12000,"kakkanad","tvm")

    print(args[2])

display_employee("hari","hr",12000,"kakkanad","tvm")
display_employee("aswin",13000,"qa","kakkanad","tvm")



def display_student(**kwargs):#kwargs={"name":"vipin","rol":"123","course":"mca"}

    print(kwargs.get("name"))


display_student(name="vipin",rol=123,course="mca")



def display_mobile(**kwrags):

    print(kwrags)

    print(kwrags.get("price"))

get_mobprice= lambda **kwargs:kwargs.get("price")


display_mobile(title="edge60",display="amoled",processor="mediatek",price=3400)

print(get_mobprice(title="xiomi15",display="amoled",processor="mediatek",price=63000))







# display_key_and_values  

def display_key_and_values(**kwargs):#kwargs={"name":"bob","gender":"male","age":32}

    for k,v in kwargs.items():

        print(k,v)    


display_key_and_values(name="bob",gender="male",age=32)


# *args
# **kwrags

# calculator(10,20,30,40,50,operand="+")
# calculator(10,20,30,40,operand="*")
# calculator(10,20,operand="*")

def calculator(*args,**kwargs):
    result=1
    
    if kwargs.get("operand")=="+":

        return sum(args)
    
    elif kwargs.get("operand") == "*":

        for num in args:

            result=result*num
        return result

print(calculator(10,20,30,40,operand="+"))
print(calculator(10,20,30,operand="*"))



