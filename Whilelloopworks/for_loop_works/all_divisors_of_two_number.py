

# read num1=12
# read num2=24

# display common divisors of num1 and num2

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
# i                        e
# 

num1=int(input("enter num1"))#12

num2=int(input("enter number2"))#24

for i in range(1,num1+1):

    if num1%i==0 and num2%i==0:

        print(i)






