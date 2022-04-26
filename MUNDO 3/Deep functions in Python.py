def readnum(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print("Invalid input. Please try again.")
            continue #volta ao inicio do while
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
        else:
            return n

def readfloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print("Invalid input. Please try again.")
            continue 
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()
        else:
            return n


num = readnum(input("Enter a number: "))
num2 = readfloat(input("Enter a real number: "))
print(f'The integer is {num} and the real number is {num2}')