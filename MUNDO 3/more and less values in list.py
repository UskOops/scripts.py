values = []
for c in range(0, 5):
    values.append(int(input(f'Type a value for position {c}: ')))
print('='*15)
print(f'You typed the following values: {values}')
print('='*15)
print(f'The most value typed is {max(values)} in position {values.index(max(values))}') # index returns the position of the max or less value
print('='*15)
print(f'The less value typed is {min(values)} in position {values.index(min(values))}') 
print('='*15)
print(f'The sum of all values typed is {sum(values)}')
print('='*15)
print(f'The average of all values typed is {sum(values)/len(values)}')