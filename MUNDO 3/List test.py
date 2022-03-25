list = [1,3,5,7,9] #lembrando que parte da posição 0
list[2] = 3 #substitui o valor da posição 2
list.append(11) #adiciona o valor 11 na lista
list.insert(2,4) #adiciona o valor 4 na posição 2
if 4 in list:
    print('4 está na lista')
else:
    print('4 não está na lista')
print('='*15)
list.remove(3) #remove o valor na posição 3 da lista
print(list)
print('='*15)
print(f'O tamanho da lista é {len(list)}')