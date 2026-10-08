# Pertemuan 06 Nested Loop Python

Nama: Jihan Fithriyyah
NIM: 2225250155
Kelas: 3A

## Tujuan
- Memahami konsep dasar serta alur eksekusi dari dua tingkat perulangan (nested loop).
- Menerapkan perulangan bertingkat untuk membangun struktur pola bintang dan tabel angka dua dimensi.
- Mengimplementasikan teknik akumulasi data, baik untuk taraf kelompok/baris maupun taraf keseluruhan.
- Menggunakan logika pencacahan (counter) berdasar syarat kondisi tertentu pada pasangan indeks.

## Cara Menjalankan
```bash
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
Loop Luar (i): Bertugas memproses nomor baris dari rentang 1 hingga n. Pada tiap iterasi awal baris, nilai total_baris disiapkan dari angka 0.   
Loop Dalam (j): Bertugas memproses nomor kolom dari rentang 1 hingga n untuk baris i yang sedang aktif.   
Proses Perkalian (hasil): Mengalikan variabel i dan j (hasil = i * j), lalu mencetaknya secara rata kanan agar membentuk tabel yang rapi.
Akumulator (total_baris & total_semua): total_baris menjumlahkan seluruh hasil di baris tersebut. Nilai hasil juga ditambahkan ke total_semua untuk menghitung akumulasi seluruh matriks.
Counter (count_genap): Mengecek kondisi hasil % 2 == 0. Jika syarat bernilai genap, nilai count_genap akan bertambah 1.   

##Hasil Pengujian
Input n	Hasil yang Diharapkan	Keluaran Aktual	Status
-1	Menolak input negatif, menampilkan pesan peringatan, dan meminta input ulang	Menampilkan "n harus positif." dan meminta input ulang	Berhasil
1	Tabel 1x1, Total seluruh = 1, Banyak genap = 0	Total seluruh hasil = 1, Banyak hasil genap = 0	Berhasil
2	Tabel 2x2, Total seluruh = 9, Banyak genap = 3	Total seluruh hasil = 9, Banyak hasil genap = 3	Berhasil
3	Tabel 3x3, Total seluruh = 36, Banyak genap = 5	Total seluruh hasil = 36, Banyak hasil genap = 5	Berhasil
(Test case ini sudah disesuaikan dengan nilai wajib dari modul).   
Analisis Efisiensi
Jumlah eksekusi pada badan perulangan dalam bergantung pada kuadrat dari nilai input, yaitu sebanyak n×n (n 
2) kali.   
Misalkan input n=3, maka loop dalam akan berulang sebanyak 3 
2 = 9 kali untuk memproses seluruh sel matriks.   
Ketika skala nilai n diperbesar, jumlah operasi perkalian dan pemeriksaan kondisi genap akan meningkat secara kuadratik.   

##Refleksi
Kesalahan yang Ditemukan: Terjadi error NameError: name 'count' is not defined saat menjalankan program karena terdapat ketidakcocokan pemanggilan variabel di baris cetak akhir.
