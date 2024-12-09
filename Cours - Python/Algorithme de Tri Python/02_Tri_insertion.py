def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        # Déplacer les éléments de liste[0..i-1], qui sont plus grands que la clé,
        # d'une position vers la droite pour faire de la place à la clé
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
print("Liste originale :", liste)
sorted_liste = insertion_sort(liste)
print("Liste triée :", sorted_liste)


