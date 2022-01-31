weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))
imc = weight / (height ** 2)
print("Your IMC is: {:.2f}".format(imc))
if imc < 18.5:
    print("Underweight")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Overweight")
else:
    print("Obese")
    