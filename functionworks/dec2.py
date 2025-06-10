
def add_good_decorator(fn):

    def wrapper():

        result=fn()

        return "Good"+result
    
    return wrapper

@add_good_decorator
def say_morning():

    return "Morning"

@add_good_decorator
def say_evening():

    return "Evening"


@add_good_decorator
def say_night():

    return "Night"

print(say_morning())

from datetime import datetime

def add_pm_am_dec(fn):

    def wrapper(user):

        result=fn(user)

        time=datetime.now().strftime("%p")

        if time=="AM":

            return result+" Good morning"
        else:
            return result +"Good evening"
        
    return wrapper


@add_pm_am_dec
def send_greetings_to_user(user):

    return f"hello {user}"

print(send_greetings_to_user("ram"))

