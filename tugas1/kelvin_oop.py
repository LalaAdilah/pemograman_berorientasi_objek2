#Nama    : Lala 'Adilah
#NIM     : 210511117
#Kelas   : R3 / TI21C 

class Kelvin:
    def __init__(self,kelvin):
        self.K = kelvin
    def to_celcius(self):
        return self.K - 273
    def to_reamur(self):
        return 4/5 * (self.K - 273)
    def to_fahrenheit(self):
        return 9/5 * (self.K - 273) + 32
Kelvin1= Kelvin (int(input("Masukkan Kelvin :")))
print(f"Konversi derajat Kelvin ke derajat celcius adalah: {Kelvin1.to_celcius()}")
print(f"Konversi derajat Kelvin ke derajat reamur adalah: {Kelvin1.to_reamur()}")
print(f"Konversi derajat Kelvin ke derajat kelvin adalah: {Kelvin1.to_fahrenheit()}")

