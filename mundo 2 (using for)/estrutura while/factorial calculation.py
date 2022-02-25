#from math import factorial
import time
n = int (input('Type a number to calculate factorial: '))
c = n 
f = 1 # factorial starts with 1
print('Calculating...')
time.sleep(4)
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print ('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1

print('The factorial of {} is {}'.format(n, f))
