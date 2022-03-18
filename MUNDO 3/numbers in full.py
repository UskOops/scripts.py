count = ('zero', 'one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
           'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    while True:
        num = int(input('Type a number between 0 and 20: '))
        if 0 <= num <=20:
            break
        print('Invalid number. ', end='')
    print(f'The number entered was {count[num]}.')
    print(' ')
    answer = str(input('Do you want to continue?[Y/N]: ')).upper().strip()
    if answer == 'N':
        break
print('-' * 40)
print('HAVE A GOOD DAY')
    

