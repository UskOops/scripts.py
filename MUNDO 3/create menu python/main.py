from interface import *
from time import sleep as sl
from archive import *

arch = 'TESTE.txt'

if not archexist(arch):
    create_archive(arch)

while True:
    answer = menu (['List people', 'Register people', 'Exit'])
    if answer == 1:
        print('REGISTERED PEOPLE...')
        #list content of archive
        readarchive(arch)
    elif answer == 2:
        print('New cadastre')
        name = input('Name: ')
        sl(0.3)
        age = readint('Age: ')
        sl(0.3)
        print(f'Registering {name} with age {age}')
        sl(0.3)
        cad(arch, name, age) #cadastro recebe o nome e idade
    elif answer == 3:
        print('Exiting...')
        break
    else:
        print('Invalid option')
    sl(0.5)
       

        