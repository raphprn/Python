import random

nombre_mystere = random.randint(1, 100)
devine = None

while devine != nombre_mystere:
    devine = int(input("Entrez votre devinette : "))

    if devine < nombre_mystere:
        print("Plus haut")
    elif devine > nombre_mystere:
        print("Plus bas")
    else:
        print("Bravo ! Vous avez trouvé le nombre mystère.")