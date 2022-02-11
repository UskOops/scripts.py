from datetime import datetime
now = datetime.now().year
tlarger = 0 # contador de pessoas maiores de idade
tlower = 0 # contador de pessoas menores de idade
for p in range (1,8): # loop para 8 pessoas
    born = int(input('What year were you born? '.format(p)))
    age = now - born #calcula a idade
    print('You are {} years old.'.format(age))
    if age > 18:
        tlarger += 1 #incrementa o contador de maiores de idade
        
    else:
        tlower += 1 #incrementa o contador de menores de idade
print('You have {} people older than 18 and {} people younger than 18.'.format(tlarger, tlower))