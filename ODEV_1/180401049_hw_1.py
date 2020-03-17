kelimeler =[]
input_list =[]
histogram_list =[]

""" dosyayi okur"""
def readFile(kelimeler):
     dosya = open("1.txt", "r")
     for i in dosya:
         for j in i.split():
             kelimeler.append(j.lower())


"""histogram fonk"""
def my_h(list_1):
    dict_1=dict()
    for i in list_1:
        if i in dict_1:
            dict_1[i]+=1
        else:
            dict_1[i]=1
    return dict_1


"""histogramdaki max degeri bulur(frekansi en yuksek)"""
def max_histogram(dict_1):
    max ,key= 0,""
    for i in dict_1:
        if dict_1[i]>max:
            key = i
            max = dict_1[i]
    return key

 #klavyeden max 5 deger alip dosyaya yazacak
def writeInput():
    file = open("input.txt", "w")
    while (1):
        inp = input("Aranacak ifadeyi Giriniz: ")
        if (inp == "-1"):
            break
        while len(inp.split()) > 5:
            print("5den fazla kelime giremezsiniz!")
            inp = input("Aranacak ifadeyi Giriniz: ")
        file.write(inp)
        file.write("\n")
    file.close()

#onerilecek kelimeleri diziye aktarir
def read_input_file():
    i_file = open("input.txt")
    i_file = i_file.readlines()
    for i in i_file:
        if(i!="\n"):
            i=i.replace("\n","")
            input_list.append(i)

def writeOutput(maxKelimeler):
    dosya = open("output.txt", "w")
    uzunluk = len(maxKelimeler)
    i = 0
    while i < uzunluk:
        dosya.write(maxKelimeler[i])
        dosya.write("\n")
        i = i + 1
    dosya.close()

def split_mtd(i,j):
    list_1 = j.split(i)
    for k in range(1,len(list_1)):
        list_2=list_1[k].split()
        if(len(list_2)>0):
            list_2[0] = list_2[0].replace(",","")
            histogram_list.append(list_2[0])

def process(i):
    histogram_list.clear()
    i=i.lower()
    for j in kelimeler:
        j=j.lower()
        if i in j:
            split_mtd(i,j)

def start():
    print("--1 bitirir")
    writeInput()
    readFile()
    read_input_file()
    for i in input_list:
        if(len(i.split())<=5):
            process(" "+i)
            print(i+"+"+max_histogram(my_h(histogram_list)))
        else:
            print(i+" "+"5 ten buyuk")
start()




