print("Praktikum 5 (Zahwa Nur Azkia Putri - 064002300038)")
print("-------ELKOM 2-------")

class Film:
    def __init__(self, nama, tahun_rilis, director):
        self.nama = nama
        self.tahun_rilis = tahun_rilis
        self.director = director

# Membuat list kosong untuk menampung objek film-film favorit
daftar_film_favorit = []

# Meminta input dari pengguna untuk menambahkan detail film-film favorit
for i in range(5):
    print("Film favorit ke-{}".format(i+1))
    nama = input("Judul: ")
    tahun_rilis = input("Rilis: ")
    director = input("Director: ")
    
    # Membuat objek Film dan menambahkannya ke dalam list
    film = Film(nama, tahun_rilis, director)
    daftar_film_favorit.append(film)
    print()

