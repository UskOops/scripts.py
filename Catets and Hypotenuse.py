#maneira padrão sem usar import
#catop = float(input("Size the catet oposite: "))
#catadj = float(input("Size the catet adjacent: "))
#hyp = (catop**2 + catadj**2)**0.5
#print(f'The hypotenuse is {hyp:.2f}')

#usando import metodo math
#from math import hypot = se eu ussase esse metodo, poderia não precisaria usar o math.hypot, bastaria usar o hypot
import math
catop = float(input("Size the catet oposite: "))
catadj = float(input("Size the catet adjacent: "))
hyp = math.hypot(catop, catadj) #hypotenuse = hypot
print(f'The hypotenuse is {hyp:.2f}')