def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        # Trouver le minimum dans la sous-liste liste[i:n]
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        # Échanger le minimum trouvé avec le premier élément de la sous-liste
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
print("Liste originale :", liste)
sorted_liste = selection_sort(liste)
print("Liste triée :", sorted_liste)

