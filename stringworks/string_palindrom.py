
# read a word 
# chk given word is palindrome or not

word=input("enter word>") #RACECAR

reversed_word=word[::-1]

if word==reversed_word:

    print("palindrome")

else:

    print("not palindrome")


