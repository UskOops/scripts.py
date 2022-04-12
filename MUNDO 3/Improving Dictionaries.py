player = {}
team = []
matchs = []

while True:
    player.clear()
    player['name'] = input('Enter player name: ')
    tot = int(input(f'Enter total number of matches the {player["name"]} as played? '))
    matchs.clear()
    for i in range(0, tot):
        matchs.append(int(input(f'Enter the score of match {i+1}: ')))
    player['gols'] = matchs[:]
    player['total'] = sum(matchs)
    team.append(player.copy()) #copia o dicionário para a lista
    while True:
        answer = input('Do you want to continue? [Y/N] ').upper()[0]
        if answer in 'YN':
            break
        print('Invalid answer!')
    if answer == 'N':
        break
print('-=' * 30)# a partir daqui está o resultado
print('cod', end=' ')
for i in player.keys():
    print(f'{i:<15}', end=' ')
print()
print('-=' * 30)
for i, v in enumerate(team): #para interar com a lista usa-se o enumerate
    print(f'{i:>3}', end=' ')
    for d in v.values(): # o D = dado
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)

