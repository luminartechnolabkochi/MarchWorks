
from builtins import open

contrib1_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\contribution1.txt"
contrib2_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\contribution2.txt"
contrib3_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\contribution3.txt"


summary={}
# name=ajay
# amount=80
print()

with open(contrib1_path,"r") as fr1:

    for line in fr1:

        name,amount=line.strip("\n").split(",")

        summary[name]=summary.get(name,0)+int(amount)

with open(contrib2_path,"r") as fr2:

    for line in fr2:

        name,amount=line.strip("\n").split(",")

        summary[name]=summary.get(name,0)+int(amount)


with open(contrib2_path,"r") as fr3:

    for line in fr3:

        name,amount=line.strip("\n").split(",")

        summary[name]=summary.get(name,0)+int(amount)



print(summary)

highest_paid_player=max(summary,key=summary.get)

print(highest_paid_player,summary.get(highest_paid_player))






