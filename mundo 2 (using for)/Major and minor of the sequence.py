weight = [50, 60, 70, 80, 90, 100] # valores de peso em lista
for p in range(0,5):
    weight.append(float(input("Enter the weight of the person: ")))
    print('The highest weight is: ', max(weight))
    print('The lowest weight is: ', min(weight))
    