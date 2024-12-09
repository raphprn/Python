class Personne:
    def __init__(self, nom, age, taille):
        self.nom = nom
        self.age = age
        self.taille = taille

    def __repr__(self): # Pour un meilleur affichage
        return f"{self.nom}, {self.age} ans, {self.taille} cm"
    

def merge_sort_personne(personnes, key):
    if len(personnes) <= 1:
        return personnes
    mid = len(personnes) // 2
    left_half = merge_sort_personne(personnes[:mid], key)
    right_half = merge_sort_personne(personnes[mid:], key)
    return merge_personne(left_half, right_half, key)

def merge_personne(left, right, key):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if getattr(left[i], key) < getattr(right[j], key):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Exemple d'utilisation
personnes = [Personne("Alice", 25, 165), Personne("Bob", 20, 175), Personne("Charlie", 23, 180)]
print(merge_sort_personne(personnes, 'age'))
