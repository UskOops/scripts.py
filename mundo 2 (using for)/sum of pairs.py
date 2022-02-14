sum = 0
count = 0
for c in range (1, 10):
    num = int(input('Type a value: '))
    if num % 2 == 0:
        sum += num
        count += 1
print ('the sum of all values ​​is {} and the number pairs of values ​​is {}'.format(sum, count))
    