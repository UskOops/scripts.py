from random import randint
from time import sleep
list = []
games = []
print('='*15)
print('{:^15}'.format('MEGA SENA'))
print('='*15)
qtde = int(input('how many games do you want to make?  '))
tot = 1
while tot <= qtde:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            count += 1
        if count >= 6:
            break
    list.sort()
    games.append(list[:])
    list.clear()
    tot += 1
print('-'*15)
print('='*3, f' GENERATED {qtde} GAMES ', '='*3)
print('loading...')
sleep(2.5)
print('-'*15)
for i, l in enumerate(games):
    print(f'Game {i+1}: {l}')
    sleep(0.5)


