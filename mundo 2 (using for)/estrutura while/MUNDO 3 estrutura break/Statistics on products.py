total = totmil = less =  count = 0
cheap = ' '

while True:
    product = input('Enter the product name: ')
    if product == 'stop':
        break
    price = float(input('Enter the price R$: '))
    count += 1
    total += price
    if price >= 1000:
        totmil += 1
    
    if count == 1 or price < cheap:
        less = price
        cheap = product

    answer = ' '
    while answer not in 'YN':
        answer = input('Do you want to continue? [Y/N] ').upper()
    if answer == 'N':
        break
print (f'TOTAL: {total:.2f} reais')
print (f'Total of products that cost more than R$1000: {totmil}')
print (f'The less expensive product is: {cheap} and, costs R${less:.2f}')
print('{:=^40}'.format(' End of program '))
