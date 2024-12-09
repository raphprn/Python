def somme(a, b):
    #Cette fonction calcul la somme de deux nombres
    #Arguments:
    #a(float): le premier nombre
    #b(float): le deuxième nombre

    #Returns:
    #float: la somme de a et b

    resultat = a + b
    return resultat

#utilisation de la fonction
x = 5
y = 3
print("La somme de", x, "et", y, "est", somme(x, y))