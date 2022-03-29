expr = input('Type a math expression: ')
pile = []
for simb in expr: #simb = simbolos
    if simb == '(' :
        pile.append('(')
    elif simb == (')'):
        if len(pile) > 0:
            pile.pop() # Remove o último elemento da pilha
        else:
            pile.append(')')
            break
if len(pile) == 0:
    print('Expression is valid')
else:
    print('Expression is not valid')
