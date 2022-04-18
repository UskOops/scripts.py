def factorial(num=1):
    f = 1
    for i in range(num ,0, -1):
        f *= i
    return f

#n = int(input("Type a number: "))
#print(f'The factorial of {n} is: {factorial(n)}')
f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f' The results are: {f1}, {f2}, {f3}')
print()

print('------------------codigo de teste------------------')

def pair(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Type a number: "))
print(f'The number {num} is even: {pair(num)}')

   