"""
Program Pasar Tradisional
Penerapan struktur data:
  1. Array       -> daftar barang dan harga
  2. Linked List -> keranjang belanja (node dan pointer)
  3. Tuple       -> data pedagang dan hari buka pasar (tetap/immutable)
"""


# =====================================================
# 1. ARRAY - daftar barang dan harga
# =====================================================
def demo_array():
    print("=" * 50)
    print("1. ARRAY - Daftar Barang")
    print("=" * 50)

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

    # hapus barang (nama dan harga dihapus di index yang sama)
    i = nama.index("Garam")
    nama.pop(i)
    harga.pop(i)
    print("\nSetelah Garam dihapus:", nama)

    # cari barang
    cari = "Telur"
    if cari in nama:
        idx = nama.index(cari)
        print(f"{cari} ditemukan, harga Rp{harga[idx]}")


# =====================================================
# 2. LINKED LIST - keranjang belanja
# =====================================================
class Node:
    def __init__(self, barang):
        self.barang = barang
        self.next = None


class Keranjang:
    def __init__(self):
        self.head = None

    def tambah_awal(self, barang):
        node = Node(barang)
        node.next = self.head
        self.head = node

    def tambah_akhir(self, barang):
        node = Node(barang)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def sisip_setelah(self, target, barang):
        cur = self.head
        while cur and cur.barang != target:
            cur = cur.next
        if cur is None:
            print(f"  '{target}' tidak ada di keranjang")
            return
        node = Node(barang)
        node.next = cur.next
        cur.next = node

    def hapus(self, barang):
        cur, prev = self.head, None
        while cur and cur.barang != barang:
            prev, cur = cur, cur.next
        if cur is None:
            print(f"  '{barang}' tidak ditemukan")
            return
        if prev is None:
            self.head = cur.next      # hapus node pertama
        else:
            prev.next = cur.next

    def cari(self, barang):
        cur, pos = self.head, 1
        while cur:
            if cur.barang == barang:
                return pos
            cur, pos = cur.next, pos + 1
        return -1

    def jumlah(self):
        cur, n = self.head, 0
        while cur:
            n, cur = n + 1, cur.next
        return n

    def tampil(self):
        cur, hasil = self.head, []
        while cur:
            hasil.append(cur.barang)
            cur = cur.next
        print("  " + " -> ".join(hasil) + " -> None" if hasil else "  (kosong)")


def demo_linked_list():
    print("\n" + "=" * 50)
    print("2. LINKED LIST - Keranjang Belanja")
    print("=" * 50)

    # a) membuat dan menyambung node secara manual
    n1 = Node("Beras")
    n2 = Node("Minyak")
    n3 = Node("Gula")
    n1.next = n2
    n2.next = n3

    print("Traversal node manual:")
    cur = n1
    while cur:
        print(" ", cur.barang)
        cur = cur.next

    # b) mengelola node lewat class Keranjang
    print("\nMengelola keranjang dengan class:")
    k = Keranjang()
    k.tambah_akhir("Beras")
    k.tambah_akhir("Minyak")
    k.tambah_akhir("Gula")
    print("Awal:")
    k.tampil()

    k.tambah_awal("Telur")
    print("Tambah Telur di awal:")
    k.tampil()

    k.tambah_akhir("Kopi")
    print("Tambah Kopi di akhir:")
    k.tampil()

    k.sisip_setelah("Minyak", "Garam")
    print("Sisip Garam setelah Minyak:")
    k.tampil()

    k.hapus("Gula")
    print("Hapus Gula:")
    k.tampil()

    print("Posisi Garam  :", k.cari("Garam"))
    print("Jumlah barang :", k.jumlah())


# =====================================================
# 3. TUPLE - data pedagang dan hari buka (tetap)
# =====================================================
def demo_tuple():
    print("\n" + "=" * 50)
    print("3. TUPLE - Data Pedagang")
    print("=" * 50)

    pedagang = ("P001", "Bu Mimi", "Los Sayur")

    kode, nama, lokasi = pedagang
    print("Kode  :", kode)
    print("Nama  :", nama)
    print("Lokasi:", lokasi)

    # pedagang[2] = "Los Ikan"   # ERROR, data lapak tidak boleh berubah sembarangan
    try:
        pedagang[2] = "Los Ikan"
    except TypeError as e:
        print("Ubah lokasi: ERROR ->", e)

    # Hari buka pasar (tetap)
    hari_buka = ("Senin", "Rabu", "Jumat", "Minggu")
    print("Pasar buka hari pertama:", hari_buka[0])
    print("Jumlah hari buka       :", len(hari_buka))
    print("Buka hari Jumat?       :", "Jumat" in hari_buka)

    # kumpulan tuple dalam satu list
    daftar_pedagang = [
        ("P001", "Bu Mimi", "Los Sayur"),
        ("P002", "Pak Momo", "Los Ikan"),
        ("P003", "Bu Mima", "Los Buah"),
    ]
    print("\nDaftar pedagang:")
    for kode, nama, lokasi in daftar_pedagang:
        print(f"  {kode} | {nama:<10} | {lokasi}")


# =====================================================
# PROGRAM UTAMA
# =====================================================
if __name__ == "__main__":
    demo_array()
    demo_linked_list()
    demo_tuple()