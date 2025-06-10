# GCD|HCF of two numbers
# write a program to find hcf|gcd of two numbers
# num1=12
# num2=24
# hcf(12,24) is =>12

num1=int(input("enter num1"))
num2=int(input("enter num2"))

smallest=0



smallest=num1 if num1<num2 else num2

hcf=1

for i in range(1,smallest+1):

    if num1%i==0 and num2%i==0:

        hcf=i

print(hcf)