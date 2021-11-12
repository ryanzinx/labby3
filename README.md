# labby3
# Program latihan 1
jumlah =int(input("masukkan jumlah n :"))
import random
for i in range (jumlah) :
    print("data ke", i+1,"=",(random.uniform(0.1,0.5)))

# Program latihan 2
max = 0
while True:
    a=int(input("masukan bilangan :"))
    if max < a:
        max = a
    if a ==0:
        break
print ("\n bilangan terbesar adalah :", max)

# Program latihan 3
print("PROGRAM KEDUA BILANGAN TERBESAR DAN TERKECIL")

nilai1 = int(input("Masukkan angka : "))
nilai2 = int(input("Masukkan Angka : "))

if nilai1 > nilai2:
    terbesar = nilai1
else:
    terbesar = nilai2
print("Nilai terbesar dari " + str(nilai1) + " " + str(nilai2) + " adalah " + str(terbesar))

