from time import sleep

n1 = int(input('Type the first value: '))
n2 = int(input('Type the second value: '))
op = 0
while op != 5:
    
    print('''[1] Sum; 
[2] Subtraction;
[3] Multiplication; 
[4] Division; 
[5] Exit''')
    op = int(input('Type the your option: '))
    if op == 1:
        sum = n1 + n2
        print('The sum is: ', sum)
    elif op == 2:
        sub = n1 - n2
        print('The subtraction is: ', sub)
    elif op == 3:
        mul = n1 * n2
        print('The multiplication is: ', mul)
    elif op == 4:
        div = n1 / n2
        print('The division is: ', div)
    elif op == 5:
        print('Exit')
    else:
        print('Invalid option')
        sleep(2)
print('End of the program')

