# given two words word1 and word2 
# write a program to chk these are anagram or not

word1="silenT".lower()

word2="listen".lower()

srt_word1=sorted(word1)

srt_word2=sorted(word2)

if srt_word1==srt_word2:

    print("anagram")
else:
    print("not anagram")

