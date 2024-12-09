def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

liste1 = [64, 25, 12, 22, 11]
liste2 = liste1.copy()

print("Liste originale :", liste1)

# Tri par sélection
sorted_liste1 = selection_sort(liste1)
print("Liste triée avec selection_sort() :", sorted_liste1)

# Utilisation de la méthode sort()
liste2.sort()
print("Liste triée avec sort() :", liste2)
