print(f'{"="*15} ATM SIMULATOR {"="*15}')
print('\n')
value = int(input('Enter the value amount to withdraw: R$ '))
total = value
money = 50
total_money = 0

while True:
    if total >= money:
        total -= money
        total_money += 1
    else:
        if total_money > 0:
            print (f'You received {total_money} notes of R$ {money}.')
        if money == 50:
            money = 20
        elif money == 20:
            money = 10
        elif money == 10:
            money = 1
        total_money = 0  
        if total == 0:
            break
print('\n')
print(f'{"="*15} HAVE A GOOD DAY!!! {"="*15}')
