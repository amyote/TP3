import random



continuer = True
initNouvelleRonde = True

niveauVie = 20
numeroAdversaire = 0
numeroCombat = 0

nombreVictoire = 0
nombreVictoireSuite = 0
nombreDefaite = 0

forceMinDe = 1
forceMaxDe = 5
forceBoss = 10


# Montrer le statut pre=combat a l'utilisateur.
def print_status():
    print(f"STATUT PRE-COMBAT:\n\
Adversaire: {numeroAdversaire}\n\
Force de l'adversaire: {forceAdversaire}\n\
Niveau de vie de l'usager: {niveauVie}\n\
Combat {numeroCombat}: {nombreVictoire} vs {nombreDefaite}")


while continuer:
    
    input("\n\nAppuyez sur Entree pour continuer/commencer...")


    # Si on devrait initialiser une nouvelle ronde. En particulier, on ne devrait pas s'ils choisissent de voir les regles.
    if initNouvelleRonde:

        numeroAdversaire += 1

        if nombreVictoireSuite >= 3:
            forceAdversaire = forceBoss
        else:
            # On a une distribution differente entre chiffre au hasard entre 1 et 12 et somme de deux chiffres au hasard entre 1 et 6
            forceAdversaire = random.randint(forceMinDe, forceMaxDe) + random.randint(forceMinDe, forceMaxDe)

    # Dire a l'utilisateur sa situation et ses options.
    print(f"Vous tombez face a face avec un adversaire de difficulte: {forceAdversaire}.")
    entree = input("Que voulez-vous faire?\n\
1. Combattre cet adversaire\n\
2. Contourner cet adversaire et aller ouvrir une autre porte\n\
3. Afficher les regles du jeu\n\
4. Quitter la partie\n\
: ")


    # S'il choisit de se battre, on affiche le statut, roule le de du joueur et on compare a la force de l'adversaire.
    if entree == "1":

        print_status()

        numeroCombat += 1

        resultatDes = random.randint(1, 6) + random.randint(1, 6)
        victoireCombat = resultatDes > forceAdversaire

        print(f"COMBAT:\n\
Lancer des: {resultatDes}\n\
Dernier combat: {'victoire' if victoireCombat else 'defaite'}")

        # Si on gagne, augmenter le nombre de victoire, le nombre de victoires de suite et le niveau de vie.
        if victoireCombat:

            nombreVictoire += 1
            nombreVictoireSuite += 1

            niveauVie += forceAdversaire
            print(f"STATUT POST-COMBAT:\n\
Niveau de vie: {niveauVie}\n\
Nombre de victoires consecutives: {nombreVictoireSuite}")
    
        # Si on perd, augmenter le nombre de defaites, annuler le nombre de victoires de suite et diminuer le niveau de vie.
        else:

            nombreDefaite += 1
            nombreVictoireSuite = 0

            niveauVie -= forceAdversaire
            print(f"STATUT POST-COMBAT:\n\
Niveau de vie: {niveauVie}")

            # Verifier si on est mort.
            if niveauVie <= 0:
                print(f"La partie est terminee, vous avez vaincu {nombreVictoire} monstre(s)")
                continuer = False
        initNouvelleRonde = True
    
    # S'il choisit de ne pas se battre, on diminue le niveau de vie.
    elif entree == "2":

        niveauVie -= 1
        initNouvelleRonde = True

    # S'il veut voir les regles, on lui montre.
    elif entree == "3":

        print("REGLES:\n\
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n\
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\
La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

        initNouvelleRonde = False
        

    # S'il veut quitter, on termine la boucle de jeu.
    elif entree == "4":

        print("Merci et au revoir...")
        continuer = False

# QUESTION THEORIQUE: QUE FAUDRAIT-IL CHANGER POUR AVOIR PLUSIEURS MONSTRES DERRIERE UNE PORTE
# En fait il y a plusieurs manieres de le faire, mais en voici une qui se passe sur plusieures rondes.
# (Pre-combat) On prend une liste de force d'adversaires au hasard
# (Combat) On enleve la somme des forces d'adversaires au niveau de vie du joueur
# Le joueur choisit un monstre a attaquer
# On prend un nombre d'attaque au hasard pour le joueur.
# S'il bat le monstre (nombre d'attaque plus haut que la force du monstre), il gagne son nombre de niveau de vie. Sinon, rien n'arrive.
# Continuer jusqu'a ce que soit le joueur perde tout son niveau de vie ou les monstres sont tous vaincus
