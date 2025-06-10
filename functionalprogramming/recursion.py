


# display hello world n times


for i in range(1,6):

    print("Hello world")



def show_hello_world(n):

    if n==1:
        return 
    
    print("rec helloworld")

    return show_hello_world(n-1)


show_hello_world(6)



n=5
# # 5*4*3*2*1
# fact=1

# for i in range(1,n+1):

#     fact=fact*i

# print(fact)

# 5*4!
# 4*3!
# 3*2!
# 2*1!

def factorial(n):

    if n==1 or n==0:

        return 1
    
    return n*factorial(n-1)


print(factorial(5))



def sum_of_n(number):

    if number==0:

        return 0
    
    return number+sum_of_n(number-1)

print(sum_of_n(10))

# 10 

# stack
# c   function call

# 5 1*factorial(1-1)
# 4 2*factorial(2-1)
# 3 3*factorial(3-1)
# 2 4*factorial(4-1)
# 1 5*factorial(5-1)
# 0 factorial(5)

# database
# 1)relational database (mysql,postgres)
# 2)non relational database(mongodb)