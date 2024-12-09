vies_restantes = 7
mot_secret = "abricot"
mot_decouvert = "_____"
lettres_utilisees = ""

while vies_restantes > 0 and mot_decouvert != mot_secret:
    print("Mot à deviner:", mot_decouvert)
    print("Lettres déjà utilisées:", lettres_utilisees)
    proposition = input("Proposez une lettre: ")
    lettres_utilisees += proposition + " "
    
    if proposition in mot_secret:
        print("La lettre est dans le mot !")
        mot_decouvert = ""
        for index in range(len(mot_secret)):
            if mot_secret[index] in lettres_utilisees:
                mot_decouvert += mot_secret[index]
            else:
                mot_decouvert += "_"
    else:
        print("La lettre est pas dans le mot.")
        vies_restantes -= 1

if mot_decouvert == mot_secret:
    print("Vous avez trouvé le mot", mot_secret, "!")
else:
    print("Perdu ! Le mot était:", mot_secret)