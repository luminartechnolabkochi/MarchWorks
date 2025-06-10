

word="madam" #13
#     01234

length=len(word)-1

result=""

for i in range(length,-1,-1):

    result=result+word[i]

print(result)