from colorama import Fore, Style, init
init(autoreset=True)

def sanctuaire_oublie():
    print(Fore.YELLOW + "\nVous atteignez finalement le pied de l’escalier. Devant vous s’étend une vaste salle, éclairée par des flammes vertes.")
    print(Fore.CYAN + "Max murmure : 'C’est quoi cet endroit...?'")
    print(Fore.MAGENTA + "Au centre de la pièce, une statue imposante représentant une créature mi-humaine, mi-serpent, vous observe silencieusement.")
    print(Fore.RED + "Soudain, une voix résonne dans la salle : 'Vous êtes entrés dans le sanctuaire oublié. Seuls ceux qui prouvent leur valeur peuvent continuer.'")

    print(Fore.RED + "\n1. Examiner la statue.")
    print(Fore.RED + "2. Explorer les murs pour trouver des indices.")
    print(Fore.RED + "3. Tenter d’ouvrir la porte au fond de la pièce.")
    print(Fore.RED + "4. Parler à Max pour élaborer un plan.")

    choix = input(Fore.WHITE + "Que fais-tu (1/2/3/4) ? : ")

    if choix == "1":
        print(Fore.MAGENTA + "\nTu t’approches de la statue. Ses yeux semblent te suivre.")
        print(Fore.YELLOW + "À la base de la statue, une inscription dit : 'Seuls les cœurs courageux et les esprits éclairés passeront.'")
        sanctuaire_defi()
    elif choix == "2":
        print(Fore.CYAN + "\nTu explores les murs et découvres des gravures représentant des scènes de bataille.")
        print(Fore.YELLOW + "L’un des symboles s’illumine légèrement sous ta main.")
        sanctuaire_defi()
    elif choix == "3":
        print(Fore.RED + "\nTu tentes d’ouvrir la porte au fond de la salle, mais elle est scellée.")
        print(Fore.MAGENTA + "Une voix gronde : 'Vous ne pouvez avancer sans passer l’épreuve.'")
        sanctuaire_oublie()
    elif choix == "4":
        print(Fore.CYAN + "\nTu te tournes vers Max et lui expliques que vous devez résoudre l’énigme de la pièce.")
        print(Fore.YELLOW + "Max trouve une pierre incrustée dans le sol qui semble pouvoir être activée.")
        sanctuaire_defi()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        sanctuaire_oublie()

def sanctuaire_defi():
    print(Fore.MAGENTA + "\nUne lumière envahit la pièce, et la statue s’anime lentement.")
    print(Fore.RED + "'Pour passer, vous devez répondre à mon énigme ou affronter ma colère.'")
    print(Fore.CYAN + "'Voici l’énigme : Je commence par la nuit et finis par le jour. Que suis-je ?'")
    print(Fore.RED + "1. L’ombre.")
    print(Fore.RED + "2. L’horizon.")
    print(Fore.RED + "3. Le crépuscule.")

    choix = input(Fore.WHITE + "Réponds à l’énigme (1/2/3) : ")

    if choix == "3":
        print(Fore.GREEN + "\nLa statue hoche lentement la tête : 'Bonne réponse. Vous pouvez continuer.'")
        print(Fore.YELLOW + "La porte au fond de la salle s’ouvre lentement, dévoilant un nouveau chemin.")
        fin_partie_6()
    elif choix in ["1", "2"]:
        print(Fore.RED + "\nLa statue gronde : 'Mauvaise réponse. Vous devrez payer le prix.'")
        print(Fore.MAGENTA + "Un piège se déclenche, et des créatures serpentine surgissent des ombres.")
        combat_serpents()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        sanctuaire_defi()

