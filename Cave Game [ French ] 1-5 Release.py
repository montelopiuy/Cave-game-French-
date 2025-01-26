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