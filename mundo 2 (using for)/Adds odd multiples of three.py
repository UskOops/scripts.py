sum = 0
count = 0
for c in range (1, 525, 2):
    if c % 3 == 0: #se c é múltiplo de 3
        count += 1 #incrementa +1 ao valor
        sum += c #soma ou adiciona o valor
print ('the sum of all values ​​is {} and the number of values ​​is {}'.format(sum, count))
