phrase = input("Enter with a phrase: ").upper().strip() # strip() removes all whitespaces
print (f'the letter "a" first appears in the phrase: ', phrase.count('A')) # count() counts the number of times a string appears in a string
print (f'the letter "a" first appears in the phrase: ', phrase.find('A')+1) # find() returns the index of the first occurrence of a string
print (f'the letter "a" last appears in the phrase: ', phrase.rfind('A')+1)# rfind() returns the index of the last occurrence of a string
