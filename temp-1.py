print("Hello AI Era")

type(9)

type(9.2)

# STRINGLER

12
type(12)

"12"
type("12")

"a" + "b"
"a" " b"
"a" "-b"


gel_yaz = "gelecegi_yazanlar"
len(gel_yaz)


# DEGISKENLER

a = 5
b = "ali_uzaya_git"
c = a*9

a/c
a*b

# TYPE_DONUSUMLERI

birinci_sayi = input()

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)

int(11.0)

12

float(12)

str(12)

type(str(12))


# PRINT

print("gelecegi", "yazanlar", sep="_")


#VERI YAPILARI

#LISTE

notlar = [90, 80, 70, 50]


#append

liste = ["ali", "veli", "isik"]

liste

liste.append("berkcan")
liste

liste.remove("berkcan")
liste


#insert

liste = ["ali", "veli", "isik"]
liste
liste.insert(0, "ayse")
liste



#TUPLE

t = ("ali", "veli", 1, 2, 3.2, [1, 2, 3, 4])


#SET

m = [1, "a", "ali", 123]
m


s = set(m)
s


#FONKSIYON
#MATEMATIKSEL ISLEMLER
4*4
4/4
5-1
6+3
3**2


#FONKSIYON NASIL YAZILIR?
#Fonksiyon girdiğimizi belirtmek için def yazarız ve bu devamında gelen şeyin bir fonksiyon olduğunu belirtir.

def kare_al(x):
  print(x**2)

kare_al(3)



def kare_al(x):
  print("Girilen sayinin karesi:" + str(x**2))

kare_al(3)


def kare_al(x):
  print("Girilen sayi:" + str(x) + ", Karesi:" + str(x**2))

kare_al(3)


#IKI ARGUMANLI FONKSIYON TANIMLAMAK

def carpma_yap(x, y):
  print(x*y)

carpma_yap(2, 3)


#On Tanımlı Argumanlar

def carpma_yap(x, y=1):
  print(x*y)
carpma_yap(3)


#Argumanlarin Siralanmasi
def carpma_yap(x, y=1):
  print(x*y)
carpma_yap(y = 2, x = 3)


#Ne Zaman Fonksiyon Yazilir?

#sokaklambasi
#isi, nem, sarj

def direk_hesap(isi, nem, sarj):
  print((isi + nem)/sarj)

direk_hesap(25,40,70)


#Fonksiyonlarin ciktilarinin üzerine bir işlem uygulayamayız. Print ile ekrana basılan şey sadece değerin gösterilmesidir. Üzerine bir işlem yapılamazç

#Return fonksiyonu ile ciktiyi girdi olarak yazip uzerinde islem yapabiliriz.

def direk_hesap(isi, nem, sarj):
  return (isi + nem)/sarj

direk_hesap(25,40,70)*9


#Local ve Global Degiskenler

#Global Degisken

x = 10
y = 20


#Local Degisken

x = 10
y = 20

def carpma_yap(x, y):
  return x*y

carpma_yap(2,3)

#Local Etki Alanindan Global Etki Alanini Degistirmek

x = []

def eleman_ekle(y):
  x.append(y)
  print(str(y) + " ifadesi eklendi")

eleman_ekle("ali")

eleman_ekle("veli")

x


#True-False Sorgulamalari

sinir = 5000

sinir == 4000

sinir == 5000

5 == 4

5 == 5


#If

sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
  print("Gelir sinirdan kucuk")
  
  
#Else
sinir = 50000
gelir = 35000

if gelir < sinir:
  print("Gelir sinirdan kucuk")

else:
  print("Gelir sinirdan buyuk")



#Diger ornek

sinir = 50000
gelir = 50000

if gelir == sinir:
  print("Gelir sinira esittir")

else:
  print("Gelir sinirdan buyuk")
  
  
  #Elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
  print("Tebrikler, hediye kazandiniz. ")
elif gelir1 < sinir:
  print("Uyari!")
else:
  print("Takibe devam")
  
  
#ornek uygulama

sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
  print("Tebrikler: " + magaza_adi + " promosyon kazandiniz!")
elif gelir < sinir:
  print("Uyari! Cok dusuk gelir: " + str(gelir))
else:
  print("Takibe devam")
  

#Donguler - FOR

ogrenci = ['ali', 'veli', 'isik', 'berk']

for i in ogrenci:
  print(i)
  
print(ogrenci[0])



maaslar = [1000, 2000, 3000, 4000, 5000]

for i in maaslar:
  print(i)
  
  
 #maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz

 maaslar[0]*20/100 + maaslar[0]

 #fonksiyon yazmak

def yeni_maas(x):
   print(x)


def yeni_maas(x):
  print(x*20/100 + x)

for i in maaslar:
  yeni_maas(i)
  
  
#ornek uygulama 2

maaslar = [1000, 2000, 3000, 4000, 5000]

def maas_ust(x):
   print(x*10/100 + x)

def maas_alt(x):
  print(x*20/100 + x)

for i in maaslar:
  if i >= 3000:
    maas_ust(i)

  else: 
    maas_alt(i)
    
    
#ornek uygulama myself

notlar = [65, 90, 82, 76]
notlar.sort()
def yuksek_not(x):
  print(x + 5)

def dusuk_not(x):
  print(x + 10)

for i in notlar:
  if i >= 80:
    yuksek_not(i)

  else:
    dusuk_not(i)



#BREAK AND CONTINUE

maaslar = [5000, 2000, 1000, 3000, 6000]

maaslar.sort()

for i in maaslar:
  if i == 3000:
    print("Kesildi")
    break
  print(i)
  
maaslar = [5000, 2000, 1000, 3000, 6000]

maaslar.sort()

for i in maaslar:
  if i == 3000:
    print("keep going")
    continue
  print(i)
  
  
#WHILE

sayi = 1

while sayi < 10:
  sayi += 1
  print(sayi)
  
  
  

















