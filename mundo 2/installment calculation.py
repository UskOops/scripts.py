house = float(input("Enter the price of the house: "))
salary = float(input("Enter your salary:  R$"))
years = int(input("Enter the number of years you want to pay the house: "))
installment = house / (years * 12)
min = salary * 30 / 100
if installment <= min:
  print("Your installment is {} and you can pay it with your salary.".format(installment))
else:
  print("Your installment is {} and you can't pay it with your salary.".format(installment))
  print('Your monthly installment is R$ {:.2f}'.format(installment)) #valor do parcelamento
  print('Your minimum monthly payment is R$ {:.2f}'.format(min)) #minimo que pode ser pago
  print('Your total payment is R$ {:.2f}'.format(min * 12)) #12 is the number of months