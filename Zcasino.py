import random
import math
import mods


def main():
    choix = True
    while choix : 
        # Partie 1 : Initialisation du joueur
        somme_misee = mods.demander_mise()
        nombre_choisi = mods.demander_nombre()
        couleur_choisie = mods.determiner_couleur(nombre_choisi)
        
        # Partie 2 : Verification et resultat
        nombre_random = random.randint(0, 49)
        print(f"la valeur du nombre random est , {nombre_random} \n")
        couleur_random = mods.determiner_couleur(nombre_random)
        print(f"la couleur random est , {couleur_random} \n")
        
        if nombre_choisi == nombre_random:
            somme_misee += somme_misee * 3
            choix = mods.demander_choix()
            
        elif couleur_choisie == couleur_random:
            somme_misee += math.ceil(somme_misee * 0.5)
            choix = mods.demander_choix()
        else:
            somme_misee = 0
            print("Vous avez tout perdu\n")
            choix = False
        
        print(f"Votre nouvelle somme est : {somme_misee}")

if __name__ == "__main__":
    main()
