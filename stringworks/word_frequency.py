
text=str()

# "",'',"""",str()

search_word="cd"

srch_word_len=len(search_word)

text_len=len(text)

limit=text_len-srch_word_len


frequency=0

for i in range(0,limit+1):

    sliced_word=text[i:i+srch_word_len]

    print(i)

    if sliced_word==search_word:

        frequency+=1

print(frequency)


