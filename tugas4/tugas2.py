
class Guru:
    def __init__(self, nama, umur):
        self. nama = nama
        self.umur = umur
class Sekolah:
    def __init__(self, nama, guru):
        self.nama = nama
        self.guru = guru
    def daftar_guru(self):
        print("Daftar Guru di Sekolah:");
        for guru in self.guru:
            print(guru.nama, guru.umur)
g1 = Guru("Aina", 30,)
g2 = Guru("Soraya",29)
sekolah = Sekolah("Pidi", [g1, g2])
sekolah.daftar_guru()

