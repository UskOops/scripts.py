num = []
pairs = []
odds = []
while True:
    num.append(int(input('Type a number: ')))
    answer = (input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if answer in 'Nn':
        break
for i in num:
    if i % 2 == 0: # Se o resto da divisão por 2 for 0, então o número é par
        pairs.append(i) # Adiciona o número na lista de pares
    else:
        odds.append(i)# Adiciona o número na lista de ímpares
print(f'The numbers are: {num}')
print(f'The pairs are: {pairs}')
print(f'The odds are: {odds}')
print('End of program.')