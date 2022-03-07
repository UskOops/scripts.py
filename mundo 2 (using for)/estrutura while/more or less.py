answer = 'Y'
sum = qtde = average = more = less = 0 #if all variavles receving 0, can u put them in the same line
while answer in 'Yy':
    num = int(input('Type a number: '))
    sum += num
    qtde += 1
    if qtde == 1:
        more = less = num
    else:
        if num > more:
            more = num
        if num < less:
            less = num
    answer = input('Do you want to continue? [Y/N] ').upper().strip()
average = sum / qtde
print(f'The average of {qtde} numbers is {average}')
print(f'The biggest number is {more} and the lowest is {less}')
