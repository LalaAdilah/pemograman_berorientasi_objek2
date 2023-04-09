class Buku:
    def __init__(self, judul, jenis):
        self.judul = judul
        self.jenis = jenis
class Penulis:
    def __init__(self, nama, buku):
        self.nama = nama
        self.buku = buku
    def daftar_buku(self):
        print("Buku Karya Penulis Hamka:");
        for buku in self.buku:
            print(buku.judul, buku.jenis)
bk1 = Buku("Di bawah Lindungan Ka'bah", "(Novel)",)
bk2 = Buku("Terusir", "(Novel)")
penulis = Penulis("Hamka", [bk1, bk2])
penulis.daftar_buku()