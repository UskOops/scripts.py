days = int(input("How many days you rent the car? "))
km = float(input("Enter the number of kilometers driven: "))
pay = days * 60
km = km * 0.15
total = pay + km
print("The total payment is: ", total)