def datasheet(player='<unknown>', gols=0): #parametros opcionais
    print (f'The {player} as scored {gols} goals')

#main
name  = input("Enter with the player name: ")
gols = input("Enter with the player goals: ")
if gols.isnumeric(): # se o que eu digitar for um número, ele vai entrar no if.
    gols = int(gols) # se eu digitar um número, ele vai converter para inteiro.
else:
    gols = 0 # se eu digitar algo que não seja um número, ele vai entrar no else e o gols vai ser 0.
if name.strip() == "":
    datasheet(gols=gols)
else:
    datasheet(name, gols)