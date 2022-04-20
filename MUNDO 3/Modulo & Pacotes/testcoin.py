import Coin

price = float(input("Enter the price: R$ "))
print(f'The half of {price} is {Coin.half(price)}')
print(f'The double of {price} is {Coin.double(price)}')
print(f'The price up 10% is {Coin.up(price, 10)}')
print(f'The price down 10% is {Coin.down(price, 20)}')

