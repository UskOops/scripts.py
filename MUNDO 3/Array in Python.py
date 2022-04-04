array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumeven = bigger = sumcol = 0 # sumeeven = soma dos pares, more = maior valor, sumcol = soma das colunas
for l in range(0, 3):
    for c in range(0, 3):
        array[l][c] = int(input(f'Type the {l+1}º value for position [{l},{c}]: '))
print('=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{array[l][c]:^5}]', end='')
        if array[l][c] % 2 == 0:  #se a matriz L C for par
            sumeven += array[l][c] #ele faz a soma dos pares, recebe o valor da matriz
    print()
print('=-'*15)
print(f'The sum of even numbers is: {sumeven} ')
for l in range(0, 3):
    sumcol += array[l][2] #soma das colunas recebe o valor da matriz na linha L e coluna 2
print(f'The sum of the third column is: {sumcol} ')
print('=-'*15)
for c in range (0, 3):
    if c == 0:
        bigger = array[1][c] #maior valor recebe o valor da matriz na linha 1 e coluna C
    elif array[1][c] > bigger: #se o valor da matriz na linha L e coluna C for maior que o maior valor
        bigger = array[1][c] #maior valor recebe o valor da matriz na linha 1 e coluna C
print(f'The biggest value is: {bigger} ')


