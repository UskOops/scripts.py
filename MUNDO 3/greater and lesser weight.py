name = []
weight = []
for p in range(0, 6):
    name.append(input('Type the NAME: '))
    weight.append(int(input('Type the WEIGHT: ')))
for p in range(0, 6):
    if weight[p] >= 80:
        print(f'{name[p]} , is overweight')
        name += 1
    else:
        print(f'{name[p]} , is not overweight')
        weight += 1
print('='*15)
print(f'Total of overweight people: {weight.count(80)}')
print(f'Total of not overweight people: {weight.count(79)}')