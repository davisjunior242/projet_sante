# ============================================================
# CALCULATRICE AVEC QUATRE (4) FONCTIONS DE BASE
# Apprenant: M'BIELO-LIBEAU Davis Junior
# Date: 09 juillet 2026
# ============================================================


# SECTION 1 : LES FONCTIONS DES OPÉRATIONS MATHÉMATIQUES

def addition(a, b):
    return a + b 

def soustraction(a, b):
    return a - b 

def multiplication(a, b):
    return a * b  # L'astérisque * sert pour la multiplication

def division(a, b):
    if b == 0:
        print("Impossible de diviser par zéro")
        return None
    return a / b


# SECTION 2 : LES FONCTIONS POUR L'AFFICHAGE ET L'INTERACTION

def afficher_menu():
    print("\nQuelle operation veux-tu faire ?")
    print("1 - Addition") 
    print("2 - Soustraction") 
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")   

def obtenir_nombre(message):
    while True:  
        try:
            nombre = float(input(message))
            return nombre
        except ValueError:
            print("Tu dois entrer un nombre valide !")

def afficher_resultat(a, operateur, b, resultat):
    print("\n" + "=" * 50)  
    print(f" {a} {operateur} {b} = {resultat}")  
    print("=" * 50)

def demander_continuation():
    print("\nVeux-tu faire un autre calcul ?")
    reponse = input("Tape 'oui' ou 'non' : ")
    if reponse.lower() == "oui":
        return True  
    else:
        return False 

def afficher_au_revoir():

    print("\nMerci d'avoir utilisé AkieniCalcul ! A bientôt !")

# SECTION 3 : LA FONCTION PRINCIPALE

def calculatrice():
    print("=" * 50)
    print("            AKIENI CALCULETTE - DATASCIENCE")
    print("=" * 50)
    
    continuer = True
    
    # Tant que continuer est Vrai, on fait des calculs
    while continuer:
        # Étape 1: Afficher le menu des opérations
        afficher_menu()
        
        # Étape 2: Demander le choix de l'utilisateur
        choix = input("Tape le numéro de ton choix : ")
        
        # Étape 3: Vérifier si l'utilisateur veut quitter
        if choix == "5":
            # On dit au revoir et on sort de la boucle
            afficher_au_revoir()
            break  # "break" sort de la boucle while
        
        # Étape 4: Vérifier si le choix est valide (1,2,3 ou 4)
        if choix not in ["1", "2", "3", "4"]:
            # Si ce n'est pas valide, on affiche un message
            print(" Ce n'est pas un choix valide ! Réessaie.")
            # "continue" fait revenir au début de la boucle
            continue
        
        # Étape 5: Demander les deux nombres à l'utilisateur
        print("\nDonner les deux nombres :")
        a = obtenir_nombre("Premier nombre : ")
        b = obtenir_nombre("Deuxième nombre : ")
        
        erreur = False  # On suppose qu'il n'y a pas d'erreur
        
        # Étape 7: Faire le calcul selon le choix de l'utilisateur
        if choix == "1":
            resultat = addition(a, b) 
            operateur = "+" 
        elif choix == "2":
            resultat = soustraction(a, b)
            operateur = "-"
        elif choix == "3":
            resultat = multiplication(a, b)
            operateur = "×"
        elif choix == "4":
            resultat = division(a, b)
            operateur = "÷"
            if resultat is None:
                erreur = True
        
        # Étape 8: Afficher le résultat (s'il n'y a pas d'erreur)
        if not erreur:
            afficher_resultat(a, operateur, b, resultat)
        
        # Étape 9: Demander si l'utilisateur veut continuer
        if not demander_continuation(): 
            afficher_au_revoir()
            continuer = False  

# SECTION 4 : LANCEMENT DU PROGRAMME
calculatrice()