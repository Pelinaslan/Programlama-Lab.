from sympy import Symbol, Limit

t=Symbol('t')
t1=Symbol('t1')
delta_t=Symbol('delta_t')

St= 5*t**2 + 2*t +8
St1=St.subs({t:t1})
#print(St1) #5*t1**2 + 2*t1 + 8

St1_delta=St.subs({t:t1 + delta_t})
#print(St1_delta) #2*delta_t + 2*t1 + 5*(delta_t + t1)**2 + 8

#delta_t ye gore turev aliyoruz
print(Limit((St1_delta-St1)/delta_t,delta_t,0).doit()) #10*t1 + 2
