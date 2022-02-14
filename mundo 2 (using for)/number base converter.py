num = int(input('type a integer number: '))
print('''Choice a base to convert:
[1] Binary
[2] Octal
[3] Hexadecimal''') # o usuario escolhe a base
option = int(input('your option: '))
if option == 1:
    print('{} convert to binary is {}'.format(num, bin(num)[2:])) # [2:] para tirar o 0b
elif option == 2:
    print('{} convert to octal is {}'.format(num, oct(num)[2:])) # [2:] para tirar o 0o
elif option == 3:
    print('{} convert to hexadecimal is {}'.format(num, hex(num)[2:])) # [2:] para tirar o 0x
else:
    print('invalid option')


