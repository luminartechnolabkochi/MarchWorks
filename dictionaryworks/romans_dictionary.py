
# I,V,X, L,C,  D,  M
# 1,5,10,50,100,500,1000 

romans={
    "I":1,
    "V":5,
    "X":10
}

# roman V 

print(romans["V"])

# add roamn L with value 50

romans["L"]=50


# add roamn C with value 100

romans["C"]=100

print(romans)
# chk key D exist if d not exist add D with value 500


if "D" not in romans:

    romans["D"]=500

print(romans)


# chk M is  exist if not add key M with value 1000

if "M" not in romans:

    romans["M"]=1000

print(romans)