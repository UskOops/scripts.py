array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        array[l][c] = int(input(f'Type the {l+1}º value for position [{l},{c}]: '))
print('=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{array[l][c]:^5}]', end='')
    print()
print('=-'*15)
print(f'The sum of the values in the arrays is {sum(sum(array))}')
