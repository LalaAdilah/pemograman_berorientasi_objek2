class Film:
    def __init__(self, judul, genre):
        self.judul = judul
        self.genre = genre
class Sutradara:
    def __init__(self, nama, film):
        self.nama = nama
        self.film = film
    def daftar_film(self):
        print("Film Karya Sutradara pidi:");
        for film in self.film:
            print(film.judul, film.genre)
f1 = Film("Milea", "(Roman)",)
f2 = Film("Dilan", "(Roman)")
sutradara = Sutradara("Pidi", [f1, f2])
sutradara.daftar_film()