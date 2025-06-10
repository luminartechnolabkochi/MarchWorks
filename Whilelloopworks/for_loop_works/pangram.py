word="the quick brown fox jumps over the lazy dog"

alphabets="abcdefghijklmnopqrstuvwxyz"

is_pangram=True

for ch in alphabets:#ch=a

    if ch not in word:

        is_pangram=False
        break
print(is_pangram)




