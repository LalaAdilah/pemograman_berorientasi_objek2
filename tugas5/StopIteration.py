print('Lala Adilah\n 210511117 \nT121C(R3)\n')
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
        if number == 3:
            raise StopIteration
    except StopIteration:
        break