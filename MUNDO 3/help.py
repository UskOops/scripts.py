"""Utilizando dockstring"""

# def counter(i, e, p): #init #end #pass
#    """This function counts from i to e in steps of p."""
#    c = i
#    while c <= e:
#        print(f'{c}', end='..')
#        c += p
#    print('\nReady!!!')
# counter(2, 10, 2)
#
# help(counter)

"""paramentros opcionais"""

# def sum(a, b, c=0):  # parametros opcionais, atribuir 0 como padrão
#    """This function sums a, b and c."""
#    s = a + b + c
#    print(f'The sum is {s}')
#sum (1, 2, 3)
#sum (1, 2)

"""escopos de variaveis"""

# def teste():
#    x = 1 #variavel local --> so funciona dentro da função
#    print(f'n != {n}')
#    print(f'x = {x}')
#
# n = 10 #variavel global --> funciona dentro e fora da função
#print(f'n = {n}')
#x = 0
# teste()
#print(f'x = {x}')

"""retorno de valores"""

#def sum(a=0, b=0, c=0):
#    s = a + b + c
#    return s #usando return para retornar o valor
#r1 = sum (3, 4, 5)
#r2 = sum (2, 4)
#r3 = sum (4)
#print(f'the values are {r1}, {r2}, {r3}')