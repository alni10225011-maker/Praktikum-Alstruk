class Node:
    def __init__(self, barang):
        self.barang = barang
        self.next = None

# buat 3 node
n1 = Node("Beras") 
n2 = Node("Minyak")
n3 = Node("Gula")

# sambungkan
n1.next = n2
n2.next = n3

# tampilkan
cur = n1
while cur:
    print(cur.barang)
    cur = cur.next