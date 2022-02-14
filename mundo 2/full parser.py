sumage = 0 #soma idade
averageage = 0 #media idade
bigageH = 0 #maior idade homem
nameold = '' #nome da pessoa mais velha
totwoman25 = 0 #total de mulheres -25 anos

for p in range(1,5): #numero de pessoas
    name = input('Type the NAME of the person: ')
    age = int(input('Type the AGE of the person: '))
    sex = (input('Sex [M/F]: ')).strip()
    sumage += age
if p == 1 and sex in 'Mm': # se a pessoa for a primeira e o sexo for masculino
    bigageH = age
    nameold = name
if sex in 'Mm' and age < bigageH:
    bigageH = name
    nameold = name
if sex in 'Ff' and age > 25: 
    totwoman25 += 1
averageage = sumage / 4
print('The average of age in group is {}'.format(averageage))
print('In this case have {} womans with most 20 age'.format(totwoman25))
print('The oldest person is {} with {} years old'.format(nameold, bigageH))

