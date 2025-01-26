from colorama import Fore, Style, init
init(autoreset=True)

def souterrains():
    print(Fore.YELLOW + "\nVous descendez dans un long tunnel sombre, seulement éclairé par une faible lueur émanant des murs.")
    print(Fore.CYAN + "Max murmure : 'Qu’est-ce que c’est que cet endroit... ? On dirait une sorte de labyrinthe.'")
    print(Fore.MAGENTA + "Le sol est humide, et des gravures étranges recouvrent les murs. Vous entendez des bruits lointains, comme des chaînes qui traînent.")
    print(Fore.RED + "Que fais-tu ?")
    print(Fore.RED + "1. Suivre les gravures pour trouver un chemin.")
    print(Fore.RED + "2. Explorer le tunnel au hasard.")
    print(Fore.RED + "3. Vous arrêter pour écouter les bruits et analyser l’environnement.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nVous suivez les gravures, qui semblent raconter une histoire étrange. Elles parlent d’un 'gardien' qui protège un trésor.")
        print(Fore.YELLOW + "Soudain, une porte cachée s’ouvre, révélant une nouvelle salle.")
        gardien()
    elif choix == "2":
        print(Fore.CYAN + "\nVous avancez au hasard dans le tunnel. Les bruits deviennent plus forts, et vous vous retrouvez face à une grande grille.")
        print(Fore.RED + "Un symbole étrange brille sur la grille.")
        grille()
    elif choix == "3":
        print(Fore.MAGENTA + "\nVous vous arrêtez pour écouter. Les bruits semblent provenir de plusieurs directions.")
        print(Fore.RED + "Max trouve un mécanisme au sol et dit : 'Regarde ça... on dirait un piège.'")
        piege()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        souterrains()

def gardien():
    print(Fore.YELLOW + "\nVous entrez dans une grande salle circulaire, où se tient une immense statue avec des yeux brillants.")
    print(Fore.CYAN + "Une voix résonne : 'Pour avancer, vous devez prouver votre valeur. Répondez à mon énigme ou affrontez ma colère.'")
    print(Fore.MAGENTA + "L’énigme est la suivante :")
    print(Fore.GREEN + "'Je suis toujours devant toi, mais tu ne peux jamais m’atteindre. Que suis-je ?'")
    print(Fore.RED + "1. Le futur")
    print(Fore.RED + "2. Une ombre")
    print(Fore.RED + "3. Un mirage")

    choix = input(Fore.WHITE + "Réponds à l’énigme (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nLa statue s’anime et dit : 'Tu as raison. Le futur est inaccessible, mais il guide toujours nos pas.'")
        print(Fore.CYAN + "Une porte s’ouvre, et vous avancez dans un nouveau tunnel.")
        souterrains_suite()
    elif choix == "2":
        print(Fore.RED + "\nLa statue gronde : 'Faux. Une ombre te suit, elle ne te précède pas.'")
        print(Fore.YELLOW + "Un piège s’active, et des flèches volent dans la pièce. Vous devez fuir !")
        souterrains()
    elif choix == "3":
        print(Fore.RED + "\nLa statue gronde : 'Faux. Un mirage est une illusion, mais je parle d’une réalité inaccessible.'")
        print(Fore.YELLOW + "Le sol se dérobe sous vos pieds, et vous tombez dans une fosse.")
        souterrains()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        gardien()

def grille():
    print(Fore.YELLOW + "\nLa grille est scellée par un symbole étrange. Max remarque un mécanisme à côté.")
    print(Fore.CYAN + "Une inscription dit : 'Le bon choix vous ouvrira la voie, mais un faux pas vous coûtera cher.'")
    print(Fore.MAGENTA + "Trois boutons sont devant vous, chacun avec un symbole différent :")
    print(Fore.RED + "1. Un cercle avec une flamme.")
    print(Fore.RED + "2. Un triangle avec une goutte d’eau.")
    print(Fore.RED + "3. Un carré avec une feuille.")

    choix = input(Fore.WHITE + "Quel symbole choisis-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.RED + "\nTu appuies sur le bouton, mais une explosion se déclenche, et des flammes remplissent la salle.")
        print(Fore.YELLOW + "Vous êtes obligés de fuir en courant.")
        souterrains()
    elif choix == "2":
        print(Fore.GREEN + "\nTu appuies sur le bouton, et de l’eau jaillit du sol, éteignant un piège caché.")
        print(Fore.CYAN + "La grille s’ouvre lentement, vous permettant de continuer.")
        souterrains_suite()
    elif choix == "3":
        print(Fore.RED + "\nTu appuies sur le bouton, mais le sol se fissure, et des lianes vous attaquent.")
        print(Fore.YELLOW + "Vous devez fuir à toute vitesse.")
        souterrains()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        grille()

def piege():
    print(Fore.YELLOW + "\nMax examine le mécanisme et dit : 'Je crois qu’on peut désactiver ça, mais c’est risqué.'")
    print(Fore.CYAN + "Un levier rouillé est visible à côté.")
    print(Fore.RED + "1. Tenter de désactiver le piège.")
    print(Fore.RED + "2. Ignorer le piège et continuer prudemment.")
    print(Fore.RED + "3. Utiliser un objet pour bloquer le mécanisme.")

    choix = input(Fore.WHITE + "Que fais-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.GREEN + "\nMax désactive le piège avec succès, et un passage secret s’ouvre.")
        print(Fore.YELLOW + "Vous avancez vers une nouvelle salle.")
        souterrains_suite()
    elif choix == "2":
        print(Fore.RED + "\nVous passez à côté du piège, mais une flèche est tirée et blesse légèrement Max.")
        print(Fore.CYAN + "Malgré la douleur, vous continuez à avancer.")
        souterrains_suite()
    elif choix == "3":
        print(Fore.GREEN + "\nTu utilises un objet pour bloquer le mécanisme. Le piège est désactivé, et vous continuez votre chemin.")
        souterrains_suite()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        piege()

def souterrains_suite():
    print(Fore.YELLOW + "\nVous atteignez une immense porte ornée de symboles lumineux. Elle semble mener à un endroit encore plus dangereux.")
    print(Fore.CYAN + "Max te regarde et dit : 'On est proches de la fin, je le sens... mais es-tu prêt ?'")
    print(Fore.RED + "La porte s’ouvre lentement, révélant une lumière aveuglante.")
    print(Fore.MAGENTA + "\n**Partie 5 : En construction...**")

# Commencer la partie 4
souterrains()