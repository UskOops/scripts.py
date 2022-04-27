from interface import *
from time import sleep as sl
from archive import *

arch = 'TESTE.txt'

if not archexist(arch):
    create_archive(arch)

while True:
    answer = menu (['List people', 'Register people', 'Exit'])
    if answer == 1:
        header('REGISTERED PEOPLE...')
        #list content of archive
        readarchive(arch)
    elif answer == 2:
        print('----New cadastre----')
        print()
        name = input('Name: ')
        sl(0.3)
        age = readint('Age: ')
        sl(0.3)
        print('writing...')
        sl(0.8)
        print(f'Registering {name}...')
        sl(0.3)
        cad(arch, name, age) #cadastro recebe o nome e idade
    elif answer == 3:
        print('Exiting...')
        break
    else:
        print('Invalid option')
    sl(0.5)
       

        