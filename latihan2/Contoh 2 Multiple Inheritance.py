#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang mengerjakan tugas")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang membuat laporan pekerjaan")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def mengobrol(self):
        print(self.nama, "sedang mengobrol")
mhs_pekerja = MahasiswaPekerja("Shabira", "230001", "Akuntan")
mhs_pekerja.belajar() 
mhs_pekerja.bekerja() 
mhs_pekerja.mengobrol() 