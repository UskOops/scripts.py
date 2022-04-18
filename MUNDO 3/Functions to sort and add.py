from random import randint as rand
from time import sleep as sl


def sort(list):
    print("Sorting...")
    for count in range(0, 5):
        n = rand(1, 10)
        list.append(n)
        print(f'{n}', end=' ', flush=True)
        sl(0.5)
    print('\nReady!!!')


def sumpair(list):
    sum = 0
    for v in list:  # pra cada valor na lista
        if v % 2 == 0:  # se o valor for divisivel por 2
            sum += v  # soma o valor


    print(f'The sum of the even numbers is: {sum}')

numbers = []
sort(numbers)
sumpair(numbers)
