# Jeux_casino
Jeux de hasard python IDE

## Notre règle du jeu

— Le joueur mise sur un numéro compris entre 0 et 49 (50 en tout). En choisissant
son numéro, il y dépose la somme qu’il souhaite miser.
— La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros
pairs sont de couleur noire, les numéros impairs sont de couleur rouge. Le croupier
lance la roulette, lâche la bille et quand la roulette s’arrête, relève le numéro
de la case dans laquelle la bille s’est arrêtée. Dans notre programme, nous ne
reprendrons pas tous ces détails « matériels » mais ces explications sont aussi à
l’intention de ceux qui ont eu la chance d’éviter les salles de casino jusqu’ici. Le
numéro sur lequel s’est arrêtée la bille est, naturellement, le numéro gagnant.
— Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50,
plutôt faible), le gain est de 3 fois la somme misée.
— Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur
que le numéro gagnant (s’ils sont tous les deux pairs ou tous les deux impairs).
Si c’est le cas, le gain est de 50 % de la somme misée. Si ce n’est pas le cas, le
joueur perd sa mise.
Dans les deux scénarios gagnants vus ci-dessus (le numéro misé et le numéro gagnant sont
identiques ou ont la même couleur), le croupier remet au joueur la somme initialement
misée avant d’y ajouter ses gains. Cela veut dire que, dans ces deux scénarios, le joueur
récupère de l’argent. Il n’y a que dans le troisième cas qu’il perd la somme misée.

A vous de jouer
