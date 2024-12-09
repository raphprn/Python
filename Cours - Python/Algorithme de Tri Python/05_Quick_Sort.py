def quicksort(liste):
    def partition(low, high):
        pivot = liste[high]  # Choisir le pivot
        i = low - 1       # Indice du plus petit élément
        for j in range(low, high):
            if liste[j] <= pivot:
                i = i + 1
                liste[i], liste[j] = liste[j], liste[i]
        liste[i + 1], liste[high] = liste[high], liste[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(liste) - 1)
    return liste

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
print("Liste originale :", liste)
sorted_liste = quicksort(liste)
print("Liste triée :", sorted_liste)
