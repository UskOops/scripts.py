n1 = float(input('type your first note: ')) 
n2 = float(input('type your second note: '))
m = (n1 + n2)/2 # media
print('your average is: ', m) # print media
if m >= 6: #se media for maior ou igual a 6
    print('your grade is good')
else: #se media for menor que 6
    print('your grade is bad')