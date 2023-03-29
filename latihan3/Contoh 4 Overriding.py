#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C

from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def start(self):
        pass

class Mobil(Kendaraan):
    def start(self):
        print("Starting Mobil...")

class Motor(Kendaraan):
    def start(self):
        print("Starting Motor...")

class Bus(Kendaraan):
    def start(self):
        print("Starting bus...")

kendaraan = [Mobil(), Motor(), Bus()]

for kendaraan in kendaraan:
    kendaraan.start()