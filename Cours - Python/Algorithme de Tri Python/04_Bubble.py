def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        # Déclare une variable pour suivre si des échanges ont été faits
        swapped = False
        # Parcourt la liste jusqu'à n-i-1 car les derniers i éléments sont déjà triés
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                # Échange les éléments s'ils sont dans le mauvais ordre
                liste[j], liste[j+1] = liste[j+1], liste[j]
                swapped = True
        # Si aucun échange n'a été fait, la liste est déjà triée
        if not swapped:
            break
    return liste

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
print("Liste originale :", liste)
sorted_liste = bubble_sort(liste)
print("Liste triée :", sorted_liste)
