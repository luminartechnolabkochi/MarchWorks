
from functools import reduce

arr=[10,12,13,14,15]

total=reduce(lambda n1,n2:n1+n2,arr)
print(total)

product=reduce(lambda n1,n2:n1*n2,arr)
print(product)


# functools.py > reduce
# builtins.py =>map,filter,
# evens


# even_numbers=list(filter(lambda num:num%2==0,arr))

# print(even_numbers)

# e_numbers=[num for num in arr if num%2==0]
# print(e_numbers)



# cube_list=list(map(lambda num: num**3,arr))

# print(cube_list)


# add_five_list=list(map(lambda num:num+5,arr))

# print(add_five_list)


# 3 error
# 1.syntax error
# 2.logical error
#3.runtime error (error handling ) try except finally
                                    #raise,assert

# map()
# filter()
# reduce()



