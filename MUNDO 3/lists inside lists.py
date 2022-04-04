people = []
data = []
totmore = totless = 0
for c in range(0, 3):
   data.append(input('Type the NAME: '))
   data.append(int(input('Type the AGE: ')))
   people.append(data[:])
   data.clear()
for p in people:
    if p[1] >= 21:
        print(f'{p[0]} , is old enough to vote')
        totmore += 1
    else:
        print(f'{p[0]} , is not old enough to vote')
        totless += 1
print('='*15)
print(f'Total of people that can vote: {totmore}')