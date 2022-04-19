def readint(msg):
    ok = False
    value = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print("Invalid input, please try again!")
        #if ok:
        #    break
            return value
#main
n = readint("Enter an integer: ")
print("You entered", n)
