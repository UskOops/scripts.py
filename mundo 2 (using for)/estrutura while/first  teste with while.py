n = 1
pair = odd = 0 # par e ímpar inicializados com 0
while n != 0: #enquanto n for diferente de 0
    n = int(input('Type a value: ')) #pega o valor do número
    if n % 2 == 0: #se o número for par
        pair += 1 #soma 1 ao contador de pares
    else: #se não for par
        odd += 1 #soma 1 ao contador de ímpares
print('Number of pairs {} and odd {} '.format(pair, odd)) #imprime o contador de pares