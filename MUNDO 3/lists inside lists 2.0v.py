num = [[], []]
value = 0
for c in range(1, 8):
    value = int(input(f'Type the {c}o. value: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)
print('-='*15)
print(f'List of even numbers: {num[0]}')
print(f'List of odd numbers: {num[1]}')
print('-='*15)
print(f'The sum of even numbers: {sum(num[0])}')
print(f'The sum of odd numbers: {sum(num[1])}')
print('-='*15)
print(f'The average of even numbers: {sum(num[0])/len(num[0])}')
print(f'The average of odd numbers: {sum(num[1])/len(num[1])}')
print('-='*15)
