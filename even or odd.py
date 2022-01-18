number = input('Tell me a number: ')
result = int(number) % 2 #modulo de operação
if result == 0: #se o resultado for 0, então é par
    print('The number is even!')
else: #se não for, então é impar
    print('The number is odd!')
