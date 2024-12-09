import random

a = random.randint(0, 10)
b = random.randint(0, 10)

print("Nombre a: " + str(a))
print("Nombre b: " + str(b))

if a > b:
    print("Le nombre a est plus grand que le nombre b.")
elif a < b :
    print("Le nombre a est plus petit que le nombre b.")
else :
    print("Les deux nombres sont égaux.")