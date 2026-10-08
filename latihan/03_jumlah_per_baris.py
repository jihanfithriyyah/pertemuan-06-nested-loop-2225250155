# Loop luar mengontrol baris i (1 sampai 4)
# Loop dalam mengontrol kolom j (1 sampai 3)
# Akumulator total_baris direset ke 0 di awal setiap baris baru
# Output menampilkan jumlah total hasil i * j per baris

for i in range(1, 5):
    total_baris = 0
    for j in range(1, 4):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")