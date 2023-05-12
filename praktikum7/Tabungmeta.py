#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan volume tabung
        def luas(cls, jari):
            return 3.14 *jari * jari
        cls.luas = classmethod(luas)
        
        def volume(cls, jari, tinggi):
            return 3.14 *jari * jari * tinggi
        cls.volume = classmethod(volume)
class Tabung(metaclass=TabungMeta):
    pass
s = Tabung()
# Menghitung luas permukaan tabung dengan jari=7
luas_tabung = Tabung.luas(7)
print("Luas Tabung:", luas_tabung)
# Menghitung volume tabung dengan jari=7 dan tinggi=12
volume_tabung = Tabung.volume(5, 10)
print("Volume Tabung:", volume_tabung)