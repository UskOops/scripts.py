from interface import *
from time import sleep as sl

while True:
    answer = menu (['Create file', 'Register people', 'List people', 'Exit'])
    if answer == 1:
        print('Creating file')
    elif answer == 2:
        print('Registering people')
    elif answer == 3:
        print('Listing people')
    elif answer == 4:
        print('Exiting...')
        break
    else:
        print('Invalid option')
    sl(0.5)
       

        