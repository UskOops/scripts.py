values = []
while True:
    values.append(int(input('Type a value: ')))
    answer = (input('Do you want to continue? [Y/N] ')).strip().upper()[0] # strip() remove os espaços antes e depois da string
    if answer in 'Nn':
        break
print(f'You typed {len(values)} values.')
values.sort(reverse=True) #ordena a lista de forma decrescente
print(f'The values typed in order are: {values}')
if 5 in values:
    print('The value 5 appears in the list.')
else:
    print('The value 5 does not appear in the list.')
