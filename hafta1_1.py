
#pow fonksiyonu
def power(a,b):
    if b==0:
           return 1
    elif b==1:
           return a
    else:
            #return a*power(a,b-1)    //sayiyinin kendisiyle sayinin ussunun bir eksigini carparak
           #return power(a*a,b/2)     //sayinin karesini ussun yarisini us alarak carpiyoruz

#recursive pow fonksiyonu
          if b%2==0:
              return power(a*a,b//2)
          else:
              return power(a*a,b//2)*a

print(pow(3,4))   #81



#Listenin max toplamini,baslangic degerini ve bitis degerini bulma
liste_1=[4,-3,5,-2,-1,2,6,-2]
max=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
        if max<t:
            max=t
            i_1,i_2=i,j
print(max,i_1,i_2)   #(11,0,7)

