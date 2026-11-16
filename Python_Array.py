nama = ["Beras", "Minyak", "Gula", "Telur", "Garam"]
harga = [5000, 12000, 8000, 15000, 3000]

print("Barang ke-1:", nama[0], "-", harga[0])

# tambah barang baru
nama.append("Kopi")
harga.append(20000)

# harga minyak naik
harga[1] = 13000

print("\nDaftar barang:")
for i in range(len(nama)):
    print(f"{i+1}. {nama[i]} : Rp{harga[i]}")

print("\nTotal harga:", sum(harga))

murah = harga.index(min(harga))
mahal = harga.index(max(harga))
print("Termurah:", nama[murah], "-", harga[murah])
print("Termahal:", nama[mahal], "-", harga[mahal])