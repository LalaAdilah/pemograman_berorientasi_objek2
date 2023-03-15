class Pegawai:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
    def info(self):
        print(f"Nama: {self.nama}\nNIP: {self.nip}")
pegawaiA = Pegawai("Lala", "20223")
pegawaiA.info()