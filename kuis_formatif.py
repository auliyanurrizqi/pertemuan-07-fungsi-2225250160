
# KUIS FORMATIF PERTEMUAN 07
# Materi: Fungsi, Parameter, Return Value, dan Scope Python

soal = [
    {
        "pertanyaan": "1. Apa fungsi kata kunci def dalam Python?",
        "pilihan": [
            "A. Menghapus variabel",
            "B. Mendefinisikan fungsi",
            "C. Mengulang program",
            "D. Menampilkan gambar"
        ],
        "jawaban": "B",
        "pembahasan": "def digunakan untuk mendefinisikan atau membuat fungsi."
    },
    {
        "pertanyaan": "2. Apa perbedaan parameter dan argumen?",
        "pilihan": [
            "A. Parameter adalah nilai, argumen adalah nama fungsi",
            "B. Keduanya selalu sama",
            "C. Parameter menerima data, argumen adalah nilai yang dikirim",
            "D. Parameter hanya digunakan untuk print"
        ],
        "jawaban": "C",
        "pembahasan": "Parameter ditulis dalam definisi fungsi, sedangkan argumen diberikan saat fungsi dipanggil."
    },
    {
        "pertanyaan": "3. Kapan return lebih tepat daripada print?",
        "pilihan": [
            "A. Saat hasil fungsi perlu digunakan kembali",
            "B. Saat ingin menghapus fungsi",
            "C. Saat ingin menghentikan komputer",
            "D. Saat ingin membuat komentar"
        ],
        "jawaban": "A",
        "pembahasan": "return mengembalikan nilai agar dapat disimpan atau digunakan dalam perhitungan lain."
    },
    {
        "pertanyaan": "4. Berapakah hasil dari kuadrat(4) jika fungsi mengembalikan x * x?",
        "pilihan": [
            "A. 8",
            "B. 12",
            "C. 14",
            "D. 16"
        ],
        "jawaban": "D",
        "pembahasan": "Hasilnya 4 * 4 = 16."
    },
    {
        "pertanyaan": "5. Mengapa variabel lokal berguna dalam fungsi?",
        "pilihan": [
            "A. Agar semua variabel menjadi global",
            "B. Agar penggunaan variabel terbatas pada fungsi",
            "C. Agar program tidak memerlukan parameter",
            "D. Agar semua hasil otomatis dicetak"
        ],
        "jawaban": "B",
        "pembahasan": "Variabel lokal membatasi penggunaan nama variabel pada ruang lingkup fungsi."
    },
    {
        "pertanyaan": "6. Apa yang terjadi jika fungsi membutuhkan dua argumen wajib tetapi hanya diberi satu?",
        "pilihan": [
            "A. Program selalu menghasilkan nol",
            "B. Fungsi otomatis menambah argumen",
            "C. Python menghasilkan TypeError",
            "D. Python menghapus fungsi"
        ],
        "jawaban": "C",
        "pembahasan": "Jumlah argumen tidak memenuhi parameter wajib sehingga Python menghasilkan TypeError."
    },
    {
        "pertanyaan": "7. Apa output dari kode berikut?\ndef tambah(a, b):\n    return a + b\n\nprint(tambah(3, 5) * 2)",
        "pilihan": [
            "A. 8",
            "B. 10",
            "C. 13",
            "D. 16"
        ],
        "jawaban": "D",
        "pembahasan": "tambah(3, 5) menghasilkan 8, kemudian 8 dikalikan 2 menjadi 16."
    },
    {
        "pertanyaan": "8. Apa perbedaan Step Into dan Step Over di VS Code?",
        "pilihan": [
            "A. Step Into masuk ke fungsi, Step Over menjalankan satu baris tanpa menelusuri isi fungsi",
            "B. Step Into menghapus kode, Step Over menyimpan kode",
            "C. Step Into untuk GitHub, Step Over untuk Python",
            "D. Keduanya digunakan hanya untuk mencetak hasil"
        ],
        "jawaban": "A",
        "pembahasan": "Step Into menelusuri isi fungsi, sedangkan Step Over melewati penelusuran baris internal fungsi."
    },
    {
        "pertanyaan": "9. Mengapa modularisasi membantu pengujian program?",
        "pilihan": [
            "A. Karena semua kode digabung menjadi satu baris",
            "B. Karena program tidak membutuhkan input",
            "C. Karena setiap fungsi dapat diuji secara terpisah",
            "D. Karena kesalahan tidak mungkin terjadi"
        ],
        "jawaban": "C",
        "pembahasan": "Fungsi dengan tugas yang jelas memudahkan pengujian dan pencarian kesalahan."
    },
    {
        "pertanyaan": "10. Perintah Git apa yang mengirim commit lokal ke GitHub setelah remote terhubung?",
        "pilihan": [
            "A. git init",
            "B. git push",
            "C. git add",
            "D. git status"
        ],
        "jawaban": "B",
        "pembahasan": "git push mengirim commit lokal ke repositori remote seperti GitHub."
    }
]
