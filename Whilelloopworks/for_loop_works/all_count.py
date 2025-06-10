

word="pneumonoultramicroscopicsilicovolcanoconiosis"

VOWELS="aeiou"

v_count=0

c_count=0

for ch in word:

    if ch in VOWELS:

        v_count+=1

    else:
        c_count+=1

print("vowel count",v_count)

print("consonant count",c_count)

# word="the quick brown fox jumps over the lazy dog"
