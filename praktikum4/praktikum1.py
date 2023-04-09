class Jurnal:
    def __init__(self, judul, halaman):
        self.judul = judul
        self.halaman = halaman
class Peneliti:
    def __init__(self, nama, jurnal):
        self.nama = nama
        self.jurnal = jurnal
    def daftar_jurnal(self):
        for jurnal in self.jurnal:
            print(jurnal.judul, jurnal.halaman)
jurnal1 = Jurnal("Sistem Informasi", 90,)
jurnal2 = Jurnal("Basis Data", 75)
peneliti = Peneliti("Syarifah", [jurnal1, jurnal2])
peneliti.daftar_jurnal()