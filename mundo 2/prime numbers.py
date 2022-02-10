num = int(input('Type a number: '))
tot = 0 # total
for c in range (1, num + 1): 
    if num % c == 0: # se o resto da divisão for zero, significa que o número é divisível por ele
        print(c, end=' ')
        tot += 1 # soma +1 ao total
print('\n') # para quebrar linha
if num == 1:
    print('1 is not a prime number')
else:
    print('{} has {} divisors'.format(num, tot))
    if tot == 2:
        print('{} is a prime number'.format(num))
    else:
        print('{} is not a prime number'.format(num))