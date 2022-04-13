def counter(i, f, s): #i = initial, f = final, p = step
    print(f'Counter the {i} at {f} the {s} in the {s}')
    print('~'*20)
    
    if i < f:
        count = i
        while count <= f:
            print(f'{count}', end=' ')
            count += s
    print('END!')
counter(0,100,10) #contador de 0 a 100 de 1 em 1
counter(100,0,-10) #contador de 100 a 0 de -1 em -1
counter(0,10,2) #contador de 0 a 10 de 2 em 2

