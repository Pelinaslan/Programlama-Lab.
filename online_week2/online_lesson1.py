from sympy import Symbol
from sympy import factor
from sympy import expand
from sympy import pprint
x=Symbol('x')
y=Symbol('y')

p=x*(x+x)
print(p)  #2*x**2

p=(x+2)*(x+3)
print(p) #(x + 2)*(x + 3)

expr=x**2 -y**2
print(factor(expr))  #(x - y)*(x + y)  #carpanlara ayirma

factors=factor(expr)
print(expand(factors)) #x**2 - y**2   #carpanlara ayrilan ifadeyi sadelestir

expr=x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors=factor(expr)
print(factors) #(x + y)**3
pprint(factors)  #carpanlara ayirma islemini uslu ifade seklinde yapar


x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)

expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})  #x'i 1 le y'yi 2 yle degistir
print(res) #9     #1*1+ 1*2+ 1*2+ 2*2=9

r=expr.subs({x:1-y})  #x yerine 1-y yazdik
print(r)   #y**2 + 2*y*(1 - y) + (1 - y)**2

x = Symbol('x')
series = x
n=50
x_value=10
for i in range(2, n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print(series_value)   #68680/3


