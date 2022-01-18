from random import randint #importando a função randint do módulo random
from time import sleep #importando a função sleep do módulo time
computer = randint(0, 6) #gerando um número aleatório entre 0 e 6
print('-=-' * 15) #imprimindo 10 traços
player = int(input("Say a number between 0 and 6: ")) #pedindo o número ao jogador
print('processing...')
sleep(3) #aguardando 3 segundos
print('-=-' * 15) 
print ('You say: {}'.format(player)) #imprimindo o número ao jogador
if player == computer: #verificando se o número ao jogador é igual ao número aleatório
    print('You win!') 
else:
    print('You lose!')
print('-=-' * 15)
print('The number was {}'.format(computer)) #imprimindo o número aleatório
print('-=-' * 15)