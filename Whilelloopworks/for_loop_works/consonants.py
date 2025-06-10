word="pythonissimple"
#count  consonants

VOWELS="aeiou"

c_count=0

for ch in word:
    
    if ch not in VOWELS:

        c_count+=1

print(c_count)

