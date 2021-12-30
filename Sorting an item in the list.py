import random
n1 = input('First name: ')
n2 = input('Second name: ')
n3 = input('Third name: ')
n4 = input('Fourth name: ')
list = [n1, n2, n3, n4]
chose = random.choice(list)
print(f'The chosen name is: {chose}')