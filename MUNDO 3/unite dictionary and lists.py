people = {} # dicionario vazio
guys = [] # lista vazia
sum = average = 0 # soma e media
while True:
    people.clear() # limpa o dicionario
    people['name'] = input('What is your name? ')
    print('-=' * 20)
    while True: 
        people['sex'] = input('SEX: [M/F] ').upper()[0]
        print('-=' * 20)
        if people ['sex'] in 'MF': 
            break
        print('ERROR! Please, type you correct sex (M or F): ')
    people ['age'] = int(input('AGE: '))
    guys.append(people.copy()) 
    print('-=' * 20)
    while True:
        answer = input('Do you want continue? [Y/N] ').upper()[0]
        if answer in 'YN':
            break
        print('ERROR! Answer only Y or N: ')
    if answer == 'N':
        break
print('-=' * 20)
print(f'(A)Total of people: {len(guys)}')
for guy in guys:
    sum += guy['age'] # soma das idades
    average = sum / len(guys) # media das idades
print(f'(B)The average of age is {average:.2f}') # media arredondada usando 2 casas decimais
print(f'(C)The registered women are, ', end='')
for guy in guys: 
    if guy['sex'] == 'F':
        print(f'{guy["name"]} ', end='') 
print(f'(D) List of people with age above average: ', end='')
for guy in guys:
    if guy ['age'] >= average:
        


