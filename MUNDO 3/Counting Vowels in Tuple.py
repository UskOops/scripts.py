words = ('learning','python','study','tuple','work','life')
for w in words:
    print(f' \nIn word {w.upper()} there are',end= ' ')
    for word in w:
        if word.lower() in 'aeiou':
            print(word,end=' ')