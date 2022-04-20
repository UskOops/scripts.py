def up(price, rate):
    answer =  price + (price * rate/100)
    return answer

def down(price, rate):
    answer = price - (price * rate/100)
    return answer

def double(price):
    answer = price * 2
    return answer

def half(price):
    answer = price / 2
    return answer