#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C


class Matematika:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c
mat = Matematika()
B = mat.add(7, 8, 6)
print(B)

mat = Matematika()
C = mat.add(8,2)
print(C)