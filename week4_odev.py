#Pelin ASLAN 180401049



#i parametresinin sagi ve solunu kontrol edip koşul saglanmadigi durumda yer degistirir
#recursive olarak devam eder
def min_heapify(array, i):
    """"
    array:Heap listesi
    i:heapify in uygulanmaya baslayacagi index
    """
    left= 2*i+1
    right= 2*i+2
    length= len(array)-1
    smallest = i
    if left  <=length and array[i] > array[left]:
        smallest= left
    if right <=length and array[smallest]> array[right]:
        smallest=right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array,smallest)


#sondan baslayarak liste minheap hale gelene kadar tüm elemanlara min_heapify fonksiyonunu uygular
def build_min_heap(array):
    """
    array:Heap listesi
    """
    for i in reversed(range(len(array)//2)):
        min_heapify(array,i)


#bir heap listesini kucukten buyuge siralar
def heapsort(array):
    """
    array:Siralanacak liste
    """
    array=array.copy()
    build_min_heap(array) #listeyi heap yapisi haline getirir
    sorted_array=[]

    for _ in range(len(array)):
        array[0],array[-1]=array[-1],array[0] #dizinin basi ile sonunu degistirdi
        sorted_array.append(array.pop()) #sondaki sayiyi listeden siler ve sirali listeye ekler
        min_heapify(array,0) #listeyi tekrar min heap haline getirir
    return sorted_array



#####

def insertItemToHeap(myheap_1,item):
    """
    myheap_1: Heap listesi
    item: listeye eknenecek sayi
    """
    myheap_1.append(item) #heap'e eleman ekler
    build_min_heap(myheap_1) #eleman ekledikten sonra bozulan heap yapisini tekrar minheap yapar


def removeItemFrom(myheap_1):
    """
    myheap_1: Heap listesi

    """
    if(len(myheap_1)==0):
        return 0
    myheap_1[0],myheap_1[-1]=myheap_1[-1],myheap_1[0] #dizinin basi ile sonunu degistirdi
    myheap_1.pop() #sondaki elemani sildi(en kucuk eleman)
    build_min_heap(myheap_1) #eleman sildikten sonra olusan listeyi tekrar heap yapisina cevirdi

#####
my_array_1=[8,10,3,4,7,15,1,2,16]
my_array_2=[8,10,3,4,7,15,1,2,16]

build_min_heap(my_array_1)
print(my_array_1) #[1, 2, 3, 4, 7, 15, 8, 10, 16]

my_sorted_array=heapsort(my_array_2)
print(my_array_2,my_sorted_array) #[8, 10, 3, 4, 7, 15, 1, 2, 16] [1, 2, 3, 4, 7, 8, 10, 15, 16]


insertItemToHeap(my_array_2,19)
print(my_array_2) #[1, 2, 3, 4, 7, 15, 8, 10, 16, 19]
removeItemFrom(my_array_2)
print(my_array_2) #[2, 4, 3, 10, 7, 15, 8, 19, 16]

