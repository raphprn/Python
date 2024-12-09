class Personne:
    def __init__(self, nom, age, taille):
        self.nom = nom
        self.age = age
        self.taille = taille

    def __repr__(self): # Pour un meilleur affichage
        return f"{self.nom}, {self.age} ans, {self.taille} cm"
    
def tri_par_age(personnes):
    for i in range(1, len(personnes)):
        key = personnes[i]
        j = i - 1
        while j >= 0 and key.age < personnes[j].age:
            personnes[j + 1] = personnes[j]
            j -= 1
        personnes[j + 1] = key
    return personnes

# Exemple d'utilisation
personnes = [Personne("Alice", 25, 165), Personne("Bob", 20, 175), Personne("Charlie", 23, 180)]
print(tri_par_age(personnes))
