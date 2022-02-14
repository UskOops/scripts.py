from datetime import date
print('You must enlist?')
sexo = str(input('What is your gender? '))
if sexo in 'female woman Female Woman Girl girl ': #in é um operador de comparação
    print('You are not required to enlist in the army..')
    deseja = str(input('Still you want to enlist? '))
    if deseja in 'Yes yes':
        print('Ok, then fill in the form')
    if deseja in 'No no':
        print('Ok, bye!!!')
if sexo in 'Masculine masculine Man Men man men':
    print('Your enlistment is mandatory\nContinue filling out the form') 
else:
    print('Gênero inválido. Tente novamente')
    exit()
i = int(input('What year were you born? '))
ano = date.today().year #date.today() retorna a data atual
dma = ano - i #diferença de anos entre o ano atual e o ano de nascimento
ada = i + 18 #idade mínima para se alistar
qtf = 18 - dma #quantidade de anos para se alistar
qtjf = dma - 18 #idade mínima para se juntar ao exército
if dma < 18:
    print('Its not time to enlist in the army yet, you still have {} years, your enlistment will be in{}: '.format(qtf, ada))
elif dma == 18:
    print('Its time to join the army!')
elif dma > 18 and dma < 22: #dma é a diferença de anos entre o ano atual e o ano de nascimento
    if qtjf == 1:
        print('Its been {} year since your enlistment which was in {}, if you havent enlisted yet, run!'.format(qtjf, ada))
    else:
        print('Its been {} years since your enlistment which was in {}, if you havent enlisted yet, run!'.format(qtjf, ada))
elif dma > 18 and dma > 22: #
    print('Its been {} years since your enlistment in {}, its been a while, if you havent been yet what are you doing with your life???'.format(qtjf, ada))