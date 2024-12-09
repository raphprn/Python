def seuil_de_rentabilite(x, y, z):
    if z >= y:
        raise ValueError("Le prix avec la carte doit être inférieur au prix normal.")
    
    n = x / (y - z)
    
    return int(n) + 1

def main():
    try:
        x = float(input("Entrez le coût de la carte de cinéma (x) : "))
        y = float(input("Entrez le prix d'une place normale (y) : "))
        z = float(input("Entrez le prix d'une place avec la carte (z) : "))
        
        places = seuil_de_rentabilite(x, y, z)
        print(f"La carte d'abonnement devient rentable à partir de {places} places.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()