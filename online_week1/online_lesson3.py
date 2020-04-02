import random

def get_n_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers
get_n_random_numbers()


def my_lineer_search(my_list,item_search):
    found=(-1,-1)  #listede yoksa
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)  #listede bulundu

    return found

my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
#my_list=get_n_random_numbers(10,-1,8)
print("liste",my_list)      #('liste', [2, 3, 2, 5, 8, 2, 4, 3, 3, 2, 8, 5, 2, 4, 4, 4, 4, 4])
print(my_lineer_search(my_list,2)) #(2, 12)




##listenin aritmetik ort. bulma##
def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s+=1
        t+=item
    mean_=t/s
    return mean_

print("aritmetik ort.",my_mean(my_list))  #('aritmetik ort.', 3)


##listeyi siralama##
def bubble_sort(my_list):
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp

    return my_list
print("sirali liste",bubble_sort(my_list))  #('sirali liste', [2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 8, 8])




####
def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1

    while low <=high:
        mid=(low+high) //2

        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high=mid-1
        else:
            low=mid+1

    return found


my_list_2=bubble_sort(my_list)
#print("sirali liste",my_list_2)
print(my_binary_search(my_list_2,3))   #(3, 5)

##medyan bulma##
##Medyan, bir sayisal veri serisi siralandiginda ortada kalan sayidir.##
  
def my_median(my_list):
    my_list_2 = bubble_sort(my_list)
    #print(my_list_2)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle]


    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2


    return median

print("medyan",my_median(my_list))   #('medyan', 4)
