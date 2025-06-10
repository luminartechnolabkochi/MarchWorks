

# read a number 
# display all divisors of number

# sample input1:4
# output:1,2,4

# sample input1:16
# output:1,2,4,8,16


number=int(input("enter number"))

for i in range(1,number+1):

    if number%i==0:

        print(i)