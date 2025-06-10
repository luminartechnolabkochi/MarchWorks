

# create a funtion display_good_morning with no paramater 
# function should display good morning


def display_good_morning():

    print("Good Morning")


# function_call by using function name

display_good_morning()


# create a funtion display_good_evening with no paramater 
# function should display good evening


def display_good_evening():

    print("Good evening")


display_good_evening()


# function with parameter


def greetings(message):

    print(message)

greetings("good evening")

greetings("morning")


# create a function display_message with two parameter user,message
# function should display hello user message



def display_message(user,message):

    print(f"hello {user} {message}")

display_message("Arun","Good morning")


# create a function add_number with two params num1,num2
# display sum of num1,num2


def add_number(num1,num2):

    result=num1+num2

    print(result)


add_number(100,200)

add_number(500,700)

# create a function cube with one parameter num
# display cube of num



def cube(num):

    result=num**3

    print(result)

cube(7)

# function with parameter and a return value



# create a function min_two with two param n1,n2
# return smallest number

def min_two(n1,n2):

    if n1<n2:

        return n1
    
    else:
        return n2
    

res=min_two(10,7)
print(res)



# builtins.py