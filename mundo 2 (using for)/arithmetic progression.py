first = int(input("Type the first number: "))
reason = int(input("reason: "))
tenth = first + (10 - 1) * reason #formula do N-ésimo termo de uma PA
for c in range(first,tenth+reason,reason):
  print('{}'.format(c), end=' → ') #saida
