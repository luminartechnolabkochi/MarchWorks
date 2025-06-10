
# assert key word that test if condtion is true else raise 
# an assertion error 

# debugg

# create a function add_numbers that accept any numbers of
# params function should return sum of all +ve numbers only


def add_numbers(*args):

    return sum(args)



# assert add_numbers(100,200)==300,"invalid output"

# assert add_numbers(100,200,300)==600 ,"not working with different number of prameters"

# assert add_numbers(-100,100,-200,200)==300,"inavlid with - arguments"


# create a function smart_sub with two params num1,num2
# function should return +ve number after subtraction

def smart_sub(num1,num2):

    return abs(num1-num2)

assert smart_sub(100,80)==20,"inavlid out put"

assert smart_sub(80,100)==20,"invalid with parameter order"

assert smart_sub(100,50)==50,"invalid out put"

# fundamentals
# data types
# operators
# flowcontrol
    #decision making
    #looping
#functions
    #builtin functions(min,max,sum,input,print,round,abs,enumerate)
    #function define ,call
    #lambda fumctions
    #recursion

#string
    #string and string methods
    #string slicing

#collections
    #properties
    #list and list methods
    #set and set methods
    #tuple and tuple methods
    #dictionary and dictionary methods
    #nested collection
    #list comprehension

#File I/O
    #file operations [read,write,append]
    #processing json file

#python package and module
    #import
    #datetime

#Error handling
    #try,except,finally
    #raise,assert

# OOPS(object oriented programming)
    

