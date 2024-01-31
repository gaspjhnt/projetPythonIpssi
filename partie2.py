from math import sqrt


# Déterminer le PGCD entre deux nombres entiers.
def pgcd(x, y):
    
    """ Calcul du PGCD de deux entiers X et Y """
    while y != 0:
        x, y = y, x % y
    return x



# Déterminer si un nombre entier est premier
def isPrime(n):

    """Verification d'un nombre entier s'il est premier"""
    if n <= 1:
        return False
    
    # On sait que si n pas premier il doit avoir un diviseur <= à sa racine carrée.
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



# Déterminer si deux nombres entiers sont entiers entre eux
def arePrime(x, y):
    
    """Appelle de la fonction PGCD"""
    if (pgcd(x, y) != 1):
        return False
    return True




if __name__ == "__main__":
    
    """ Déterminer le PGCD entre deux nombres entiers """
    # Récuperation des nombres entrés par l'utilisateur
    nb1 = int(input("Entrez un nombre entier : "))
    nb2 = int(input("Entrez un deuxième nombre entier : "))
    # Appelle de la fonction
    print("Le PGCD de", nb1, "et", nb2, "est", pgcd(nb1, nb2))


    """ Déterminer si un nombre entier est premier """
    # Récuperation d'un nombre entré par l'utilisateur
    nb3 = int(input("Entrez un nombre entier :"))
    if (isPrime(nb3)):
        print(nb3, "est premier.")
    else:
        print(nb3, "n'est pas premier.")


    """ Déterminer si deux nombres entiers sont prmier entre eux c'est à dire leur PGCD == 1"""
    # Récuperation d'un nombre entré par l'utilisateur
    nb4 = int(input("Entrez un nombre entier : "))
    nb5 = int(input("Entrez un deuxième nombre entier : "))
    if (arePrime(nb4, nb5)):
        print(nb4, "et", nb5,"sont premiers entre eux.")
    else:
        print(nb4, "et", nb5,"ne sont pas premiers entre eux.")