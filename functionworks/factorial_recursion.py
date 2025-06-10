

# 3
# 3*2*1


def factorial(num):

    if num==0:
        return 1
    
    return num*factorial(num-1)

print(factorial(4))

# 1*factorial(1-1) 1*factorial(0)=1
# 2*factorial(2-1)#2*factorial(1)=2*1=2
#3*factorial(3-1)#3*factorial(2)=3*2=6
# 4*fact(4-1)#4*factorial(3)=4*6=24
