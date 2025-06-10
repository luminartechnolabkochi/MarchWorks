


# display wlecome_python_n_times()

# for i in range(1,6):

#     print("Welcome python")


def welcome_python_n_times(count):

    if count==1:

        return
    
    print("welcome python")

    welcome_python_n_times(count-1)

welcome_python_n_times(950)