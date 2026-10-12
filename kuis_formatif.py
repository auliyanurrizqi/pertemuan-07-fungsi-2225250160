
# KUIS FORMATIF: FUNGSI DALAM PYTHON

# 1. Fungsi kata kunci def
print("1. Kata kunci def digunakan untuk mendefinisikan atau membuat fungsi dalam Python.")
print()

# 2. Perbedaan parameter dan argumen
def tambah(a, b):
    return a + b

print("2. Parameter adalah variabel dalam definisi fungsi,")
print("   sedangkan argumen adalah nilai yang diberikan saat fungsi dipanggil.")
print("   Contoh tambah(3, 5) =", tambah(3, 5))
print()

# 3. Perbedaan return dan print
print("3. return digunakan untuk mengembalikan nilai dari fungsi,")
print("   sedangkan print digunakan untuk menampilkan informasi ke layar.")
print()

# 4. Nilai variabel x pada fungsi kuadrat
def kuadrat(x):
    return x * x

x = kuadrat(4)
print("4. Nilai x =", x)
print()

# 5. Variabel lokal
print("5. Variabel lokal membatasi penggunaan data dalam fungsi,")
print("   mengurangi risiko perubahan yang tidak diinginkan,")
print("   serta memudahkan pengujian dan perbaikan program.")
print()

# 6. Fungsi dengan argumen yang kurang
print("6. Jika fungsi membutuhkan dua argumen tetapi hanya diberi satu,")
print("   Python menghasilkan TypeError.")

# Contoh kesalahan (tidak dijalankan):
# print(tambah(5))
print()

# 7. Menggunakan return dalam perhitungan lain
hasil = kuadrat(3) + kuadrat(4)
print("7. Hasil kuadrat(3) + kuadrat(4) =", hasil)
print()

# 8. Perbedaan Step Into dan Step Over
print("8. Step Into digunakan untuk masuk ke dalam fungsi saat debugging.")
print("   Step Over menjalankan satu baris tanpa menelusuri isi fungsi.")
print()

# 9. Manfaat modularisasi
print("9. Modularisasi memudahkan pengujian fungsi secara terpisah,")
print("   sehingga kesalahan lebih mudah ditemukan dan diperbaiki.")
print()

# 10. Perintah Git untuk mengirim commit ke GitHub
print("10. Perintah Git untuk mengirim commit lokal ke GitHub adalah:")
print("    git push")
