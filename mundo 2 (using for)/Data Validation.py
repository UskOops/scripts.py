sex = input("Type your sex: [M/F] ").strip().upper()
age = input("Type your age: ")
while sex not in 'MmFf': #pega primeira letras de ambos os sexos
    sex = input('Ivalid data, please, inform your sex: ').strip().upper()
print('sex {} has been registered with sucessul'.format(sex) )