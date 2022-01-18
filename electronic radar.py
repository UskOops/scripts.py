speed = float(input("Enter the speed of the vehicle in km/h: "))
if speed > 80: #se a velocidade for maior que 80km/h
    print("You are going too fast, take your traffic ticket!")
    ticket = (speed - 80) * 7 #calculando o valor da multa
    print("The value of your ticket is R${:.2f}".format(ticket)) #formatando o valor da multa
else: #caso contrario se a velocidade for menor que 80km/h
     print("You are driving safely, have a nice day! :) ")
