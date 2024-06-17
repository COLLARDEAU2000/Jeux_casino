def demander_mise():
    while True:
        try:
            somme_misee = float(input("Entrez la somme à miser : "))
            if somme_misee > 0:
                return somme_misee
            else:
                print("La somme doit être positive et superieur a 0.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre valide.")

def demander_nombre():
    while True:
        try:
            nombre = int(input("Choisissez un nombre entre 0 et 49 : "))
            if 0 <= nombre <= 49:
                return nombre
            else:
                print("Le nombre doit être compris entre 0 et 49.")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un nombre entier.")

def determiner_couleur(nombre):
    return 'noir' if nombre % 2 == 0 else 'rouge'

def choix_fait(valeur) -> bool:
	return True if valeur  == "yes" else False

def demander_choix():
    while True:
        try:
            choix = str(input("Choisissez  entre yes et no : "))
            if choix == "yes" or choix == "no":
                return  choix_fait(choix)
            else:
                print("Le choix doit être entre yes et no ")
        except ValueError:
            print("Erreur de saisie. Veuillez entrer un choix entre yes ou no.")