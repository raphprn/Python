# Tri par sélection (Selection Sort)
def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    return liste

# Tri à bulles (Bubble Sort)
def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                swapped = True
        if not swapped:
            break
    return liste

# Tri rapide (Quick Sort)
def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    left = [x for x in liste if x < pivot]
    middle = [x for x in liste if x == pivot]
    right = [x for x in liste if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Tri fusion (Merge Sort)
def merge_sort(liste):
    if len(liste) <= 1:
        return liste
    mid = len(liste) // 2
    left_half = merge_sort(liste[:mid])
    right_half = merge_sort(liste[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Tri par insertion (Insertion Sort)
def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste


import time
import random

# Générer des jeux de données
# liste triée
sorted_list = [i for i in range(100)]
# liste inversée
reversed_list = [i for i in range(100, 0, -1)]
# liste random
random_list = [random.randint(1, 100) for _ in range(100)]
# grande liste random
large_random_list = [random.randint(1, 1000) for _ in range(1000)]

# Liste des algorithmes de tri
sort_algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Insertion Sort": insertion_sort
}

# Comparer les performances
for name, sort_func in sort_algorithms.items():
    print(f"\n{name}:")
    for test_case, data in [("Sorted List", sorted_list), ("Reversed List", reversed_list), ("Random List", random_list), ("Large Random List", large_random_list)]:
        data_copy = data[:]
        start_time = time.time()
        sort_func(data_copy)
        end_time = time.time()
        print(f"{test_case}: {end_time - start_time:.6f} seconds")
