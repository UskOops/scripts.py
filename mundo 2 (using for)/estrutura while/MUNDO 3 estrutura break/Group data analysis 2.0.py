tot18 = totM = totalW =0

while True:
    age = int(input("Enter your age: "))
    sex = ' '
    while sex not in 'MF':
        sex = (input('SEX: [M/F]')).strip().upper()[0]
    if age >= 18:
        tot18 += 1

    if sex == 'M':
        totM += 1

    if sex == 'F' and age < 20:
        totalW += 1


    answer = ' '
    while answer not in 'SN':
        answer = (input('Do you wanna continue? [S/N]')).strip().upper()
        print('====='*15)
    if answer == 'N':
        break
    print(f'Total of people with age more 18: {tot18}')
    print(f'In total we have {totM} MAN registered')
    print(f'In total we have {totalW} WOMAN registered')