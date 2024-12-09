nbre1 = int(input("Entrez un nombre 1 "))
nbre2 = int(input("Entrez un nombre 2 "))

operation = int(input("Operation : 1 = addition, 2 = soustraction / 3 = multiplication / 4 = division "))

if operation == 1:
    print(nbre1 + nbre2)
elif operation == 2:
    print(nbre1 - nbre2)
elif operation == 3:
    print(nbre1 * nbre2)
elif operation == 4:
    print(nbre1 / nbre2)
else:
    print("Erreur")