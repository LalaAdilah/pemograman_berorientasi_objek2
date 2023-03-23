#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3

class Seseorang:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    def get_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("alamat:", self.alamat)
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, nama, umur, alamat, mahasiswa_id):
        super().__init__(nama, umur, alamat)
        self.mahasiswa_id = mahasiswa_id
    def get_info(self):
        super().get_info()
        print("Mahasiswa_id:", self.mahasiswa_id)
# Single Inheritance
class Karyawan(Seseorang):
    def __init__(self, nama, umur, alamat, karyawan_id, salary):
        super().__init__(nama, umur, alamat)
        self.karyawan_id = karyawan_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("Karyawan_id:", self.karyawan_id)
        print("Salary:", self.salary)
# Multiple Inheritance
class Penulis(Karyawan, Mahasiswa):
    def __init__(self, nama, umur, alamat, karyawan_id, salary, mahasiswa_id,published_books):
        Karyawan.__init__(self, nama, umur, alamat, karyawan_id, salary)
        Mahasiswa.__init__(self, nama, umur, alamat, mahasiswa_id)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("Mahasiswa_id:", self.mahasiswa_id)
        print("Published Books:", self.published_books)


