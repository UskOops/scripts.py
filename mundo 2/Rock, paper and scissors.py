from random import randint
items = ('rock', 'paper', 'scissors') # lista de opções
IA = randint(0, 2) # escolhe aleatoriamente uma das opções
print ('''You can choose between:
[0] - rock
[1] - paper
[2] - scissors''')
player = int(input('Choose your option: '))
print ('-=' * 15)
print ('the computer chose: {}'.format(items[IA]))
print ('you chose: {}'.format(items[player]))
print ('-=' * 15)
if IA == player:
    print ('DRAW!')
elif IA == 0 and player == 1:
    print ('You win!')
elif IA == 0 and player == 2:
    print ('You lose!')
elif IA == 1 and player == 0:
    print ('You lose!')
elif IA == 1 and player == 2:
    print ('You win!')
elif IA == 2 and player == 0:
    print ('You win!')
elif IA == 2 and player == 1:
    print ('You lose!')
else:
    print ('Invalid option!')


