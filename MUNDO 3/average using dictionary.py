student = {}
student['name'] = input('Enter your name: ')
student['average'] = float(input(f'Average of {student["name"]}: '))
print('='*20)
if student['average'] >= 7:
    print(f'{student["name"]} is aprovred!')
elif 5 <= student['average'] < 7:
    print(f'{student["name"]} is aproved with a warning!')
else:
    print(f'{student["name"]} is reprovided!')
print('=' * 30)
for key, value in student.items():
    print(f'- {key}: {value}')
