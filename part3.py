from colorama import Fore, Style, init
init(autoreset=True)

def foret():
    print(Fore.YELLOW + "\nVous sortez de la maison du boucher en courant, épuisés mais soulagés d’être encore en vie.")
    print(Fore.CYAN + "Max s’arrête et dit : 'Regarde autour de toi... où sommes-nous ?'")
    print(Fore.GREEN + "Autour de vous, une forêt dense, avec des arbres gigantesques dont les branches semblent former des ombres menaçantes.")
    print(Fore.RED + "Une étrange brume s’installe, et un murmure inquiétant résonne à travers les arbres.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Avancer prudemment à travers la forêt.")
    print(Fore.RED + "2. Chercher un abri pour la nuit.")
    print(Fore.RED + "3. Essayer de retrouver votre chemin en appelant à l’aide.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nVous avancez lentement dans la forêt. Les branches craquent sous vos pas, et les murmures deviennent plus forts.")
        print(Fore.YELLOW + "Max te suit de près, serrant une branche comme arme de fortune. Soudain, une silhouette apparaît au loin.")
        rencontre()
    elif choix == "2":
        print(Fore.CYAN + "\nVous trouvez une vieille cabane abandonnée au milieu des arbres. Elle semble vide, mais l’atmosphère est étrange.")
        print(Fore.RED + "Max murmure : 'Je ne suis pas sûr que ce soit une bonne idée...'")
        cabane()
    elif choix == "3":
        print(Fore.RED + "\nTu cries à l’aide, mais les murmures semblent répondre à tes appels. Une voix sinistre résonne : 'Tu n’aurais pas dû venir ici.'")
        print(Fore.MAGENTA + "Max te regarde avec terreur : 'C’était une erreur, courons !'")
        fuite()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        foret()

def rencontre():
    print(Fore.YELLOW + "\nLa silhouette s’approche lentement. C’est une vieille femme avec des vêtements déchirés et un regard vide.")
    print(Fore.CYAN + "Elle tend la main vers vous et chuchote : 'Vous êtes en danger... mais je peux vous aider, à un prix.'")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Lui demander de l’aide malgré tout.")
    print(Fore.RED + "2. Ignorer la vieille femme et continuer.")
    print(Fore.RED + "3. La menacer avec une arme improvisée.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nLa vieille femme te donne une amulette étrange et murmure : 'Cela vous protégera, mais n’oubliez pas... tout a un prix.'")
        print(Fore.YELLOW + "Vous continuez votre chemin, mais un sentiment d’inquiétude vous envahit.")
        foret_suite()
    elif choix == "2":
        print(Fore.CYAN + "\nVous passez à côté d’elle sans un mot. Elle rit doucement : 'Vous n’arriverez jamais à vous en sortir seuls.'")
        print(Fore.RED + "Les murmures deviennent plus forts autour de vous...")
        foret_suite()
    elif choix == "3":
        print(Fore.RED + "\nTu brandis une arme improvisée pour effrayer la vieille femme. Elle recule en riant : 'Tu regretteras ce choix.'")
        print(Fore.MAGENTA + "Max te regarde, inquiet, mais vous continuez à avancer.")
        foret_suite()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        rencontre()

def cabane():
    print(Fore.YELLOW + "\nLa cabane est sombre et poussiéreuse. Sur une table, tu trouves un carnet contenant des notes étranges.")
    print(Fore.CYAN + "Les notes parlent d’un rituel ancien pour échapper à la malédiction de la forêt.")
    print(Fore.RED + "Max trouve une carte indiquant un 'autel sacré' caché dans la forêt.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Suivre la carte pour trouver l’autel.")
    print(Fore.RED + "2. Rester dans la cabane et préparer un plan.")
    print(Fore.RED + "3. Brûler le carnet, pensant qu’il est maudit.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nVous suivez la carte, avançant prudemment à travers la forêt. Les murmures semblent vous guider...")
        autel()
    elif choix == "2":
        print(Fore.CYAN + "\nVous décidez de rester dans la cabane. Mais la nuit tombe, et des bruits étranges se font entendre dehors.")
        print(Fore.RED + "Une ombre passe devant la fenêtre, et Max murmure : 'On aurait dû partir...'")
        cabane_suite()
    elif choix == "3":
        print(Fore.RED + "\nTu brûles le carnet, mais cela semble déclencher quelque chose. La cabane tremble, et une voix hurle : 'Erreur fatale !'")
        print(Fore.YELLOW + "Vous fuyez dans la forêt sans savoir ce qui va se passer.")
        foret()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        cabane()

def fuite():
    print(Fore.RED + "\nVous courez à travers la forêt, mais les murmures deviennent des cris stridents.")
    print(Fore.YELLOW + "Max trébuche et tombe. Une ombre gigantesque semble s’approcher de lui.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Aider Max à se relever.")
    print(Fore.RED + "2. Laisser Max et continuer à fuir.")
    print(Fore.RED + "3. Affronter l’ombre malgré la peur.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu aides Max à se relever, et vous courez ensemble. L’ombre vous poursuit, mais vous trouvez un passage secret.")
        autel()
    elif choix == "2":
        print(Fore.RED + "\nTu laisses Max derrière toi. Les cris de l’ombre et de Max résonnent dans la forêt.")
        print(Fore.CYAN + "Tu te sens coupable, mais tu continues seul.")
        foret_suite()
    elif choix == "3":
        print(Fore.RED + "\nTu te tiens devant l’ombre, mais elle est trop puissante. Elle te repousse avec violence.")
        print(Fore.YELLOW + "Max te tire par le bras, et vous fuyez ensemble.")
        foret_suite()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        fuite()

def foret_suite():
    print(Fore.YELLOW + "\nAlors que vous continuez à avancer, la forêt semble changer. Les arbres bougent, et le sol devient instable.")
    print(Fore.CYAN + "Max murmure : 'C’est comme si la forêt était vivante...'")
    print(Fore.MAGENTA + "Une lumière apparaît au loin, peut-être un signe d’espoir ? Mais des cris retentissent derrière vous.")
    print(Fore.RED + "La suite dépend de vos choix précédents…")

def autel():
    print(Fore.YELLOW + "\nVous arrivez à l’autel sacré, un endroit mystérieux entouré de statues anciennes.")
    print(Fore.CYAN + "Max pose la carte sur l’autel, et un mécanisme se déclenche. Une porte apparaît dans le sol.")
    print(Fore.MAGENTA + "Mais une ombre géante s’approche derrière vous...")
    print(Fore.RED + "Que fais-tu ?")
    print(Fore.RED + "1. Entrer rapidement dans la porte.")
    print(Fore.RED + "2. Affronter l’ombre avec l’amulette.")
    print(Fore.RED + "3. Prier devant l’autel pour demander de l’aide.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nVous sautez dans la porte, laissant l’ombre derrière vous. Vous êtes dans un passage souterrain.")
        print(Fore.YELLOW + "La suite reste à découvrir...")
    elif choix == "2":
        print(Fore.RED + "\nTu brandis l’amulette, et une lumière intense repousse l’ombre. Mais l’amulette se brise.")
        print(Fore.CYAN + "Max te regarde et dit : 'On doit continuer, même sans protection.'")
        print(Fore.YELLOW + "La porte vous mène sous terre.")
    elif choix == "3":
        print(Fore.CYAN + "\nTu pries devant l’autel, et les statues semblent bouger. Une lumière apparaît, et l’ombre recule.")
        print(Fore.YELLOW + "La porte s’ouvre, et vous descendez dans le passage.")
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        autel()

# Commencer la partie 3
foret()