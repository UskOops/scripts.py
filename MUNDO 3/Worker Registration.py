from datetime import datetime as time
datas = {}
datas['name'] = input('Type your NAME: ')
datas['last_name'] = input('Type your LAST NAME: ')
print('-=' * 20)
born = int(input('Type your BORN YEAR: '))
print('-=' * 20)
datas ['age'] = time.now().year - born
datas['ctps'] = int(input('Type your CTPS NUMBER (0 if you do not have): ')) #ctps = carte de trabalho
if datas ['ctps'] != 0:
    datas['hiring'] = int(input('Type the year you were hired: '))
    datas['salary'] = float(input('Type your salary: R$ '))
    datas['retirement'] = datas['age'] + ((datas['hiring'] + 38) - time.now().year)
print('-=' * 30)
for k, v in datas.items():
    print(f' - {k} : {v}')
print('-=' * 30)
print(f' - {datas["name"]} {datas["last_name"]} will retire in {datas["retirement"]} years with {datas["salary"]}R$')
print('-=' * 30)
print('END')

