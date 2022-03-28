numbers = []
while True:
    n = input('Type a value: ')
    if n not in numbers: # Verifica se o valor digitado já existe na lista se não existir adiciona na lista
        numbers.append(n) #append adiciona um valor na lista
        print('Value added successfully')
    else:
        print('This value already exists.')
    answer = input('Do you want to continue? [Y/N] ')
    if answer in 'Nn':
        break
print('='*15)
#numbers.sort() # Ordena a lista
print(f'You typed {len(numbers)} values') #basta tirar o len e voce vera uma lista ordenada