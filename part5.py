from colorama import Fore, Style, init
init(autoreset=True)

def salle_du_jugement():
    print(Fore.YELLOW + "\nLa grande porte s’ouvre dans un fracas assourdissant. Une lumière éblouissante inonde la pièce.")
    print(Fore.MAGENTA + "Vous entrez dans une immense salle circulaire, où un trône en pierre est placé au centre.")
    print(Fore.RED + "Sur ce trône, une silhouette encapuchonnée vous observe silencieusement.")
    print(Fore.CYAN + "La voix grave de la silhouette résonne : 'Bienvenue, voyageurs. Vous avez prouvé votre bravoure jusqu’ici, mais êtes-vous dignes d’aller plus loin ?'")
    print(Fore.GREEN + "Le Jugement commence. Vous devrez répondre correctement aux questions et affronter le gardien si nécessaire.")

    print(Fore.RED + "\n1. Répondre à ses questions.")
    print(Fore.RED + "2. Défier directement la silhouette.")
    print(Fore.RED + "3. Tenter de fuir en trouvant une autre issue.")

    choix = input(Fore.WHITE + "Que fais-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.YELLOW + "\nLa silhouette commence à poser ses énigmes.")
        enigme_du_jugement()
    elif choix == "2":
        print(Fore.RED + "\nTu dégaines une arme improvisée et défies la silhouette. Elle se lève lentement, dévoilant un immense guerrier de pierre.")
        print(Fore.RED + "Le combat est inévitable.")
        combat_gardien()
    elif choix == "3":
        print(Fore.MAGENTA + "\nVous tentez de fuir, mais les murs se referment. La silhouette éclate de rire : 'Vous ne pouvez échapper au Jugement !'")
        print(Fore.RED + "Un piège se déclenche, et vous êtes obligés de revenir au centre de la salle.")
        salle_du_jugement()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        salle_du_jugement()

def enigme_du_jugement():
    print(Fore.MAGENTA + "\nLa silhouette pose la première énigme :")
    print(Fore.CYAN + "'Plus je suis grand, moins vous en voyez. Que suis-je ?'")
    print(Fore.RED + "1. Le brouillard")
    print(Fore.RED + "2. La nuit")
    print(Fore.RED + "3. L’obscurité")

    choix = input(Fore.WHITE + "Réponds à l’énigme (1/2/3) : ")

    if choix == "2":
        print(Fore.GREEN + "\nLa silhouette hoche la tête : 'Correct. La nuit cache le monde à vos yeux.'")
        print(Fore.YELLOW + "Une lumière éclaire une porte au fond de la salle.")
        print(Fore.CYAN + "Max chuchote : 'C’était la bonne réponse... continuons.'")
        fin_partie_5()
    elif choix in ["1", "3"]:
        print(Fore.RED + "\nLa silhouette gronde : 'Mauvaise réponse ! Vous devez payer pour votre ignorance.'")
        combat_gardien()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        enigme_du_jugement()

def combat_gardien():
    print(Fore.RED + "\nLe gardien de pierre se lève et s’approche lentement.")
    print(Fore.YELLOW + "Max crie : 'Attention ! Il est énorme !'")
    print(Fore.CYAN + "\nQue fais-tu ?")
    print(Fore.RED + "1. Attaquer avec une arme improvisée.")
    print(Fore.RED + "2. Chercher un point faible.")
    print(Fore.RED + "3. Tenter de distraire le gardien.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.RED + "\nTu attaques le gardien avec tout ce que tu as, mais sa peau de pierre est impénétrable.")
        print(Fore.YELLOW + "Il contre-attaque, et vous êtes projetés contre un mur.")
        print(Fore.MAGENTA + "Max trouve une faiblesse pendant que tu te relèves.")
        combat_suite()
    elif choix == "2":
        print(Fore.GREEN + "\nTu observes attentivement le gardien et remarques une fissure sur son genou droit.")
        print(Fore.YELLOW + "Tu hurles à Max : 'La fissure ! Vise la fissure !'")
        combat_suite()
    elif choix == "3":
        print(Fore.MAGENTA + "\nTu lances un objet pour distraire le gardien. Il se retourne un instant, ce qui te donne le temps d’attaquer.")
        print(Fore.YELLOW + "Max s’élance et frappe la fissure sur son genou.")
        combat_suite()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        combat_gardien()

def combat_suite():
    print(Fore.GREEN + "\nLe gardien tombe à genoux, grièvement blessé.")
    print(Fore.YELLOW + "La silhouette sur le trône applaudit lentement : 'Impressionnant. Vous avez vaincu mon gardien.'")
    print(Fore.CYAN + "Une porte s’ouvre, révélant un escalier menant encore plus profondément sous terre.")
    print(Fore.MAGENTA + "Max te regarde et dit : 'On ne peut plus reculer maintenant. Allons-y.'")
    fin_partie_5()

def fin_partie_5():
    print(Fore.YELLOW + "\nVous franchissez la porte et descendez les escaliers. L’air devient plus froid, et une nouvelle lumière brille au loin.")
    print(Fore.CYAN + "Max murmure : 'Qu’est-ce qui nous attend encore... ?'")
    print(Fore.MAGENTA + "\n**Parties 6-10 : En cours de développement...**")

# Lancer la Partie 5
salle_du_jugement()