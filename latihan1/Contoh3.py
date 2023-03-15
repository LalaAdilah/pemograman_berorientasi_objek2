class Persegi:
    def __init__(self, panjang,lebar):
        self.p = panjang
        self.l = lebar
    def luas(self):
        return (self.p * self.l)
persegiA = Persegi(2,5)
print(f"Luas Persegi: {persegiA.luas()}")