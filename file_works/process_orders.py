
swiggy_order_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\swiggy_orders.txt"

zomatto_order_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\zomatto_orders.txt"

walkin_order_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\walkin_orders.txt"


order_count={}#cb:1


with open(swiggy_order_path,"r") as fr1:

    for line in fr1:

        item=line.rstrip("\n")

        order_count[item]=order_count.get(item,0)+1

with open(zomatto_order_path,"r") as fr2:

    for line in fr2:

        item=line.rstrip("\n")

        order_count[item]=order_count.get(item,0)+1


with open(walkin_order_path,"r") as fr2:

    for line in fr2:

        item=line.rstrip("\n")

        order_count[item]=order_count.get(item,0)+1

print(order_count)



print(sorted(order_count,reverse=True,key=order_count.get))


# .json
# FILE

# oops