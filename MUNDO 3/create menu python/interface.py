def row(size=40):
    return '-' * size

def header(txt):
    print(row())
    print(txt.center(40))
    print(row())

def menu(list):
    header('MENU PRINCIPAL')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    print(row())