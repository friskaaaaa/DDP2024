# Soal No 1
# 1. Buat variabel list dengan value. [NamaKendaraan, JenisKendaraan, ccKendaraan, WarnaKendaraan, RodaKendaraan]
kendaraan = ['Honda Beat', 'Sepeda Motor', 120, 'Merah', 2]
print("Kendaraan Saya")
print(kendaraan)
print("========")
# Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
# kendaraan.append(20000000)
# kendaraan.append("Metic")
kendaraan.extend([20000000, "Metic"])
print(kendaraan)
print("========")
# tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert(2, 'Honda')
print(kendaraan)
print("========")

# Soal No 2

# Buat program phyton dengan match case untuk menghitung luas bangun datar :
# Jika pilih 1, maka menghitung luas persegi
# Jika pilih 2, maka menghitung luas lingkaran
# Jika pilih 3, maka menghitung luas segitiga
# Kalau pilihannya tidak ada makan ada keterangan : salah pilih

print('Ini adalah program sederhana untuk menghitung luas bangun datar')
print("Pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
PilihMenu = int(input("Silahkan pilih menu dengan mengetikan angka 1-3 :"))

match PilihMenu:
    case 1 :
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yang mau dihitung"))
        hitung = sisi * sisi
        print(f"Luas persegi adalah : {hitung}")
    case 2 :
        print("Luas lingkaran = phi*r*r")
        r= int(input("Masukkan Angka Anda "))
        phi= 3.14
        luas= phi*r*r
        print(int(luas))
    case 3 :
        print('Ini adalah operasi luas segitiga')
        alas= int(input('Masukkan alas:'))
        tinggi= int(input('Masukkan tinggi:'))

        luas_segitiga= int(1/2*alas*tinggi)
        print(f'Luas Segitiga = 1/2 *', alas, '*', tinggi, '=', luas_segitiga)
    case _:
        print("Pilihan tidak valid, silahkan pilih antara 1-3")