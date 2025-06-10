

# create a function is_leap_year with one parameter year
# return true if year is leap year else return false



def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    else:

        return False
    
res=is_leap_year(2025)

print(res)

# create a function factorial with one parameter  num
# return factorial of number

def factorial(num):

    result=1

    for i in range(1,num+1):

        result=result*i

    return result

res=factorial(3)

print(res)

# 0,1,1,2

#      p c n 

# create a function smart_sub with two parameter num1,num2 
# return num1-num2 if num1>num2
# return num2-num1 if num2>num1


# smart_sub(10,5) #5
# smart_sub(5,10) #5

def smart_sub(num1,num2):

    return num1-num2 if num1>num2 else num2-num1
    
result=smart_sub(10,5)

print(result)#5

result=smart_sub(5,10)

print(result)

# create a function last_digit_max with two param num1,num2
# return num1 if last_digit_of num1 > last_digit_of_num2 
# else return num2

# sample input last_digit_max(187,878) 
# o/p=>187


def last_digit_max(num1,num2):

    if num1%10>num2%10:

        return num1
    else:

        return num2
    
result=last_digit_max(187,872)

print(result)


# 