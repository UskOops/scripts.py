from datetime import date
actual = date.today().year
born = int(input('Enter your year of birth: '))
age = actual - born
print('Your age is {}'.format(age))
if age <= 12:
    print('You are a kid')
elif age > 12 and age <= 18:
    print('You are a teenager')
elif age > 18 and age <= 30:
    print('You are a young adult')
elif age > 30 and age <= 50:
    print('You are an adult')
elif age > 50 and age <= 80:
    print('You are an old')
