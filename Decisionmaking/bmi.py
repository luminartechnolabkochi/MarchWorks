

# BMI=weight/height_in_meter **2

height=int(input("enter height in cm"))

weight=int(input("enter weight in kg"))

height_in_meter=height/100

bmi=round(weight/height_in_meter**2)

print(bmi) #24

if bmi<20:

    print("underweight")

elif bmi<25:
    print("normal weight")

elif bmi<30:

    print("overweight")
else:

    print("obese")

