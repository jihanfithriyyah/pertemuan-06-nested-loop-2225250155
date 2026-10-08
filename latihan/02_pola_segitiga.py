# Loop luar mengontrol jumlah baris (1 sampai n)
# Loop dalam mengontrol jumlah bintang di setiap baris
# Output menampilkan pola segitiga bintang bertingkat

n = int(input("n: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()