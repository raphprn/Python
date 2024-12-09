def merge_sort(liste):
    if len(liste) <= 1:
        return liste

    # Diviser la liste en deux sous-listes
    mid = len(liste) // 2
    left_half = merge_sort(liste[:mid])
    right_half = merge_sort(liste[mid:])

    # Fusionner les deux sous-listes triées
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Fusionner les sous-listes en comparant les éléments
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Ajouter les éléments restants des sous-listes
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
print("Liste originale :", liste)
sorted_liste = merge_sort(liste)
print("Liste triée :", sorted_liste)

