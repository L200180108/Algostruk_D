def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
K = [50, 20, 70, 10]
#swap(K, 1, 3)
#print (K)

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini + 1, sampaiSini):
        if A[i] < A [posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil
A = [18,13,44,25,66,107,78,89]
##j = cariPosisiYangTerkecil(A,2,len(A))
##print(j)

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
##bubbleSort(A)
##print(A)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)
##selectionSort(K)
##print(K)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos >0 and nilai <A [pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
Z =[5, 7, 9, 6, 2, 1, 3, 10, 4, 8]
##insertionSort(Z)
##print(Z)
