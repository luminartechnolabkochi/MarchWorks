

file_path="C:\\Users\\Luminar\\Desktop\\MarchPythonWorks\\file_works\\story.txt"

f=open(file_path,"r")

word_count={}

for line in f:

    words=line.split()

    for w in words:

        if w in word_count:

            word_count[w]+=1
        else:
            word_count[w]=1
            
print(word_count)





