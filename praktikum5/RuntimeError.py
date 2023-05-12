print('Lala Adilah\n 210511117 \nT121C(R3)\n')
def get_data():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data

print(get_data())