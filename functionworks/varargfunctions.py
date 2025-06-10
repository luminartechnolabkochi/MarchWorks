

# * => arguments


def add_mnumbers(*nums):

    return sum(nums)


# filter_positive_numbers(10,-1,-2,12,13)
# filter_positive_numbers(10,-1,-2,12,13,-2,-7)
# (10,12,13)

def filter_positive_numbers(*nums):#nums=(10,-2,-3,-4,12,13)

    return [n for n in nums if n>0]

print(filter_positive_numbers(10,-2,-3,-4,12,13))




def filter_negative_numbers(*nums):

    return [num for num in nums if num<0] 


print(filter_negative_numbers(-10,12,-13))


# concat_strings("hello","hai") hellohai
# concat_strings("good","morning","all") goodmorningall

def concat_strings(*args):

    result=""

    for w in args:

        result=result+w

    return result

print(concat_strings("hello","hai"))
print(concat_strings("good","morning","all"))