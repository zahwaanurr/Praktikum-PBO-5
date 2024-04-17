print("Praktikum 5 (Zahwa Nur Azkia Putri - 064002300038)")
print("-------ELKOM 1-------")

film_favorit = []

for i in range(5):
    film = input("Film favorit ke-{}: ".format(i+1))
    film_favorit.append(film)

print("\nDaftar film favorit")
for i, film in enumerate(film_favorit):
    print("{}. {}".format(i+1, film))
