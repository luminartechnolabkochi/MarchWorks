#number=153
#3**3+ 5**3+ 1**3

# for loop

number=int(input("enter number"))

sum=0

while(number!=0):

    digit=number%10

    cube=digit**3

    sum+=cube

    number=number//10

print(sum)



