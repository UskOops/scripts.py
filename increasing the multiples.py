salary =  float(input('what is your salary? '))
if salary <= 2550:
    new = salary + (salary * 12 / 100) #dividindo por 100 para transformar em porcentagem
else:
    new = salary + (salary * 8 / 100)
print('who received a salary R$ {:.2f} now you will receive a salary R$ {:.2f}'.format(salary, new))#formatando o valor