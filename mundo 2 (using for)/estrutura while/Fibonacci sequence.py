print('---'*15)
print('----FIBONACCI SEQUENCE----')
print('---'*15)
n = int(input('How many terms you can show ? '))
t1 = 0
t2 = 1
print('***'*15)
print('{} → {} → '.format(t1, t2), end=' ')
cont = 3 #while cont is less than n
while cont <= n:
    t3 = t1 + t2
    print('{} → '.format(t3), end=' ')
    t1 = t2
    t2 = t3 # cont continue do it
    cont += 1
