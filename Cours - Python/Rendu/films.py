import random
from PIL import Image

image = Image.open("/Users/raphaelparone/Documents/IIM/Cours - Python/Rendu/image.png")
image.show()

films = [
    "Star Wars",
    "Le Seigneur des Anneaux",
    "Harry Potter",
    "Jurassic Park",
    "Titanic",
    "Avatar",
    "Matrix",
    "Le Parrain",
    "Pulp Fiction",
    "Forrest Gump"
]

score = 0
erreurs = 0
films_trouves = set()
random.shuffle(films)

print("Devinez les films !")

while len(films_trouves) < len(films):
    guess = input("\nQuel est le titre du film ? ")

    if guess in films_trouves:
        print("Déjà trouvé !")
    elif guess.lower() in [film.lower() for film in films]:
        score += 1
        films_trouves.add(guess)
        print("Correct ! Votre score est :", score)
    else:
        erreurs += 1
        print("Incorrect ! Erreurs :", erreurs)

    if erreurs >= 3:
        print("Game Over ! Votre score final est :", score)
        break
else:
    print("Félicitations ! Vous avez trouvé tous les films. Votre score est de :", score)
