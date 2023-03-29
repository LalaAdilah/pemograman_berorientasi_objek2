#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C

class Ayam:
    def bersuara(self):
        print("Uuuuu")
class Bebek:
    def bersuara(self):
        print("Wek wek")

def cetak_suara(objek):
    objek.bersuara()

ayam = Ayam()
bebek = Bebek()

cetak_suara(ayam) 
cetak_suara(bebek) 