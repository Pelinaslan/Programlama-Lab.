import random
#-5 ile 5 arasindaki rakamlardan 10 elemanli bir liste olusturur
def get_n_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers
print(get_n_random_numbers())

#ex./ [-4, -4, 1, 3, -2, -1, -4, -3, 3, -4]


#histogram
def my_frequency_with_dict(list):

    frequency_dict={}  # dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict


#alternatif hist.
def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
print(result_1,result_2)
            #({8: 2, 2: 5, 3: 3, 4: 6, 5: 2}, [[2, 5], [3, 3], [5, 2], [8, 2], [4, 6]])