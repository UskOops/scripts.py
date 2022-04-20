#'import utilizavel' desse metodo você aponta o caminho para o arquivo usando o . //exemplo #todo utilizavel.factorial
"""a primeira maneira é a mais recomendada"""
from utilizavel import factorial, double

num = int(input("Type a value: "))
fat = factorial(num)
print(f'The factorial of {num} is {fat}')
print(f'Double of {num} is {double(num)}')