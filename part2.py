from colorama import Fore, Style, init
init(autoreset=True)

def maison():
    print(Fore.YELLOW + "\nAprès avoir quitté la cave, tu te retrouves dans une maison étrange. Les murs sont en béton renforcé, et toutes les fenêtres sont bloquées par des barres de métal.")
    print(Fore.CYAN + "Le garçon, Max, te suit de près. Il chuchote : 'Je crois qu'on est toujours en danger... cette maison n'est pas normale.'")
    print(Fore.GREEN + "Soudain, une lourde porte métallique claque derrière toi. Une voix rauque résonne dans la maison :")
    print(Fore.RED + "'Vous êtes mes invités maintenant... mais pas pour longtemps.'")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Fouiller la pièce pour trouver une arme.")
    print(Fore.RED + "2. Essayer de forcer une fenêtre pour t'échapper.")
    print(Fore.RED + "3. Chercher un endroit pour te cacher.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu fouilles la pièce et trouves un couteau de cuisine posé sur une table. Ce n'est pas une arme idéale, mais ça pourrait t'aider à te défendre.")
        print(Fore.YELLOW + "Max te regarde et dit : 'On doit rester ensemble.'")
        niveau_maison2("arme")
    elif choix == "2":
        print(Fore.RED + "\nTu essaies de forcer une fenêtre, mais les barres de métal sont solides. La voix rauque se rapproche...")
        print(Fore.MAGENTA + "'Vous ne sortirez jamais !'")
        niveau_maison2("aucune arme")
    elif choix == "3":
        print(Fore.CYAN + "\nTu trouves un placard et décides de t'y cacher avec Max. Vous retenez votre souffle tandis que des pas lourds se rapprochent.")
        print(Fore.RED + "'Je sens votre peur...' dit la voix rauque.")
        niveau_maison2("aucune arme")
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        maison()

def niveau_maison2(equipement):
    print(Fore.YELLOW + "\nLe boucher, un homme imposant avec un tablier ensanglanté et une hache, entre dans la pièce. Il vous fixe avec un sourire terrifiant.")
    print(Fore.CYAN + "Max panique, mais tu sais qu'il faut agir rapidement.")
    print(Fore.MAGENTA + "Que fais-tu ?")
    print(Fore.RED + "1. Attaquer le boucher avec ce que tu as.")
    print(Fore.RED + "2. Lancer un objet pour distraire le boucher et courir.")
    print(Fore.RED + "3. Parler au boucher pour gagner du temps.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1" and equipement == "arme":
        print(Fore.GREEN + "\nTu fonces sur le boucher avec ton couteau. Il est surpris et recule légèrement, mais il est encore très dangereux.")
        print(Fore.YELLOW + "Max trouve un objet lourd et t'aide à le frapper. Ensemble, vous parvenez à désarmer le boucher.")
        niveau_maison3()
    elif choix == "1" and equipement == "aucune arme":
        print(Fore.RED + "\nTu essaies d'attaquer le boucher à mains nues, mais il te repousse facilement. Il rit en disant : 'Courageux, mais stupide.'")
        print(Fore.YELLOW + "Max te tire par le bras et crie : 'Fuyons !'")
        niveau_maison3()
    elif choix == "2":
        print(Fore.CYAN + "\nTu lances un objet pour distraire le boucher. Il se retourne, et toi et Max courez vers une autre pièce.")
        print(Fore.GREEN + "Le boucher grogne : 'Vous ne pourrez pas fuir pour toujours !'")
        niveau_maison3()
    elif choix == "3":
        print(Fore.MAGENTA + "\nTu essaies de parler au boucher. Il s'arrête un instant, intrigué, mais son sourire terrifiant revient rapidement.")
        print(Fore.RED + "'Parler ne vous sauvera pas.' Il lève sa hache...")
        print(Fore.YELLOW + "Max te tire par le bras pour fuir.")
        niveau_maison3()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        niveau_maison2(equipement)

def niveau_maison3():
    print(Fore.YELLOW + "\nVous trouvez une trappe cachée dans le sol. Max crie : 'Par ici !'")
    print(Fore.CYAN + "Vous ouvrez la trappe et descendez dans un passage étroit. Le boucher est sur vos talons.")
    print(Fore.GREEN + "Alors que vous avancez, vous trouvez une porte métallique avec un clavier numérique.")
    print(Fore.MAGENTA + "Une note est accrochée à la porte : 'La clé est 5321.'")
    print(Fore.RED + "Le boucher arrive derrière vous, brandissant sa hache.")
    print(Fore.YELLOW + "Que fais-tu ?")
    print(Fore.RED + "1. Entrer rapidement le code pour ouvrir la porte.")
    print(Fore.RED + "2. Tenter de bloquer le passage avec un objet lourd.")
    print(Fore.RED + "3. Faire face au boucher pour le ralentir.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu entres le code rapidement, et la porte s'ouvre. Toi et Max vous précipitez à l'intérieur et refermez la porte juste à temps.")
        print(Fore.YELLOW + "Vous êtes à l'abri... pour l'instant.")
    elif choix == "2":
        print(Fore.CYAN + "\nTu trouves une étagère et la renverses pour bloquer le passage. Cela ralentit le boucher, mais il est toujours en train de vous poursuivre.")
        print(Fore.GREEN + "Tu utilises ce temps pour entrer le code et ouvrir la porte.")
        print(Fore.YELLOW + "Vous êtes à l'abri... pour l'instant.")
    elif choix == "3":
        print(Fore.RED + "\nTu te prépares à faire face au boucher, mais il est beaucoup trop fort. Tu es gravement blessé.")
        print(Fore.YELLOW + "Max t'entraîne malgré tout dans la pièce après avoir ouvert la porte.")
        print(Fore.CYAN + "Vous êtes à l'abri, mais à quel prix ?")
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        niveau_maison3()

# Commencer la partie 2
maison()