from random import randint
from time import sleep
from operator import itemgetter #itemgetter is used to sort the list
game = {'Marco': randint(1, 6), 'Gaby': randint(1, 6), 'Feu': randint(1, 6), 'Lucas': randint(1, 6)}
ranking = ()
print('VALUES SORTED: ')
print('waiting...')
sleep(3)
for key, value in sorted(game.items()):
    print(f'{key} take {value} in the dice')
    sleep(1)
print('\n')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True) 
print('-=' * 13)
print('RANKING OF THE PLAYERS: ')
print('-=' * 15)
for indice, value in enumerate(ranking):
    print(f'{indice+1}º place: {value[0]} with {value[1]}') #tupla dentro de uma lista
    sleep(1)
print('\n')
print('-=' * 13)
print('THANKS FOR PLAYING!')
