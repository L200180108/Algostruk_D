if target in arraytempatYangDicari:
    print("Targetnya terdapat di array itu.")
else :
    print("Targetnya tidak terdapat di array itu.")

##LATIHAN 1##
    
def cariLurus(wadah,target):
    n = len(wadah)
    for i in range(n):
        if wadah [i] == target:
            return True
    return False

##LATIHAN 2##
class Mahasiswa():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.NIM = nim
        self.kotaTinggal = kota
        self.uangSaku = us
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python isn't cool.")
        
import mhs as py
c0 = py.MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = py.MhsTIF('Budi',51,'Sragen',230000)
c2 = py.MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = py.MhsTIF('Chandra',18,'Surakarta',235000)
c4 = py.MhsTIF('Eka',4,'Boyolali',240000)
c5 = py.MhsTIF('Fandi',31,'Salatiga',250000)
c6 = py.MhsTIF('Deni',13,'Klaten',245000)
c7 = py.MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = py.MhsTIF('Janto',23,'Klaten',245000)
c9 = py.MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = py.MhsTIF('Khalid',29,'Purwodadi',265000)
##
##lalu membuat daftar mahasiswa dalam bentuk list
##
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di ' + target)

##LATIHAN 3##
def cariTerkecil(kumpulan):
    n = len(kumpulan)
    #anggap item pertama adalah yang terkecil
    terkecil = kumpulan[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if kumpulan [i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil  #kembalikan yang terkecil

##Bagaimana programnya jika kita ingin mencari mahasiswa(dari class MhsTIF di atas) yang uang sakunya terkecil?
def usKecil(Daftar):
    minim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < minim:
            minim = i.uangSaku
            if i.uangSaku == minim:
                nama = i.nama
    return nama, minim
print(usKecil(Daftar))

##Bagaimana kalau yang terbesar?
def usBesar(Daftar):
    maxim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > maxim:
            maxim = i.uangSaku
            if i.uangSaku == maxim:
                nama = i.nama
    return nama, maxim
print(usBesar(Daftar))

##Bagaimanakah programnya jika kita ingin mencari semua mahasiswa yang uang sakunya kurang dari 250ribu?
def usKurang(Daftar):
    a=[]
    for i in Daftar:
        if i.uangSaku < 250000:
            a.append(i.nama)
    return a
print(usKurang(Daftar))

##Bagaimana kalau lebih?
def usLebih(Daftar):
    a = []
    for i in Daftar:
        if i.uangSaku >= 250000:
            a.append(i.nama)
    return a
print(usLebih(Daftar))

#LATIHAN 4##
def binSe(kumpulan,target):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1
    #secara berulang belah runtutan itu menjadi separuhnya sampai target ditemukan
    while low <= high:
        #temukan pertengahan runtut itu
        mid = (high + low)//2
        #apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return True
        #ataukah targetnya disebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        #ataukan disebelah kanannya?
        else :
            low = mid + 1
        #jika runtutannya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(list,target))
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(list,target))

##Dapatkah kamu mengubah programnya agar dia mengembalikan index-nya kalau targetnya ditemukan,
##dan mengembalikan False kalau target tidak ditemukan

def binSe(list, target):
    a=[]
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            a.append(list.index(target))
            i=list.index(target)-1
            j = list.index(target) + 1
            while target == list[i]:
                a.append(i)
                i-=1
            while target == list[j]:
                a.append(j)
                j+=1
            return a
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False

list = [2,3,3,3,4,4,4,4,4,5,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(list,target))
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(list,target))


