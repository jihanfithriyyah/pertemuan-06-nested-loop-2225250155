# Loop luar mengontrol variabel i (1 sampai 3)
# Loop dalam mengontrol variabel j (1 sampai 4)
# Counter bertambah untuk setiap pasangan (i, j) yang terbentuk
# Output menampilkan setiap pasangan dan total pasangan

count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")