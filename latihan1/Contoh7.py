
class Kelvin:
    @staticmethod
    def to_fahrenheit(kelvin):
        return 9/5 * (kelvin - 273) + 32
    @staticmethod
    def to_celcius(kelvin):
        return kelvin - 273
    @staticmethod
    def to_reamur(kelvin):
        return 4/5 * (kelvin - 273)
mykelvin = 200
myfahrenheit = Kelvin.to_fahrenheit(mykelvin)
print(myfahrenheit)
