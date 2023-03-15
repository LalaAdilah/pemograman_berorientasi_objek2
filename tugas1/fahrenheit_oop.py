#Nama    : Lala 'Adilah
#NIM     : 210511117
#Kelas   : R3 / TI21C 

class Fahrenheit:
    def __init__(self,fahrenheit):
        self.F = fahrenheit
    def to_celcius(self):
        return 5/9 * (self.F - 32)
    def to_reamur(self):
        return 4/9 * (self.F - 32)
    def to_kelvin(self):
        return 5/9 * (self.F - 32) + 273
Fahrenheit1= Fahrenheit (int(input("Masukkan Fahrenheit :")))
print(f"Konversi derajat fahrenheit ke derajat celcius adalah: {Fahrenheit1.to_celcius()}")
print(f"Konversi derajat fahrenheit ke derajat reamur adalah: {Fahrenheit1.to_reamur()}")
print(f"Konversi derajat fahrenheit ke derajat kelvin adalah: {Fahrenheit1.to_kelvin()}")

