name = []
weight = []
more = less = 0
while True:
    name.append(input("Enter NAME: "))
    name.append(float(input("Enter WEIGHT: ")))
    if len (weight) == 0:
        more = less = name[1]
    elif name[1] > more:
        more = name[1]
    elif name[1] < less:
        less = name[1]

    weight.append(name[:])
    name.clear()
    answer = input("Do you want to continue? (Y/N) ")
    if answer in "nN":
        break
print('-' * 15)
print(f'In total you cadastred: {len(weight)} people')
print(f'THE HEAVIER PERSON IS: {more}')
for p in weight:
    if p[1] == more:
        print(f'{p[0]},', end=' ')
print()
print(f'THE LIGHTER PERSON IS: {less}')
for p in weight:
    if p[1] == less:
        print(f'{p[0]},', end=' ')
        

    