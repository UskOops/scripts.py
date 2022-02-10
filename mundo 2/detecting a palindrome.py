phrase = (input('Write a phrase: ')).strip().upper()
word = phrase.split()#split() divide a string em uma lista de strings
together = ''.join(word) # junta todas as palavras em uma só
inverse = '' # inverte a string
for letter in range (len(together) - 1, -1, -1): # para cada letra da string
        inverse += together[letter]
        print(together, inverse)
if together == inverse:
    print('The phrase is a palindrome')
else:
    print('The phrase is not a palindrome')
