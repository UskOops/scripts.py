print('PA Generator')
print('-='*15)
first = int(input("Enter the first term of the AP: "))
reason = int (input('Reason PA: '))
term = first
cont = 1
while cont <= 10:
    print('{} → '.format(term), end=' ')
    term += reason
    cont += 1
print('The END')
print('-='*15)
