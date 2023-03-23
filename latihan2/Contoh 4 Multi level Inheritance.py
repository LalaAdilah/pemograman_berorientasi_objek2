#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3

class Buku:
    def __init__(self, judul):
        self.judul = judul
    def Dibaca(self):
        print(f"{self.judul} dibaca")
class Novel(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul)
        self.penulis = penulis
    def Dipinjam(self):
        print(f"sebuah novel berjudul {self.judul} karya {self.penulis} dipinjam oleh nia")
class Religi(Novel):
    def __init__(self, judul, penulis, halaman):
        super().__init__(judul, penulis)
        self.halaman = halaman
    def Dikembalikan(self):
        print(f"Novel {self.judul} karya {self.penulis} yang tebalnya {self.halaman} halaman sudah dikembalikan nia")
religi = Religi("Wanita Muslimah", "Rahmahtunisa", 300)
religi.Dipinjam() 
religi.Dikembalikan() 