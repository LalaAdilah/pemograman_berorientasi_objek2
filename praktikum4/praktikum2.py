class Mahasiswa:
    def __init__(self, nama, prodi):
        self.nama = nama
        self.prodi = prodi
class Kelompok_KKM:
    def __init__(self, nama, mahasiswa):
        self.nama = nama
        self.mahasiswa = mahasiswa
    def daftar_mahasiswa(self):
        print("Kelompok KKM:");
        for mahasiswa in self.mahasiswa:
            print(mahasiswa.nama, mahasiswa.prodi)
mhs1 = Mahasiswa("Intan", "PGSD")
mhs2 = Mahasiswa("Ajeng", "ILKOM")
kelomook_kkm = Kelompok_KKM("2", [mhs1, mhs2])
kelomook_kkm.daftar_mahasiswa()