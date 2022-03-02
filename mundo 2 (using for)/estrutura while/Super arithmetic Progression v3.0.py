print('PA Generator')
print('-='*15)
first = int(input("Enter the first term of the AP: "))
reason = int (input('Reason PA: '))
term = first
cont = 1
total = 0
more = 10
while more != 0:
    total += more
    while cont <= total:
        print('{} → '.format(term), end=' ')
        term += reason
        cont += 1
    print('-='*15)
    print('---PAUSE---')
    more = int(input('How many terms more? '))
print('END')


