def area(l, w):
    a = l * w
    print(f'The area of land is {l}x{w} is {a}m2 ')
#programa principal
print('---Land Control--')
print('-' * 20)
l = float(input('Enter the length of the land: '))
w = float(input('Enter the width of the land: '))
print('-' * 20)
area(l, w)