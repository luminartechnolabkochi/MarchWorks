

arr=[2,3,4,5,6,7]
#    0 1 2 3 4 5
#     l        r

sum=int(input("enter sum>"))

left=0

right=len(arr)-1

while(left<right):

    cur_sum=arr[left]+arr[right]

    if cur_sum==sum:

        print(arr[left],arr[right])

        break
    elif cur_sum<sum:

        left=left+1

    elif cur_sum>sum:

        right=right-1


lst=[-3,-2,-4-1,1,2,4,40]

# closest number to zero
# -1,1 largest of this number => 1

# lst=[-4,-3,14,3,4,5]
#3

number=-1

# print(abs(number))
# abs()
# abs(numer)
# print()
# round()
# max(),min(),sum(),sorted(),len()

# tuple(),set()
# dictionary()