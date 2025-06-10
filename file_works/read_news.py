

file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\news.txt"

f=open(file_path,"r")

all_word_list=[]

for line in f:
    # line=Pakistan once again violated the\n

    words=line.rstrip("\n").split(" ")

    for w in words:
        all_word_list.append(w)

print(all_word_list)












    