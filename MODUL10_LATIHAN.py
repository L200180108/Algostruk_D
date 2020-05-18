##import time
###menjumlahkan bilangan 1 sampai n
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range (1,n+1):
##        hasilnya += i
##    return hasilnya
##
##def jumlahkan_cara_2(n):
##    return (n*(n+1))/2
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_2(1000000)
##    akhir = time.time()
##    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h,akhir-awal))




##import time
##import random
##
##def insertionsort(a):
##    for i in range(1,len(a)):
##        nilai = a[i]
##        b = i
##        while b >0 and nilai<a[b - 1]:
##            a[b]=a[b-1]
##            b -=1
##        a[b]=nilai
##
##print("Average Case")    
##for i in range (5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##
##print("Worst Case") 
##for i in range (5):
##    L = list(range(3000))
##    L = L[::-1]
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##    
##print("Best Case") 
##for i in range (5):
##    L = list(range(3000))
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L),akhir-awal))
##
##
import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range (n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        ##print('i = ',i)
        t=timeit.timeit("kalangBersusuh(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

n=1000
LS=ujiKalangBersusuh(n)

plt.plot(LS)
skala=7700000
plt.plot([x*x/skala for x in range (1,n+1)])
plt.show()

















