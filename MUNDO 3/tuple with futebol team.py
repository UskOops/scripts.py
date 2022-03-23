team = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-=' * 15)
for t in team:
    print(f'{t}')
print('-=' * 15)
print(f'The first 5 team is {team[0:5]}')
print('-=' * 15)
print(f'The last 5 team is {team[-4:]}')
print('-=' * 15)
print(f'The Cruzeiro in such {team.index("Cruzeiro")+1} position ')
print('-=' * 15)
print(f'teams sorted in alphabetical order {sorted(team)}') #sorted organiza a lista em ordem alfabética
print('-=' * 15)
