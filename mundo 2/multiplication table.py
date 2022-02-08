from time import sleep
number = int(input("Type a number to see your multiplication table: "))
for i in range(1, 11):
    sleep(1)
    print(number, "x", i, "=", number * i) #printar o resultado da multiplicação