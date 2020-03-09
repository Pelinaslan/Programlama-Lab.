
#listede bulunan elemanlarin kacar tane oldugunu bulan fonksiyon
def my_h(list_1):
    my_d={}
    for item in list_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=item+1
    return my_d
print(my_h([2,3,4,6,2,5,6,6,6,6,6,6,6,2]))

#{2: 3, 3: 1, 4: 1, 5: 1, 6: 7}



#girilen degerin sozlukte neyin karsiligi oldugunu cikti verir
#karsiligi yoksa -1 dondurur

def lookup(d,V):
    for key in d:
        if d[key]==V:
            return key
    return -1

my_d =dict()

my_d ={1:3,2:5,6:8}

print(lookup(my_d,5))

#2

#recurcive olarak n. fib. sayisini bulur
known={0:0,1:1}
def fibo_rec(n):
  # if n<2:
       #return n
   #else:
        #return fibo_rec(n-1)+fibo_rec(n-2)
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        #print(known)
        return result
print(fibo_rec(10))