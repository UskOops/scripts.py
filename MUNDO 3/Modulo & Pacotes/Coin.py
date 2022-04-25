def up(price=0, rate=0, format=False):
    answer =  price + (price * rate/100)
    return answer

def down(price=0, rate=0, format=False):
    answer = price - (price * rate/100)
    return answer if format is False else coin(answer, '.2f')
    

def double(price=0, format=False):
    answer = price * 2
    return answer if not format is False else coin(answer, '.2f')

def half(price=0, format=False):
    answer = price / 2
    return answer if not format is False else coin(answer, '.2f')

def coin(price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')

def resume(price=0, rate=10, format=False):
    return f'{coin(up(price, rate, format), "")} - {coin(down(price, rate, format), "")}'