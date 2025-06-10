text="hello world python"

# display all characters in
#  the world till ecounter second vowel

VOWELS="aeiou"

v_count=0

for ch in text:    

    if ch in VOWELS:

        v_count+=1

    if v_count==2:
        break
    
    print(ch)
# for
# in for if 
# 2=>24 (2+22)
# 3=> 369  (3+33+333)
# 4 =>     (4+44+444+4444)
