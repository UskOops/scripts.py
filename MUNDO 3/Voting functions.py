# from datetime import date as dt #caso de uso: se for chamado somente dentro da def(função), economiza memoria


def vote(year):
    from datetime import date as dt
    actual = dt.today().year
    age = actual - year
    if year < 16:
        return f'With your age {age}, you NOT can vote'
    elif 16 <= age < 18 or age > 65:
        return f'With your age {age}, you can vote (OPTIONAL)'
    else:
        return f'With your age {age}, you NEED vote'

born = int(input('Enter your year of birth: '))
print(vote(born))
