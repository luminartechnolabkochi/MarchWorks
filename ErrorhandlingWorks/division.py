

num1=int(input("enter number1 >"))#12


num2=int(input("enter number2> "))#0

try:
    division_result=num1/num2# 12/0=2 error
    print(f"division result={division_result}")
except Exception as e:
    print(e)


print("line 12")

print("line 14")