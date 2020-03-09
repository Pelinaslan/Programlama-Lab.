from sympy import FiniteSet


#olasilik hesabi

def probability(space,event):
    return len(event)/len(space)

#asal mi kontrol fonksiyonu
def check_prime(number):
    if number !=1:
        for factor in range(2, number):
            if number%factor ==0:
                return False


    else:
        return False


    return True


space =FiniteSet(*range(1,21))
primes=[]
for num in space:
    if check_prime(num):
        primes.append(num)


    event =FiniteSet(*primes)
    p=probability(space,event)
    print(p)
