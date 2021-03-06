from interface import *

def archexist(name):
    try:
        a = open(name, 'rt') # rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create_archive(name):
    try:
        a = open(name, 'wt+') # wt = write text
        a.close()
    except:
        print('Error creating archive')
    else:
        print(f'Archive {name} created')

def readarchive(name):
    try:
        a = open(name, 'rt') 
    except:
        print('Error reading archive')
    else:
        header('People in the archive')
        for line in a:
            data = line.split(';') #split = separa a string em uma lista usando ; como separador
            data[1] = data[1].replace('\n', '') #replace = substitui o \n por nada
            print(f'{data[0]:<8} ---- age: {data[1]:>3}') #dado 1 = idade



def cad(arch, name='unknown', age=0):# se não for passado nome e idade, nome sera desconhecido e idade 0
    try:
        a = open(arch, 'at') # at = append text
    except:
        print('Error writing archive')
    else:
        a.write(f'{name};{age}\n')
        print(f'{name} registered with age {age}')