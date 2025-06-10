


arr=[10,11,12,13,45,46,47,78,79,90,91]

# create a two list 1)even_list 2)odd_list from arr
even_list=[]

odd_list=[]

for num in arr:

    if num%2==0:

        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list)

print(odd_list)