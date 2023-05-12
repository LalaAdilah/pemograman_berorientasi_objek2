print('Lala Adilah\n 210511117 \nT121C(R3)\n')
try:
    x = int(input("Enter a number: "))
except EOFError:
    print("End of file reached")
except ValueError:
    print("Invalid input")