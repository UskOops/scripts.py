#lista onde passa as inf das pessoas
list_name = []
list_name_man = []
list_age = []
list_sex = []
list_age_man = []
list_age_woman = []

for c in range (1,5):
    print('-------------- {}ª person ----------------'.format(c)) #imprime a lista de nomes dentro do for
    name = str(input('Type the NAME: ')).strip().upper() #strip remove os espaços em branco e upper converte para maiusculo
    list_name.append(name) #append adiciona o nome na lista

    age = int(input('Type the AGE: '))
    list_age.append(age)

    sex = str(input('Type the SEX M/F: ')).strip().upper()
    list_sex.append(sex)

    if sex == 'M': 
        list_name_man.append(name)
        list_age_man.append(age)
    if sex == 'F' and age < 20:
        list_age_woman.append(age)

print('The mean age of the group is  {}'.format(sum(list_age)/len(list_age)))
print('Name of the most old man: {}'.format(list_name_man[list_age_man.index(max(list_age_man))]))
print('Total of womans with less 20 years old: {}'.format(len(list_age_woman)))