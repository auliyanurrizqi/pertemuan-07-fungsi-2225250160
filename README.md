
# Pertemuan 07 — Fungsi Python

## Identitas Mahasiswa
- Nama: Aulia Nurrizqi
- NIM: 2225250160
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman
- Program Studi: Pendidikan Matematika
- Fakultas: FKIP
- Universitas: Universitas Sultan Ageng Tirtayasa

## Deskripsi
Proyek ini dibuat untuk memenuhi latihan dan Praktik 2 pada
Pertemuan 07 mata kuliah Algoritma dan Pemrograman.

Materi yang dipelajari meliputi fungsi, parameter, argumen,
return value, scope variabel, perulangan, seleksi, dan
pengujian program menggunakan Python.

## Tujuan
1. Memahami cara mendefinisikan dan memanggil fungsi.
2. Menggunakan parameter dan argumen dengan tepat.
3. Memahami perbedaan print dan return.
4. Memahami local scope dan global scope.
5. Membuat program matematika sederhana secara modular.
6. Menguji program menggunakan beberapa test case.

## Struktur Folder

```text
pertemuan-07-fungsi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py
```

## Daftar Latihan

### 1. Fungsi Salam
Membuat fungsi salam dengan parameter nama dan kelas.

### 2. Luas Persegi Panjang
Menghitung luas persegi panjang menggunakan fungsi
dan return value.

### 3. Jumlah Bilangan 1 sampai n
Menghitung jumlah bilangan menggunakan perulangan for.

### 4. Statistik Sederhana
Menghitung nilai minimum, maksimum, dan rata-rata data.

### 5. Eksperimen Scope
Memahami perbedaan variabel lokal dan global.

## Praktik 2: Utilitas Matematika

Program berbasis menu yang menyediakan fitur:
1. Menghitung luas persegi panjang.
2. Menghitung luas segitiga.
3. Menghitung jumlah bilangan 1 sampai n.
4. Menghitung faktorial.
5. Keluar dari program.

Program menggunakan fungsi, parameter, return value,
perulangan, seleksi, dan validasi input.

## Cara Menjalankan

Pastikan Python 3 sudah terpasang di komputer.

Jalankan latihan melalui terminal VS Code:

```bash
python latihan/01_salam.py
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
```

Jalankan program Praktik 2:

```bash
python praktik/utilitas_matematika.py
```

Pada Windows, perintah `py` dapat digunakan jika
perintah `python` tidak tersedia.

## Hasil Pengujian Praktik 2

| Operasi | Input | Hasil yang Diharapkan |
|---|---|---:|
| Luas persegi panjang | p = 8, l = 5 | 40 |
| Luas segitiga | a = 10, t = 6 | 30.0 |
| Jumlah 1 sampai n | n = 10 | 55 |
| Faktorial | n = 5 | 120 |
| Faktorial | n = 0 | 1 |

Status pengujian: sesuai apabila hasil aktual sama
dengan hasil yang diharapkan.

## Kesimpulan
Melalui latihan dan Praktik 2, fungsi membantu program
menjadi lebih terstruktur, mudah dibaca, dan dapat
digunakan kembali. Parameter digunakan untuk menerima
data, sedangkan return mengembalikan hasil perhitungan.
Scope membantu membatasi penggunaan variabel sesuai
dengan tempat variabel tersebut didefinisikan.

## Referensi
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 07.
- Python Software Foundation. Python 3 Documentation:
  Defining Functions.
  https://docs.python.org/3/tutorial/controlflow.html#defining-functions

## Catatan
Kode dan hasil pengujian perlu diperiksa kembali sebelum
dikumpulkan. Sesuaikan identitas mahasiswa dan dokumentasi
dengan hasil pengerjaan yang sebenarnya.
