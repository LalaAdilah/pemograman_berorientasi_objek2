class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(5, 9)) 
print(Kalkulator.subtract(45, 12)) 
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(9, 7)) 
print(Kalkulator.divide(30, 6)) 
