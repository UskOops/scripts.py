number = int(input('write a number for see your time table: '))
for c in range(1, 11): #range=começando de zero e incrementando em 1 e para antes do número fornecido                      
    print(number, 'x', c, '=', number * c) #identação é importante no python 
                                             # quando se chama algo dentro de um laço, é necessario dar espaço