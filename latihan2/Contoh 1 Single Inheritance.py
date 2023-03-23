#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def Melaju(self):
        print(f"sebuah {self.jenis} sedang melaju pelan")
class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def Parkir(self):
        print(f"{self.jenis} dengan merk { self.merk}  warna {self.warna} sedang parkir dipinggir jalan")
mobilA = Mobil("Mobil","Pajero Sport", "Hitam", 2477)
mobilA.Melaju()
mobilA.Parkir()