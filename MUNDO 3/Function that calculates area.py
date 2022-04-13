def area(l, w): #função que calcula a área, passo o parametro l e w dentro da função
    a = l * w #variavel que recebe a multiplicação de l e w (os parametros)
    print(f'The area of land is {l } x {w} is {a} m2 ')
#programa principal
print('---Land Control--')
l = float(input('Enter the length of the land(m): '))
w = float(input('Enter the width of the land(m): '))
print('-' * 20)
area(l, w) #chama a função area e passa os parametros l e w