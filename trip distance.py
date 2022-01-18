import time #import time module
distance = float(input("How far is your trip?: "))
print('you are about to start a journey', distance, 'km') #printando a distancia
print('please wait...')
time.sleep(3)
if distance <= 200: #menor ou igual a 200
    price = distance * 0.50 
else:
    price = distance * 0.45 #cada km custa 0.45
    
print('the price of your journey is $', format(price, '.2f'))#formatando o valor
print('thank you for using our program...')