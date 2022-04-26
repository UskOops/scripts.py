from interface import *
from time import sleep as sl
from archive import *

arch = 'TESTE.txt'

if not archexist(arch):
    create_archive(arch)

while True:
    answer = menu (['List people', 'Register people', 'Exit'])
    if answer == 1:
        print('Registering people')
        #list content of archive
        readarchive(arch)
    elif answer == 2:
        print('Listing people')
    elif answer == 3:
        print('Exiting...')
        break
    else:
        print('Invalid option')
    sl(0.5)
       

        