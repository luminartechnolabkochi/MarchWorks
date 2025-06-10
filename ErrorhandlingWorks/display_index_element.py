

lst=[1,10,12,2,3,4,5,7,8,8,8,9,9,9,9,8,8,7,5,5,4,3,3,3,2]


index=int(input("enter index position> ")) #1000
try:
    print(f" element at index {index} is {lst[index]}")
except Exception as e:
    
    index=int(input("enter index position > "))
    try:
        print(f" element at index {index} is {lst[index]}")
    except Exception as e:
        index=int(input("enter index position > "))
        print(f" element at index {index} is {lst[index]}")

finally:
    print("completed ......")