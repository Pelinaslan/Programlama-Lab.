#listenin alt dizilerinden toplami max olan dizinin degeri?

def my_f_1(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n = len(list_1)
    for i in range(n):
        for j in range(i,n):
            t = 0
            for k in range(i,j):
                t+=list_1[k]
            if t>maxSum:
                maxSum = t
    return maxSum

print(my_f_1([4,-3,5,-2,-1,2,6,-2,4,-3,5,-2,-1,2,6,-2]))   #20


def my_f_2(list_1 = [4,-3,5,-2,-1,2,6,-2]):
    maxSum = 0
    n=len(list_1)
    for i in range(n):
        t = 0
        for j in range(i,n):
            t+=list_1[j]
            if t>maxSum:
                maxSum = t
    return(maxSum)

print(my_f_2())  #11




