#using break command
n = s = 0
while n != 999:
    n = int(input('Type a number: '))
    s += n
    if n == 999:
        break
print(f'The sum of the numbers is {s}')