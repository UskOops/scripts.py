from random import randint

v = 0
while True:
    player = int(input('Type a value: ')) #while True is a loop that will continue to run until the user types a value positives or negatives
    computer = randint(0, 10)
    total = player + computer
    type =''
    while type not in 'PI':
        type = str(input('Do you want to continue? [P/I] ')).strip().upper()
    print(f'You played {player} and the computer {computer}. The total is {total}')
    print('It is even' if total % 2 == 0 else 'It is odd', end=' ')
    if type == 'P':
        if total % 2 == 0:
            print('You Win!')
            v += 1
        else:
            print('You Lose!')
            break
    elif type == 'I':
        if total % 2 == 0:
            print('You Win!')
            v += 1
        else:
            print('You Lose!')
            break
    print('Let´s play again!')
print(f'GAME OVER! You won {v} times.')
