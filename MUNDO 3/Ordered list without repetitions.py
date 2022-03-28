list =  []
for c in range(0,5):
    n = int(input('Type a value: '))
    if c == 0 or n > list[-1]: #se c for igual a 0 ou se o ultimo elemento da lista for maior que o n(numero)
        list.append(n)
    else:
        pos = 0
        while pos < len(list): #enquanto a posição for menor que o tamanho da lista
            if n <= list[pos]: #se o n for menor ou igual ao elemento da lista na posição pos
                list.insert(pos, n) #insere o n na posição pos
                break
            pos += 1 #incrementa a posição
print('='*15)
print(f'The values typed in order are: {list}')
    
