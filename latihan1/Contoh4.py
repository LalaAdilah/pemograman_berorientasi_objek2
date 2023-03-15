class Novel:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")
novelA = Novel("Ayat-Ayat Cinta", "Asma Nadia")
novelA.info()