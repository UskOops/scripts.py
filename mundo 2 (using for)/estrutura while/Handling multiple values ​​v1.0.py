#not relevant for using
num = cont = sum = 0
num = int(input('Type a number [999 to stop!]: '))
while num != 999:
    sum += num # sum = sum + num
    cont += 1
    num = int(input('Type a number [999 to stop!]: '))
    print(f'The sum of the {cont} numbers is {sum}')
print('-_-_-_End of program_-_-_-')