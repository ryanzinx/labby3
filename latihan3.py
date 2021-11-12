print("PROGRAM KEDUA BILANGAN TERBESAR DAN TERKECIL")

nilai1 = int(input("Masukkan angka : "))
nilai2 = int(input("Masukkan Angka : "))

if nilai1 > nilai2:
    terbesar = nilai1
else:
    terbesar = nilai2
print("Nilai terbesar dari " + str(nilai1) + " " + str(nilai2) + " adalah " + str(terbesar))
