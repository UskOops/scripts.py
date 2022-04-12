player = {}
team = []
matchs = []

while True:
    player.clear()
    player['name'] = input('Enter player name: ')
    tot = int(input(f'Enter total number of matches the {player["name"]} as played? '))
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
print('-=' * 30)
for i, v in enumerate(team): #para interar com a lista usa-se o enumerate
    print(f'Player {i+1}')
    for k, v in v.items():
        print(f'{k} => {v}')



print('-=' * 30)
print(f'The player {player["name"]} as played, {len(player["gols"])} matches')
print('-=' * 30)
print(f'The player {player["name"]} has scored, {player["total"]} goals')
for i, v in enumerate(player['gols']): #para interar com a lista usa-se o enumerate
    print(f'Match {i+1} => {v}')
print('-=' * 30)
while player == {}:
    print('The player has not played any match')
    break
print(f'The player {player["name"]} has scored, {player["gols"][0]} goals in the first match')
print('------END OF PROGRAM------')

