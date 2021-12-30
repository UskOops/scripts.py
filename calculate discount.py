price = float(input("Enter the price of the item? R$"))
new = price - (price * 0.05) # 5% disconto
print(f'The price of the item is R${price:.2f} and the new price is R${new:.2f}')