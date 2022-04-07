from libcst import While
from numpy import average


token = []
while True:
    name = str(input("Enter NAME: "))
    result1 = float(input("Enter result 1: "))
    result2 = float(input("Enter result 2: "))
    average = (result1 + result2) / 2
    token.append([name, [result1, result2], average])
    answer = str(input("Do you want to continue? (Y/N): "))
    if answer in "Nn":
        break
print("-" * 40)
print("{:<10}{:<10}{:<10}{:<10}".format("NAME", "RESULT 1", "RESULT 2", "AVERAGE"))
print("-" * 40)
for i, a in enumerate(token): # i = indice, a = aluno
    print("{:<10}{:<10}{:<10}{:<10}".format(a[0], a[1][0], a[1][1], a[2]))
while True:
    print("-" * 40)
    options = int(input('Show results of which student? (type 999 to exit): '))
    if options == 999:
        print('WAIT...')
        break
    if options <= len(token) - 1:
       print(f'{token[options][0]} average: {token[options][2]}')
    else:
        print('Invalid option')
print('-' * 40)
print('END')
print('-' * 40)
