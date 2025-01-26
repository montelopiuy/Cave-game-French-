from colorama import Fore, Style, init
init(autoreset=True)

def niveau1():
    print(Fore.YELLOW + "\nTu te réveilles dans une cave sombre et humide. Le sol est froid et tu entends des gouttes d'eau qui tombent, créant un écho dans la pièce.")
    print(Fore.CYAN + "Tu sens l'air moisi et l'humidité autour de toi, et tu vois à peine à cause de l'obscurité.")
    print(Fore.GREEN + "Devant toi, une porte en bois vieux et usé se dresse. Une faible lumière filtre sous la porte.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Ouvrir la porte.")
    print(Fore.RED + "2. Regarder autour de toi pour chercher quelque chose.")
    print(Fore.RED + "3. Tenter d'appeler à l'aide.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu ouvres la porte avec précaution. La porte grince de manière effrayante. Derrière, tu aperçois un tunnel sombre qui s'étend à l'infini.")
        print(Fore.YELLOW + "Le tunnel semble interminable et tu entends des bruits étranges. Tu décides d'avancer, espérant trouver une sortie.")
        niveau2()
    elif choix == "2":
        print(Fore.CYAN + "\nTu regardes autour de toi. Sur le sol, tu vois un vieux livre, une clé rouillée et un morceau de papier froissé.")
        print(Fore.MAGENTA + "Tu prends la clé, espérant qu'elle pourra t'aider à ouvrir la porte.")
        niveau2()
    elif choix == "3":
        print(Fore.RED + "\nTu cries à l'aide, mais ta voix semble se perdre dans l'obscurité. Il n'y a aucune réponse. Tu es seul.")
        print(Fore.YELLOW + "Tu sais qu'il te faut avancer, peu importe la peur qui grandit en toi.")
        niveau2()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        niveau1()

def niveau2():
    print(Fore.YELLOW + "\nAprès avoir ouvert la porte, tu entres dans un tunnel qui semble encore plus sombre. Le sol est glissant.")
    print(Fore.CYAN + "Le tunnel est humide et tu entends des bruits lointains... comme des murmures.")
    print(Fore.GREEN + "Au bout du tunnel, tu aperçois une faible lumière venant d'une porte en bois. Tu entends des chuchotements derrière.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Ouvrir doucement la porte pour voir ce qu'il y a derrière.")
    print(Fore.RED + "2. Fuir et retourner dans la cave.")
    print(Fore.RED + "3. Appeler à nouveau.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu ouvres doucement la porte. Derrière, un petit garçon te regarde, perdu et effrayé. Il semble tout aussi perdu que toi.")
        print(Fore.YELLOW + "'Je m'appelle Max', dit-il. 'Je t'ai vu arriver et je pense qu'on doit sortir ensemble.'")
        print(Fore.CYAN + "Il te tend la main, espérant que tu le suives.")
        niveau3()
    elif choix == "2":
        print(Fore.RED + "\nTu décides de fuir. Tu retournes dans la cave, mais la porte derrière toi se ferme violemment.")
        print(Fore.MAGENTA + "Tout devient encore plus sombre et une froideur glaciale te saisit. Il ne reste plus qu'à avancer.")
        niveau2()
    elif choix == "3":
        print(Fore.YELLOW + "\nTu appelles à nouveau et cette fois, tu entends un écho qui semble répondre. C'est le garçon.")
        print(Fore.GREEN + "'Je suis ici,' dit-il. 'S'il te plaît, aide-moi à sortir.'")
        niveau3()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        niveau2()

def niveau3():
    print(Fore.CYAN + "\nLe garçon t'invite à le suivre. Il te guide dans un tunnel étroit et humide. Au fur et à mesure, la lumière devient plus vive.")
    print(Fore.YELLOW + "Finalement, vous arrivez dans une grande salle. C'est un étrange labyrinthe de portes anciennes, toutes fermées.")
    print(Fore.GREEN + "'Il faut qu'on trouve la bonne porte', dit Max. 'Mais il y a des pièges à éviter.'")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Entrer dans la première porte.")
    print(Fore.RED + "2. Demander au garçon de t'expliquer d'abord.")
    print(Fore.RED + "3. Tenter de sortir par une autre issue.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu ouvres la première porte. Derrière, tu te retrouves dans une pièce remplie de vieux objets et de papiers.")
        print(Fore.YELLOW + "Tu vois des indices qui pourraient t'aider à avancer. Max t'explique qu'il faut résoudre une série d'énigmes pour passer à l'étape suivante.")
        niveau4()
    elif choix == "2":
        print(Fore.YELLOW + "\nLe garçon t'explique qu'il y a plusieurs portes, mais il faut être prudent.")
        print(Fore.GREEN + "'Ne t'inquiète pas', dit-il, 'on va les résoudre ensemble.'")
        niveau4()
    elif choix == "3":
        print(Fore.RED + "\nTu tentes de chercher une issue, mais tout est verrouillé. Il n'y a pas d'autre choix que d'entrer par une porte.")
        niveau4()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        niveau3()

def niveau4():
    print(Fore.CYAN + "\nDans la salle d'énigmes, plusieurs portes se dressent devant toi.")
    print(Fore.YELLOW + "Chacune d'elles a une inscription gravée.")
    print(Fore.GREEN + "Sur la première porte, l'inscription dit : 'Je ne peux pas être vu, mais je peux être entendu. Que suis-je ?'")
    
    enigme = input(Fore.WHITE + "Résous l'énigme pour ouvrir la porte : ")

    if enigme.lower() == "écho":
        print(Fore.GREEN + "\nLa porte s'ouvre lentement, révélant un passage lumineux.")
        print(Fore.YELLOW + "Le garçon te sourit et dit : 'Nous avons presque fini. Tu es fort.'")
        niveau5()
    else:
        print(Fore.RED + "\nL'énigme reste sans réponse. Tu réfléchis à nouveau, essayant de trouver la solution.")
        niveau4()

def niveau5():
    print(Fore.CYAN + "\nTu te retrouves finalement dans une pièce éclairée par une lumière douce.")
    print(Fore.YELLOW + "Les portes se ferment derrière toi, mais tu sais que tu as trouvé la sortie.")
    print(Fore.GREEN + "'Nous y sommes', dit Max. 'Tu es libre maintenant.'")
    print(Fore.MAGENTA + "Tu vois la lumière d'une sortie au loin. Félicitations, tu as réussi à t'échapper !")

# Démarrer l'aventure
niveau1()