print('Lala Adilah\n 210511117 \nT121C(R3)\n')
import os

try:
    os.mkdir('/mydirectory')
except OSError as e:
    print("Failed to create directory: ", e)