from sympy import Symbol,exp,sqrt,pi,Integral

x=Symbol('x')

p=exp(-(x-10)**2/2)/sqrt(2*pi)

#p fonksiyonunun x'e göre integralini aldık
print(Integral(p,(x,11,12)).doit().evalf()) #0.135905121983278



