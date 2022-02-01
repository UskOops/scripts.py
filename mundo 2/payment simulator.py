print(f'{"Payment simulator":=^40}')
price = float(input('Enter the purchase price: R$'))
print('''Payment options:
[1] - Credit card
[2] - Debit card
[3] - Cash''')
option = int(input('Enter the payment option: '))
if option == 1:
 total = price + (price * 1.50 / 100)
elif option == 2:
 total = price - (price * 5 / 100)  # 5% de desconto
elif option == 3:
 total = price - (price * 8 / 100) 
else:
    print('INVALID OPTION!!!')
print('your purchase worth R${:.2f} it will cost R$ {:.2f} in the end'.format(price,total))
print('='*40)
print('Thank you for using our payment simulator')