def combat_serpents():
    print(Fore.RED + "\nLes serpents attaquent férocement.")
    print(Fore.YELLOW + "Max hurle : 'Prends une torche, c’est notre seule chance !'")
    print(Fore.CYAN + "\nQue fais-tu ?")
    print(Fore.RED + "1. Utiliser une torche pour repousser les serpents.")
    print(Fore.RED + "2. Tenter de courir vers la porte ouverte.")
    print(Fore.RED + "3. Chercher un moyen de piéger les serpents.")

    choix = input(Fore.WHITE + "Choisis une action (1/2/3) : ")

    if choix == "1":
        print(Fore.GREEN + "\nTu brandis une torche, et les serpents reculent, effrayés par les flammes.")
        print(Fore.YELLOW + "Max en profite pour frapper un levier qui referme le sol et enferme les serpents.")
        print(Fore.MAGENTA + "La statue vous laisse passer, impressionnée par votre courage.")
        fin_partie_6()
    elif choix == "2":
        print(Fore.RED + "\nTu cours vers la porte, mais les serpents te rattrapent. Max crie pour te défendre.")
        print(Fore.MAGENTA + "Avec beaucoup de chance, vous parvenez à franchir la porte, mais Max est blessé.")
        fin_partie_6(blessure=True)
    elif choix == "3":
        print(Fore.YELLOW + "\nTu observes les environs et remarques une grille au plafond. Tu hurles à Max d'activer un levier.")
        print(Fore.GREEN + "La grille s’abat sur les serpents, les neutralisant.")
        print(Fore.CYAN + "La statue approuve votre stratégie et vous permet de continuer.")
        fin_partie_6()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        combat_serpents()

def fin_partie_6(blessure=False):
    if blessure:
        print(Fore.RED + "\nMax boitille, blessé par les serpents. Il murmure : 'Je peux continuer, mais je vais avoir besoin de repos.'")
    print(Fore.YELLOW + "\nVous traversez la porte et découvrez un immense labyrinthe de miroirs.")
    print(Fore.MAGENTA + "Les reflets se multiplient, et une voix résonne : 'Bienvenue dans le labyrinthe des âmes perdues.'")
# Lancer la Partie 6
sanctuaire_oublie()
from colorama import Fore, Style, init
import random
init(autoreset=True)

def labyrinthe_ames():
    print(Fore.MAGENTA + "\nVous entrez dans le labyrinthe. Les murs en miroir reflètent vos mouvements à l'infini.")
    print(Fore.YELLOW + "Les torches vacillantes créent des ombres inquiétantes.")
    print(Fore.CYAN + "Une voix mystérieuse murmure : 'Pour sortir, il te faudra résoudre mes énigmes et affronter tes peurs.'")

    print(Fore.RED + "\n1. Avancer tout droit.")
    print(Fore.RED + "2. Tourner à gauche.")
    print(Fore.RED + "3. Tourner à droite.")
    print(Fore.RED + "4. Parler à Max pour décider ensemble.")

    choix = input(Fore.WHITE + "Que fais-tu (1/2/3/4) ? : ")

    if choix == "1":
        print(Fore.MAGENTA + "\nVous avancez tout droit. Les miroirs semblent se resserrer autour de vous.")
        print(Fore.RED + "Soudain, une silhouette apparaît dans l’un des miroirs. Elle te ressemble... mais ce n’est pas toi.")
        enigme_miroir()
    elif choix == "2":
        print(Fore.YELLOW + "\nVous tournez à gauche et tombez sur une porte scellée. Une inscription étrange est gravée dessus.")
        print(Fore.CYAN + "'Pour ouvrir cette porte, vous devez faire face à vos regrets les plus profonds.'")
        enigme_regrets()
    elif choix == "3":
        print(Fore.CYAN + "\nVous tournez à droite et découvrez une pièce sombre.")
        print(Fore.MAGENTA + "Au centre de la pièce, un coffre fermé repose sur un piédestal. Une inscription dit : 'Choisis avec sagesse.'")
        enigme_coffre()
    elif choix == "4":
        print(Fore.CYAN + "\nTu te tournes vers Max. Il te dit : 'Je pense qu’on devrait avancer prudemment. Chaque chemin semble dangereux.'")
        labyrinthe_ames()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        labyrinthe_ames()

