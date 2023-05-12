#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C

class KetupatMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan volume ketupat
        def luas(cls, D1, D2):
            return 1/2 *D1 * D2
        cls.luas = classmethod(luas)
        
        def volume(cls, D1, D2, tinggi):
            return 1/2 *D1 * D2 * tinggi
        cls.volume = classmethod(volume)
class Ketupat(metaclass=KetupatMeta):
    pass
t = Ketupat()
# Menghitung luas permukaan ketupat dengan D1=3 dan D2=7
luas_ketupat = Ketupat.luas(3,7)
print("Luas Ketupat:", luas_ketupat)
# Menghitung volume ketupat dengan D1=3, D2=7 dan tinggi=9
volume_ketupat = Ketupat.volume(3, 7, 9)
print("Volume Ketupat:", volume_ketupat)