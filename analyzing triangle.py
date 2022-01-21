print('-=' * 15)
print('analyzing triangle')
print('-=' * 15)
r1 = float(input('first follow-up: '))
r2 = float(input('second follow-up: '))
r3 = float(input('third follow-up: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print('It is a triangle')
else:
    print('It is not a triangle')