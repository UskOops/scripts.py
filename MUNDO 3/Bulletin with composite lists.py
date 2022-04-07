from numpy import average


token = []
while True:
    name = str(input("Enter NAME: "))
    result1 = float(input("Enter result 1: "))
    result2 = float(input("Enter result 2: "))
    average = (result1 + result2) / 2
    token.append([name, [result1, result2], average])
    answer = str(input("Do you want to continue? (Y/N): "))
    if answer in "Nn":
        break
print("-" * 40)
print("{:<10}{:<8.5}{:<8.5}{:<10}".format("NAME", "RESULT 1", "RESULT 2", "AVERAGE"))
print("-" * 40)
for i, a in enumerate(token): # i = indice, a = aluno
    print("{:<10}{:<10}{:<10}{:<10}".format(a[0], a[1][0], a[1][1], a[2]))