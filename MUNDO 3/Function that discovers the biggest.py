from time import sleep as sl

def biggest(*n):
    count = biggest = 0
    print('\nAnalizing...') #\n quebra de linha
    print('-=' * 30)
    for value in n:
        print(f'{value}', end=' ', flush=True)
        sl(0.2)
        if count == 0: #se nao tenho nenhum valor, então ele é o maior
            biggest = value
        else:
            if value > biggest:
                biggest = value
        count += 1
    print(f'\nThe biggest value is {biggest}')
        

biggest(2,3,4,5,6,7,8,9,10)
biggest(17,18,19,20)
biggest(6)