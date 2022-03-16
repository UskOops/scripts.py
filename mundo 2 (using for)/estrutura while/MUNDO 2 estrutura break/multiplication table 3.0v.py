while True: 
    n = int(input('What multiplication table do you want? '))
    print('-' * 15)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')# c is count
    print('-' * 15)
    if n == 0:
        break
    elif n < 0:
        print('You can\'t use a negative number.')
        break
print('Bye!')