def enigme_miroir():
    print(Fore.MAGENTA + "\nLa silhouette dans le miroir te parle :")
    print(Fore.RED + "'Je suis toi, mais je porte le poids de tes erreurs. Si tu veux avancer, dis-moi : quelle est ta plus grande peur ?'")
    print(Fore.RED + "\n1. La solitude.")
    print(Fore.RED + "2. L’échec.")
    print(Fore.RED + "3. La trahison.")
    print(Fore.RED + "4. La mort.")

    choix = input(Fore.WHITE + "Quelle est ta réponse (1/2/3/4) ? : ")

    if choix == "1":
        print(Fore.YELLOW + "\nLa silhouette hoche la tête : 'La solitude peut être terrible, mais tu ne l’affronteras pas seul ici.'")
        print(Fore.CYAN + "Le miroir se brise, révélant un passage secret.")
        fin_labyrinthe()
    elif choix == "2":
        print(Fore.RED + "\nLa silhouette te répond : 'L’échec n’est qu’une étape vers le succès. Continue.'")
        print(Fore.MAGENTA + "Elle disparaît, laissant une clé en or.")
        fin_labyrinthe()
    elif choix == "3":
        print(Fore.RED + "\nLa silhouette murmure : 'La trahison peut venir de n’importe où. Reste vigilant.'")
        print(Fore.YELLOW + "Le miroir s’efface, et le chemin s’ouvre.")
        fin_labyrinthe()
    elif choix == "4":
        print(Fore.RED + "\nLa silhouette sourit tristement : 'La mort est inévitable, mais elle n’est pas la fin.'")
        print(Fore.MAGENTA + "Le miroir devient transparent, dévoilant une issue.")
        fin_labyrinthe()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        enigme_miroir()

def enigme_regrets():
    print(Fore.MAGENTA + "\nLa porte murmure : 'Quel regret hante ton esprit ?'")
    print(Fore.RED + "\n1. Une promesse non tenue.")
    print(Fore.RED + "2. Une opportunité manquée.")
    print(Fore.RED + "3. Une erreur qui a blessé un proche.")

    choix = input(Fore.WHITE + "Réponds à la porte (1/2/3) : ")

    if choix == "1":
        print(Fore.YELLOW + "\nLa porte s’ouvre lentement, comme si elle comprenait ta douleur.")
        fin_labyrinthe()
    elif choix == "2":
        print(Fore.CYAN + "\nLa porte grince, mais finit par s’ouvrir, révélant un escalier descendant.")
        fin_labyrinthe()
    elif choix == "3":
        print(Fore.RED + "\nLa porte murmure : 'Que feras-tu pour réparer cette erreur ?'")
        print(Fore.MAGENTA + "Tu réponds avec sincérité, et elle s’ouvre enfin.")
        fin_labyrinthe()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        enigme_regrets()

