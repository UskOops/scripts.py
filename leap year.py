from datetime import date #importa a biblioteca date
year = int(input("What year you want to analyze? Put 0 to analyze current year: "))
if year == 0: #se o ano for 0, o programa analisa o ano atual
    year = date.today().year #pega o ano atual
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #se o ano for divisivel por 4 e não por 100 ou se for divisivel por 400
    print("{} is a leap year".format(year)) #imprime o ano e a mensagem de que é um ano bissexto
else:
    print("{} is not a leap year".format(year)) #imprime o ano e a mensagem de que não é um ano bissexto
    #{} é um formato de string, ou seja, é um espaço para que o programa imprima o ano
    #o .format() é um método do python que permite que o programa imprima o ano
    #year é o nome da variável que recebe o valor do ano
      