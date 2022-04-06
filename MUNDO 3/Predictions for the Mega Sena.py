from random import randint
from time import sleep
list = []
games = []
print('='*15)
print('{:^15}'.format('MEGA SENA'))
print('='*15)
qtde = int(input('how many games do you want to make?  '))
tot = 1 # variável para o cálculo do total de números sorteados
while tot <= qtde:
    count = 0
    while True: 
        num = randint(1, 60)
        if num not in list: # se o número não estiver na lista, ele será adicionado
            list.append(num) # adiciona o número sorteado na lista
            count += 1 # conta quantos números foram sorteados
        if count >= 6:# se o número de números sorteados for igual ou maior que 6, sai do loop
            break
    #list.sort() # ordena a lista (opcional)
    games.append(list[:]) # adiciona a lista de números sorteados na lista de jogos
    list.clear() # limpa a lista para que possa receber novos números
    tot += 1 # conta quantos jogos foram feitos
print('-'*15)
print('='*3, f' GENERATED {qtde} GAMES ', '='*3)
print('loading...')
sleep(2.5)
print('-'*15)
for i, l in enumerate(games): # enumerate para mostrar o número do jogo
    print(f'Game {i+1}: {l}') # mostra os números sorteados
    sleep(0.5)


