state = {}
brasil = []
for c in range(0, 3):
    state['UF'] = (input('Federative unit: '))
    state['acronym'] = (input('state acronym: '))
    brasil.append(state.copy()) #copy() copia o dicionario
for e in brasil:
    for k, v in e.items(): # retorna todos os valores do dicionario
        print(f'The field {k} have a value {v}') #k = dicionario key, v = dicionario value