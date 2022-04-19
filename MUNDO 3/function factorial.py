def factorial(n, show=False):
    """Calculate the factorial of a number.
    :param n: number
    :param show: show the result
    :return: the factorial of n"""
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

#main
print(factorial(5, show = True)) #se eu colocar show = True, ele vai mostrar o cálculo, se não, não vai mostrar nada.