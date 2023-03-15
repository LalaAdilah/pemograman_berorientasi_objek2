#Nama    : Lala 'Adilah
#NIM     : 210511117
#Kelas   : R3 / TI21C 

class Reamur:
    def __init__(self,reamur):
        self.R = reamur
    def to_celcius(self):
        return 5/4 * self.R
    def to_fahrenheit(self):
        return 9/4 * self.R + 32
    def to_kelvin(self):
        return 5/4 * self.R + 273
Reamur1= Reamur (int(input("Masukkan Reamur :")))
print(f"Konversi derajat Reamur ke derajat celcius adalah: {Reamur1.to_celcius()}")
print(f"Konversi derajat Reamur ke derajat Fahrenheit adalah: {Reamur1.to_fahrenheit()}")
print(f"Konversi derajat Reamur ke derajat kelvin adalah: {Reamur1.to_kelvin()}")

