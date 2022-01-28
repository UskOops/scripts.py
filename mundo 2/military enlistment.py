from datetime import date
current = date.today().year #ano atual
born = int(input('year you were born: '))
age = current - born #calcula a idade
print('Who born in {}, has {} years old'.format(born, age))
if age == 18:
    print('You need enlist now!')
elif age > 18:
    balance = age - 18
    print('You should have a enlist!')
elif age < 18:
    balance = age - 18
    print('You are not old enough to enlist!')