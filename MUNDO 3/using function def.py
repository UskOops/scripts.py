def sum(*values):
    s = 0
    for num in values: #desempacotar valores
        s += num
    print(f'Calculate the sum of {values} we have {s}')
# main program
sum(10,20)
sum(30,40)
sum(50,60)
sum(70,80)
sum(90,100, 110, 120)

#def double(list): #passando parametro como lista
#    pos = 0
#    while pos < len(list):
#        list[pos] *= 2 #lista recebe o valor do elemento da lista vezes 2
#        pos += 1
#values = [1,2,3,4,5] #essa lista terá seus valores multiplicados por 2
#double(values)
#print(values)

