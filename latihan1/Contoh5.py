class Kereta:
    def __init__(self, kelas, tujuan):
        self.kelas = kelas
        self.tujuan = tujuan
    def info(self):
        print(f"kelas: {self.kelas}\nTujuan: {self.tujuan}")
keretaA = Kereta("Luxury", "Cirebon - Semarang")
keretaA .info()