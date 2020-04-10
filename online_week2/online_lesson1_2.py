import sympy as sym
from sympy import Symbol
from sympy import pprint
import sympy.plotting as syp
import matplotlib.pyplot as plt

sigma=Symbol('sigma')
x=Symbol('x')
mu=Symbol('mu')
"""
print(2*sym.pi*sigma) #2*pi*sigma
print(sym.sqrt(2*sym.pi*sigma)) #sqrt(2)*sqrt(pi)*sqrt(sigma)
pprint(sym.sqrt(2*sym.pi*sigma)) #yukaridaki sonucu matematiksel ifade halinde basar
#pprint(2*sym.pi*sigma)
"""
part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function=part_1*part_2
pprint(my_gauss_function)

syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distributon')
#fonksiyonun grafigini cizer



x_values=[]
y_values=[]
for value in range(-50,50):
    y=my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)
#(-5, 0.0117355108921433)
#(-4, 0.0119261143055990)
#(-3, 0.0121063544417139)
#(-2, 0.0122756713434441)
#(-1, 0.0124335335602443)
#(0, 0.0125794409230998)
#(1, 0.0127129271820175)
#(2, 0.0128335624865338)
#(3, 0.0129409556907849)
#(4, 0.0130347564658485)

plt.plot(x_values,y_values)
print(plt.show())

