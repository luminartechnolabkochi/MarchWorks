

# word_count

# I,V,X,L,C,D,M
character_list=["A","I","V","I","L","C","D","D","F","X","B","V"]

romans=("I","V","X","L","C","D","M")

rc={}

for ch in character_list:

    if ch in romans:

        if ch in rc:

            rc[ch]+=1
        else:
            rc[ch]=1
print(rc)