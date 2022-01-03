import random
n1 = input('first student: ')
n2 = input('second student: ')
n3 = input('third student: ')
n4 = input('fourth student: ')
list = [n1, n2, n3, n4]
random.shuffle(list) #usando shuffle para embaralhar a lista
print('The order of the students is: ')
print(list)
