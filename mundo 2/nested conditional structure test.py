#uma estrutura aninhada é quando uma está dentro da outra

name = input("What is your name? ")
if name == 'Marco':
    print("Hello, Marco!")
elif name =='Alfeu' or name == 'Alfredo' or name =='Joao':
        print('You have a nice name')
elif name in ['Claudio','Lucas','Nicolas']:
    print('You have boy name')
else:
    print('You have a normal name')
print("Beautiful name, " + name + "!") # concatenando strings