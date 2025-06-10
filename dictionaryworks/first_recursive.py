

text="ABCAC"

wc={}

for ch in text:

    if ch not in wc:

        wc[ch]=1
    else:
        print(ch,"is the recursive character")
        
        break


