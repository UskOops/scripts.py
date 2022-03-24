list = ('pencil',2.5,'pen',3.5,'eraser',1.5,'marker',4.5,'copybook',5.5)
print('-'*25)
print(f'{"LIST OF PRICE":^25}')
print('-'*25)
print('ITEM\t\tPRICE')
for pos in range(0,len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:<16.5}',end='')
    else:
         print(f'R$ {list[pos]:<7.2f}')