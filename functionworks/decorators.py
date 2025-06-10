

def swap_decorator(fn):#fn=sub

    def wrapper(n1,n2):#50,500

        if n1<n2:#50<500

            (n1,n2)=(n2,n1)#500,50

        return fn(n1,n2)#sub(500,50)
    
    return wrapper


@swap_decorator
def sub(n1,n2):#500,50


    return n1-n2#500-50=450

@swap_decorator
def division(n1,n2):

    return n1/n2


print(sub(50,500))








