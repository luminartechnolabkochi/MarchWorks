
# find missing least + ve integer
arr=[1,2,3,4,5,6,7]
#    0 1 2 3 4 5
#              l r

limit=len(arr)-1


for left in range(0,limit):

    right=left+1

    difference=arr[right] - arr[left]

    if difference !=1:

        print(arr[left]+1,"is imissing")

        break

else:

    print(arr[right]+1,"is missing")





# if()...else

# for...else















