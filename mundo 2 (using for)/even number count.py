from time import sleep
for count in range (0, 100, 2):
        print(count, end=('\r')) # \ é um caracter de escape, \r é um caracter de retorno sequencial
        sleep(0.5)
print("Congrats, you lost your time xD!")