def enigme_coffre():
    print(Fore.MAGENTA + "\nLe coffre s’ouvre légèrement. À l’intérieur, tu trouves trois objets :")
    print(Fore.RED + "1. Une dague scintillante.")
    print(Fore.RED + "2. Un parchemin mystérieux.")
    print(Fore.RED + "3. Une amulette en or.")

    choix = input(Fore.WHITE + "Quel objet choisis-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.RED + "\nLa dague est piégée ! Une explosion secoue la pièce.")
        print(Fore.MAGENTA + "Max te tire juste à temps, mais vous devez fuir rapidement.")
        fin_labyrinthe()
    elif choix == "2":
        print(Fore.CYAN + "\nLe parchemin contient une carte du labyrinthe. Vous suivez les indications pour trouver la sortie.")
        fin_labyrinthe()
    elif choix == "3":
        print(Fore.YELLOW + "\nL’amulette brille intensément. Une porte secrète s’ouvre devant vous.")
        fin_labyrinthe()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        enigme_coffre()

def fin_labyrinthe():
    print(Fore.GREEN + "\nAprès avoir surmonté les épreuves, vous trouvez enfin la sortie du labyrinthe.")
    print(Fore.YELLOW + "Max soupire de soulagement : 'On l’a fait… mais qu’est-ce qui nous attend maintenant ?'")
    print(Fore.RED + "\nDevant vous se dresse un immense château, entouré d’un fossé rempli d’eau noire.")
    print(Fore.CYAN + "Une voix résonne depuis le château : 'Vous avez survécu au labyrinthe. Venez… si vous osez.'")
    print(Fore.RED + "\n**Partie 8 : Le Château des Ombres — En cours de développement...**")

# Lancer la Partie 7
labyrinthe_ames()
from colorama import Fore, Style, init
import random
init(autoreset=True)

def chateau_ombres():
    print(Fore.MAGENTA + "\nVous entrez dans le château. L’atmosphère est glaciale, et un silence oppressant règne.")
    print(Fore.YELLOW + "Des torches sur les murs vacillent, projetant des ombres dansantes autour de vous.")
    print(Fore.CYAN + "La voix mystérieuse résonne à nouveau : 'Trois épreuves t’attendent. Seul un esprit clair et un cœur courageux te permettront de survivre.'")

    print(Fore.RED + "\n1. S’approcher du trône au centre de la salle.")
    print(Fore.RED + "2. Explorer le couloir de droite.")
    print(Fore.RED + "3. Explorer le couloir de gauche.")

    choix = input(Fore.WHITE + "Que fais-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.MAGENTA + "\nTu t’approches du trône. Une silhouette spectrale y est assise, te fixant avec des yeux vides.")
        print(Fore.RED + "'Pour avancer, résous cette énigme :'")
        enigme_trone()
    elif choix == "2":
        print(Fore.CYAN + "\nTu explores le couloir de droite. Les murs sont couverts de peintures anciennes, mais leurs yeux semblent te suivre.")
        print(Fore.YELLOW + "Un coffre est posé à la fin du couloir.")
        enigme_coffre()
    elif choix == "3":
        print(Fore.YELLOW + "\nTu prends le couloir de gauche. Une série de pièges mécaniques est activée dès que tu entres.")
        print(Fore.RED + "Max crie : 'Attention !'")
        enigme_pieges()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        chateau_ombres()

def enigme_trone():
    print(Fore.MAGENTA + "\nLa silhouette te fixe et te pose une question :")
    print(Fore.RED + "'Je suis ce que tout le monde perd mais que personne ne peut retrouver. Qui suis-je ?'")
    print(Fore.RED + "\n1. Le temps.")
    print(Fore.RED + "2. La jeunesse.")
    print(Fore.RED + "3. L’innocence.")

    choix = input(Fore.WHITE + "Quelle est ta réponse (1/2/3) ? : ")

    if choix == "1":
        print(Fore.GREEN + "\nLa silhouette incline la tête : 'Correct. Le temps est irréversible.'")
        print(Fore.YELLOW + "Un passage secret s’ouvre derrière le trône.")
        suite_chateau()
    else:
        print(Fore.RED + "\nLa silhouette hurle : 'Mauvaise réponse !' Elle te projette une vague d’énergie sombre.")
        print(Fore.CYAN + "Max te sauve de justesse, mais vous êtes forcés de fuir.")
        chateau_ombres()

def enigme_coffre():
    print(Fore.MAGENTA + "\nLe coffre est piégé. Pour l’ouvrir, il faut résoudre un casse-tête.")
    print(Fore.RED + "'Un marchand a 7 sacs, chaque sac contient 7 chats. Combien de chats y a-t-il en tout ?'")
    print(Fore.RED + "\n1. 49.")
    print(Fore.RED + "2. 56.")
    print(Fore.RED + "3. 343.")

    choix = input(Fore.WHITE + "Quelle est ta réponse (1/2/3) ? : ")

    if choix == "3":
        print(Fore.GREEN + "\nLe coffre s’ouvre lentement. À l’intérieur, une clé brillante repose sur un coussin de velours.")
        print(Fore.YELLOW + "Tu prends la clé, et un nouveau passage s’ouvre.")
        suite_chateau()
    else:
        print(Fore.RED + "\nLe coffre explose en un nuage de fumée toxique. Tu es obligé de battre en retraite.")
        chateau_ombres()

def enigme_pieges():
    print(Fore.MAGENTA + "\nTu avances dans le couloir, esquivant des lames et des flèches."
          "À un moment donné, un mécanisme bloque la porte de sortie.")
    print(Fore.RED + "'Trois leviers sont devant toi. Seul l’un d’eux désactivera les pièges.'")
    print(Fore.RED + "\n1. Tirer le levier rouge.")
    print(Fore.RED + "2. Tirer le levier bleu.")
    print(Fore.RED + "3. Tirer le levier vert.")

    choix = input(Fore.WHITE + "Quel levier tires-tu (1/2/3) ? : ")

    if choix == "2":
        print(Fore.GREEN + "\nLes pièges s’arrêtent, et la porte s’ouvre lentement.")
        print(Fore.YELLOW + "Tu continues ton chemin.")
        suite_chateau()
    else:
        print(Fore.RED + "\nLe levier active un piège supplémentaire. Des lames surgissent du sol !")
        print(Fore.CYAN + "Max te tire en arrière à temps, mais vous devez repartir.")
        chateau_ombres()

def suite_chateau():
    print(Fore.MAGENTA + "\nAprès avoir réussi l’une des épreuves, vous accédez à une grande salle centrale.")
    print(Fore.YELLOW + "Au centre, une immense porte ornée de symboles anciens bloque le chemin.")
    print(Fore.CYAN + "La voix résonne à nouveau : 'Une dernière épreuve, et tu découvriras la vérité sur ce château.'")
    print(Fore.RED + "\n**Partie 9 : Le Gardien de la Vérité — En cours de développement...**")

# Lancer la Partie 8
chateau_ombres()
from colorama import Fore, Style, init
import random
init(autoreset=True)

def gardien_verite():
    print(Fore.MAGENTA + "\nLe Gardien de la Vérité se dresse devant toi, imposant et mystérieux.")
    print(Fore.YELLOW + "Il pointe une énorme lame vers toi et dit :")
    print(Fore.RED + "'Pour accéder à la vérité, tu dois triompher de trois défis : la mémoire, la logique et le combat.'")
    
    print(Fore.CYAN + "\n1. Affronter l’épreuve de la mémoire.")
    print(Fore.CYAN + "2. Affronter l’épreuve de la logique.")
    print(Fore.CYAN + "3. Affronter l’épreuve du combat.")

    choix = input(Fore.WHITE + "Quelle épreuve choisis-tu (1/2/3) ? : ")

    if choix == "1":
        print(Fore.YELLOW + "\nLe Gardien te fixe et dit : 'Concentre-toi, car les souvenirs peuvent te trahir.'")
        epreuve_memoire()
    elif choix == "2":
        print(Fore.YELLOW + "\nLe Gardien fait apparaître un grand échiquier magique. 'La logique est ta clé.'")
        epreuve_logique()
    elif choix == "3":
        print(Fore.YELLOW + "\nLe Gardien brandit son arme. 'Prépare-toi à combattre, mais sache que je ne retiendrai pas mes coups.'")
        epreuve_combat()
    else:
        print(Fore.RED + "\nChoix invalide, essaie à nouveau.")
        gardien_verite()

def epreuve_memoire():
    print(Fore.MAGENTA + "\nDes images apparaissent dans ton esprit, rapides et confuses.")
    print(Fore.YELLOW + "Le Gardien te demande : 'Souviens-toi des symboles que tu as vus dans le château. Donne-les dans le bon ordre.'")
    symbols = ["☀️", "🌙", "⭐", "🔥"]
    random.shuffle(symbols)

    print(Fore.CYAN + "\nLes symboles suivants apparaissent :")
    print(Fore.YELLOW + f"{' '.join(symbols)}")
    reponse = input(Fore.WHITE + "Ressaisis les symboles dans le bon ordre (séparés par un espace) : ")

    if reponse == "☀️ 🌙 ⭐ 🔥":
        print(Fore.GREEN + "\nLe Gardien incline la tête : 'Bien joué, ta mémoire est impressionnante.'")
        suite_gardien()
    else:
        print(Fore.RED + "\nLe Gardien secoue la tête : 'Tu as échoué.' Une onde de choc te projette en arrière.")
        print(Fore.CYAN + "Tu peux tenter une autre épreuve.")
        gardien_verite()

def epreuve_logique():
    print(Fore.MAGENTA + "\nLe Gardien te pose une énigme complexe :")
    print(Fore.YELLOW + "'Trois personnes entrent dans une pièce, chacune portant un chapeau. Un d’eux dit :")
    print(Fore.RED + "'Je vois deux chapeaux rouges devant moi.' Les autres disent la même chose.")
    print(Fore.YELLOW + "Quelle est la couleur des trois chapeaux ?'")
    print(Fore.RED + "\n1. Tous rouges.")
    print(Fore.RED + "2. Deux rouges et un bleu.")
    print(Fore.RED + "3. Tous bleus.")

    choix = input(Fore.WHITE + "Quelle est ta réponse (1/2/3) ? : ")

    if choix == "1":
        print(Fore.GREEN + "\nLe Gardien sourit légèrement : 'La logique te guide bien.'")
        suite_gardien()
    else:
        print(Fore.RED + "\nLe Gardien secoue la tête : 'Faux. Réfléchis mieux.'")
        print(Fore.CYAN + "Tu peux tenter une autre épreuve.")
        gardien_verite()

def epreuve_combat():
    print(Fore.RED + "\nLe Gardien lève son arme, et une aura sombre remplit la salle.")
    print(Fore.YELLOW + "Le combat commence. Tu dois survivre trois rounds !")

    player_hp = 50
    gardien_hp = 70

    while player_hp > 0 and gardien_hp > 0:
        print(Fore.CYAN + f"\nTes PV : {player_hp} | PV du Gardien : {gardien_hp}")
        print(Fore.RED + "1. Attaquer.")
        print(Fore.YELLOW + "2. Esquiver.")
        print(Fore.BLUE + "3. Utiliser un objet (Potion de soin).")

        choix = input(Fore.WHITE + "Que fais-tu ? : ")

        if choix == "1":
            damage = random.randint(10, 20)
            gardien_hp -= damage
            print(Fore.GREEN + f"\nTu infliges {damage} points de dégâts au Gardien.")
        elif choix == "2":
            print(Fore.YELLOW + "\nTu esquives l’attaque du Gardien.")
            continue
        elif choix == "3":
            heal = random.randint(10, 20)
            player_hp += heal
            print(Fore.GREEN + f"\nTu récupères {heal} PV.")
        else:
            print(Fore.RED + "\nChoix invalide, le Gardien profite de ton hésitation.")
            player_hp -= random.randint(5, 15)

        # Contre-attaque du Gardien
        damage = random.randint(10, 15)
        player_hp -= damage
        print(Fore.RED + f"\nLe Gardien t’attaque et inflige {damage} points de dégâts.")

    if player_hp > 0:
        print(Fore.GREEN + "\nTu as triomphé du Gardien ! Il s’incline devant toi.")
        suite_gardien()
    else:
        print(Fore.RED + "\nTu as échoué. Le Gardien te repousse avec violence.")
        print(Fore.CYAN + "Tu peux retenter une autre épreuve.")
        gardien_verite()

def suite_gardien():
    print(Fore.MAGENTA + "\nLe Gardien recule et te montre une porte ornée de runes dorées.")
    print(Fore.YELLOW + "Il te dit : 'La vérité se trouve derrière cette porte. Mais es-tu prêt à l’entendre ?'")
    print(Fore.CYAN + "\n**Partie 10 : La Vérité — En cours de développement...**")

# Lancer la Partie 9
gardien_verite()
from colorama import Fore, Style, init
import random
init(autoreset=True)

def confrontation_finale():
    print(Fore.RED + "\nLa lumière de la salle s'assombrit alors que ton double maléfique te fixe.")
    print(Fore.MAGENTA + "Il te propose deux choix :")
    print(Fore.YELLOW + "\n1. Toucher le cristal noir pour découvrir la vérité.")
    print(Fore.YELLOW + "2. Refuser la vérité et affronter ton double en duel.")

    choix = input(Fore.WHITE + "\nQue choisis-tu (1/2) ? : ")

    if choix == "1":
        decouvrir_verite()
    elif choix == "2":
        duel_final()
    else:
        print(Fore.RED + "\nChoix invalide, le cristal pulse dangereusement. Essaie à nouveau.")
        confrontation_finale()

def decouvrir_verite():
    print(Fore.CYAN + "\nTu tends la main vers le cristal noir. Dès que tu le touches, une vague de douleur traverse ton esprit.")
    print(Fore.YELLOW + "Des visions surgissent, brouillant la réalité et révélant l’histoire oubliée de ce château.")
    print(Fore.GREEN + """
    Tu apprends que le château était autrefois un sanctuaire, un lieu où les vérités universelles étaient protégées.
    Mais une force maléfique a corrompu ses gardiens, les transformant en monstres.
    Cette force est liée à toi, car tu es le descendant d'un ancien gardien ayant trahi ses pairs.
    """)
    print(Fore.RED + "\nLa voix de ton double résonne :")
    print(Fore.RED + "'La vérité est un fardeau, et maintenant tu dois vivre avec ce poids. Ce monde compte sur toi pour le restaurer.'")
    print(Fore.MAGENTA + "\nTu tombes à genoux, accablé par cette révélation, mais une nouvelle force naît en toi.")
    print(Fore.CYAN + "\n**Partie 11 : Les Ruines Perdues — En cours de développement...**")
    exit()

def duel_final():
    print(Fore.RED + "\nTon double maléfique éclate de rire et se prépare à te combattre.")
    print(Fore.YELLOW + "Il te dit : 'Très bien, prouve-moi que tu es digne de survivre à cette vérité.'")
    
    # Initialisation des statistiques
    player_hp = 60
    double_hp = 80

    while player_hp > 0 and double_hp > 0:
        print(Fore.CYAN + f"\nTes PV : {player_hp} | PV de ton double : {double_hp}")
        print(Fore.RED + "1. Attaquer.")
        print(Fore.YELLOW + "2. Esquiver.")
        print(Fore.BLUE + "3. Utiliser un objet (Potion de soin).")

        choix = input(Fore.WHITE + "Que fais-tu ? : ")

        if choix == "1":
            damage = random.randint(15, 25)
            double_hp -= damage
            print(Fore.GREEN + f"\nTu infliges {damage} points de dégâts à ton double.")
        elif choix == "2":
            print(Fore.YELLOW + "\nTu esquives l'attaque de ton double.")
            continue
        elif choix == "3":
            heal = random.randint(10, 20)
            player_hp += heal
            print(Fore.GREEN + f"\nTu récupères {heal} PV.")
        else:
            print(Fore.RED + "\nChoix invalide, ton double en profite pour attaquer.")
            player_hp -= random.randint(5, 15)

        # Contre-attaque de ton double
        damage = random.randint(15, 20)
        player_hp -= damage
        print(Fore.RED + f"\nTon double t'attaque et inflige {damage} points de dégâts.")

    if player_hp > 0:
        print(Fore.GREEN + "\nTu as triomphé de ton double maléfique. Il s’incline avant de disparaître dans une fumée noire.")
        print(Fore.MAGENTA + "\nUne porte secrète s’ouvre, te conduisant plus loin dans le château.")
        print(Fore.CYAN + "\n**Partie 11 : Les Ruines Perdues — En cours de développement...**")
    else:
        print(Fore.RED + "\nTu as échoué, et ton double te consume entièrement.")
        print(Fore.CYAN + "Tu peux retenter le combat.")
        duel_final()

# Lancer la Partie 10
confrontation_finale()