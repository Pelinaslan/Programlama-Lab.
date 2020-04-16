from sympy import Symbol
from sympy import pprint
#import sympy.plotting as syp
import matplotlib.pyplot as plt
from sympy import factorial

#degiskenleri sembole donusturduk
n=Symbol('n') #deneme sayisi
x=Symbol('x') #istenilen basari sayisi
p=Symbol('p') #bir denemede basari elde etme olasiligi
q=Symbol('q') #bir denemede basarisiz olma olasiligi  #q=1-p

part_1=factorial(n)/(factorial(n-x)*factorial(x))
part_2=(p**x)*(q**(n-x))
fonksiyon=part_1*part_2
#pprint(fonksiyon)

Binomial_Distribution_func=fonksiyon.subs({q:1-p})
pprint(Binomial_Distribution_func)

#syp.plot(Binomial_Distribution_func.subs({n:10,p:0.5}),(x,0,10),title='Binomial distribution')

x_values=[]
y_values=[]
for value in range(0,11):
    y=Binomial_Distribution_func.subs({n:10,p:0.5,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)
plt.plot(x_values,y_values)
print(plt.show())


