from random import randint
computer = randint(0, 10)
print('I am thinking of a number between 0 and 10.')
print('You can guess was number it?')
Won = False
Guesses = 0
while not Won:
    player = int(input('Your guess: '))
    Guesses += 1 
    if player == computer:
        print('YOU WIN!')
        Won = True
    elif player < computer:
        print('Your guess is too HIGH.')
    else:
        print('Your guess is too LOW.')
print('You win with {} guesseds!.'.format(Guesses))

