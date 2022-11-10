
# Import des librairies

import pygame
import random

# Initialisation de Pygame

pygame.init()

pygame.display.set_caption("Roulette Casino")
screen = pygame.display.set_mode((720, 480))

# Import des images

background = pygame.image.load("assets/background.png")
rulesPNG = pygame.image.load("assets/rules.png")
launchPNG = pygame.image.load("assets/launch.png")
logoPNG = pygame.image.load("assets/logo.png")

rulesWritePNG = pygame.image.load("assets/rulesWrite.png")
returnButtonPNG = pygame.image.load("assets/return_button.png")

enterButtonPNG = pygame.image.load("assets/enter_button.png")
walletConsignPNG = pygame.image.load("assets/walletConsign.png")
miseConsignPNG = pygame.image.load("assets/miseConsign.png")
setConsignPNG = pygame.image.load("assets/setConsign.png")
setOptionsPNG = pygame.image.load("assets/setOptions.png")

tier1 = pygame.image.load("assets/tier1.png")
tier2 = pygame.image.load("assets/tier2.png")
tier3 = pygame.image.load("assets/tier3.png")

pair = pygame.image.load("assets/pair.png")
impair = pygame.image.load("assets/impair.png")
manque = pygame.image.load("assets/manque.png")
passe = pygame.image.load("assets/passe.png")

playWin = pygame.image.load("assets/playWin.png")
playLoose = pygame.image.load("assets/playLoose.png")
playSimple = pygame.image.load("assets/playSimple.png")
playMultiple = pygame.image.load("assets/playMultiple.png")

checkMark = pygame.image.load("assets/checkMark.png")
continueSet = pygame.image.load("assets/continueSet.png")
checkMarkT = pygame.transform.scale(checkMark, (40, 40))
checkMarkH = pygame.transform.scale(checkMark, (31, 31))

walletAnnonce = pygame.image.load("assets/walletAnnonce.png")
continueRestart = pygame.image.load("assets/continueRestart.png")
restartRestart = pygame.image.load("assets/restartRestart.png")

# Import et initialisation des polices

myFont = pygame.font.Font("assets/myFont.ttf", 35)
font = pygame.font.SysFont(None, 60)

# Initialisation des listes et variables

terms = []
pairList = []
impairList = []
manqueList = []
passeList = []
tier1List = []
tier2List = []
tier3List = []

for i in range(37):
    if i%2 == 0 and i >= 2: pairList.append(i)
    elif i != 0: impairList.append(i)

    if i >= 1 and i <= 18: manqueList.append(i)
    elif i != 0: passeList.append(i)

    if i <= 16: tier1List.append(i)
    elif i > 16 and i <= 28: tier2List.append(i)
    else: tier3List.append(i)

running = True
status = "main"

# Creation d'une fonction verifiant un click

def click(surface):
    return surface.collidepoint(pygame.mouse.get_pos())

# Commencement du jeu

while running:

    # Afficher le fond

    screen.blit(background, (0, 0))

    # Debut de l'etape "main"
    if status == "main":
    
        # Initialisation des variables
        jail = 0
        play = False

        txtWallet = ""
        walletFocus = False

        txtMise = ""
        miseFocus = False

        txtSet = ""
        setFocus = False

        checkTier1 = False
        checkTier2 = False
        checkTier3 = False

        checkPair = False
        checkImpair = False
        checkManque = False
        checkPasse = False
        
        # Affichage des elements
        font = pygame.font.SysFont(None, 15)
        signature = font.render("By Jason Coulais Léo", True, (255,255,255))
        screen.blit(signature, (360-(signature.get_rect().size.__getitem__(0))/2, 470-signature.get_rect().size.__getitem__(1)))
        font = pygame.font.SysFont(None, 60)
        screen.blit(launchPNG, (120, 240))
        screen.blit(rulesPNG, (180, 360))
        screen.blit(logoPNG, (160, 25))

        # Initialisation des bordures des elements cliquables
        rulesRect = rulesPNG.get_rect()
        rulesRect.x = 180
        rulesRect.y = 360

        launchRect = launchPNG.get_rect()
        launchRect.x = 120
        launchRect.y = 240

        logoRect = logoPNG.get_rect()
        logoRect.x = 160
        logoRect.y = 25

    # Debut de l'etape "rules"
    elif status == "rules":
        # Affichage des elements
        screen.blit(rulesWritePNG, (0, 0))
        screen.blit(returnButtonPNG, (680, 440))

        # Initialisation des bordures des elements cliquables
        returnRulesRect = rulesPNG.get_rect()
        returnRulesRect.x = 680
        returnRulesRect.y = 440

    # Debut de l'etape "wallet"
    elif status == "wallet":
        # Affichage des elements
        walletRect = pygame.draw.rect(screen, pygame.Color(255, 255, 255), (180, 275, 360, 55))
        screen.blit(enterButtonPNG, (545, 275))
        screen.blit(walletConsignPNG, (162.5, 50))

        # Initialisation des bordures de l'element cliquable
        enterWalletRect = enterButtonPNG.get_rect()
        enterWalletRect.x = 545
        enterWalletRect.y = 275

        # Affichage du texte de l'input
        textPrint = font.render(txtWallet, True, (0,0,0))
        screen.blit(textPrint, (360-(textPrint.get_rect().size.__getitem__(0))/2, 283))

        # Si le focus est sur l'input (input est cliqué), faire clignoter la barre d'entrée et la deplacer si necessaire
        if walletFocus:
            ticks = (pygame.time.get_ticks()%1000) + 1
            if ticks > 500: pygame.draw.line(screen, pygame.Color(0, 0, 0), (360+(textPrint.get_rect().size.__getitem__(0))/2, 283), (360+(textPrint.get_rect().size.__getitem__(0))/2, 323), 2)

     # Debut de l'etape "mise"
    elif status == "mise":
        # Affichage des elements
        font = pygame.font.SysFont(None, 60)
        miseRect = pygame.draw.rect(screen, pygame.Color(255, 255, 255), (180, 275, 360, 55))
        screen.blit(enterButtonPNG, (545, 275))
        screen.blit(miseConsignPNG, (162.5, 50))

        # Initialisation des bordures de l'element cliquable
        enterMiseRect = enterButtonPNG.get_rect()
        enterMiseRect.x = 545
        enterMiseRect.y = 275

        # Affichage du texte de l'input
        textPrint = font.render(txtMise, True, (0,0,0))
        screen.blit(textPrint, (360-(textPrint.get_rect().size.__getitem__(0))/2, 283))

        # Si le focus est sur l'input (input est cliqué), faire clignoter la barre d'entrée et la deplacer si necessaire
        if miseFocus:
            ticks = (pygame.time.get_ticks()%1000) + 1
            if ticks > 500: pygame.draw.line(screen, pygame.Color(0, 0, 0), (360+(textPrint.get_rect().size.__getitem__(0))/2, 283), (360+(textPrint.get_rect().size.__getitem__(0))/2, 323), 2)

     # Debut de l'etape "set"
    elif status == "set":
        # Affichage des elements
        screen.blit(setConsignPNG, (162.5, 0))
        screen.blit(setOptionsPNG, (0, 192))
        screen.blit(continueSet, (240, 421))

        screen.blit(tier1, (27, 253))
        screen.blit(tier2, (27, 300))
        screen.blit(tier3, (27, 347))

        screen.blit(pair, (288, 263))
        screen.blit(impair, (288, 300))
        screen.blit(manque, (288, 337))
        screen.blit(passe, (288, 374))

        font = pygame.font.SysFont(None, 36)
        setRect = pygame.draw.rect(screen, pygame.Color(224, 224, 224), (528, 275, 138, 55))
        textPrint = font.render(txtSet, True, (0,0,0))

        # Initialisation des bordures de l'element cliquable
        continueSetRect = continueSet.get_rect()
        continueSetRect.x = 240
        continueSetRect.y = 421

        tier1Rect = tier1.get_rect()
        tier1Rect.x = 27
        tier1Rect.y = 253

        tier2Rect = tier2.get_rect()
        tier2Rect.x = 27
        tier2Rect.y = 300

        tier3Rect = tier3.get_rect()
        tier3Rect.x = 27
        tier3Rect.y = 347

        pairRect = pair.get_rect()
        pairRect.x = 288
        pairRect.y = 263

        impairRect = impair.get_rect()
        impairRect.x = 288
        impairRect.y = 300

        manqueRect = manque.get_rect()
        manqueRect.x = 288
        manqueRect.y = 337

        passeRect = passe.get_rect()
        passeRect.x = 288
        passeRect.y = 374

        # Change l'etat si cliqué
        if(checkTier1): screen.blit(checkMarkT, (108, 255))
        if(checkTier2): screen.blit(checkMarkT, (108, 302))
        if(checkTier3): screen.blit(checkMarkT, (108, 349))

        if(checkPair): screen.blit(checkMarkH, (349, 265))
        if(checkImpair): screen.blit(checkMarkH, (349, 302))
        if(checkManque): screen.blit(checkMarkH, (349, 339))
        if(checkPasse): screen.blit(checkMarkH, (349, 374))


        # Si un nombre est déjà entré, supprimer le doublon, et si la chaine finie par une virgule, la supprimer
        if not setFocus:
            if len(terms) == 2:
                if terms[1] == terms[0]:
                    txtSet = txtSet[:-len(terms[1])]
                    terms.pop()
            elif len(terms) == 3:
                if terms[2] == terms[1] or terms[2] == terms[0]:
                    txtSet = txtSet[:-len(terms[2])]
                    terms.pop()
            elif len(terms) == 4:
                if terms[3] == terms[2] or terms[3] == terms[1] or terms[3] == terms[0]:
                    txtSet = txtSet[:-len(terms[3])]
                    terms.pop()

            if txtSet.endswith(","): txtSet = txtSet[:-1]
        
        # Si le focus est sur l'input (input est cliqué), faire clignoter la barre d'entrée et la deplacer si necessaire
        else:
            ticks = (pygame.time.get_ticks()%1000) + 1
            if ticks > 500: pygame.draw.line(screen, pygame.Color(0, 0, 0), (598+(textPrint.get_rect().size.__getitem__(0))/2, 283), (598+(textPrint.get_rect().size.__getitem__(0))/2, 323), 2)
        
        screen.blit(textPrint, (598-(textPrint.get_rect().size.__getitem__(0))/2, 288))

     # Debut de l'etape "play"
    elif status == "play":

        # Changer la taille de la police
        myFont = pygame.font.Font("assets/myFont.ttf", 48)

        # Se lance si c'est la première fois qu'il est lancé (eviter une generation de nombres en boucle)
        if not play:
            gain = 0
            zeroChance = "0"
            n = random.randint(0, 36)

            # Si l'input de l'etape precedente n'est pas vide (donc que le joueur a choisi des nombres) et que le nombre generer
            # fait parti des nombres, attribuer le gain associé
            if txtSet != "":
                if str(n) in terms:
                    if len(terms) == 1: gain = 37*int(txtMise)
                    if len(terms) == 2: gain = 18*int(txtMise)
                    if len(terms) == 3: gain = 12*int(txtMise)
                    if len(terms) == 4: gain = 9*int(txtMise)
            
            # Verifier combien de tiers sont choisis et que le nombre generer fait parti des tiers, puis donner (ou non) le gain associé
            elif checkTier2 and ((checkTier1 and n in tier1List) or (checkTier3 and n in tier3List) or n in tier2List): gain = 1.5*int(txtMise)
            elif (checkTier1 and n in tier1List) or (checkTier2 and n in tier2List) or (checkTier3 and n in tier3List): gain = 3*int(txtMise)

            # Verifier si le nombre generer fait parti des moitiés choisis par le joueur, et si oui, donner le gain associé
            if (checkPair and n in pairList) or (checkImpair and n in impairList) or (checkManque and n in manqueList) or (checkPasse and n in passeList): gain = 2*int(txtMise)

            # Assigner a la variable zeroChance la valeur necessaire, selon si le joueur a tenté une chance Simple où Multiple
            # et si le zéro est tiré
            if (checkPair or checkImpair or checkManque or checkPasse) and n == 0: zeroChance = "simple"
            if (checkTier1 or checkTier2 or checkTier3) and n == 0: zeroChance = "multiple"

            # Empecher d'avoir un entier exprimé en nombre a virgule (ex: 2 ecrit 2.0)
            rewardMultiplicator = gain/int(txtMise) - 1
            if rewardMultiplicator == int(gain/int(txtMise) - 1): rewardMultiplicator = int(gain/int(txtMise) - 1)

        # Creer les textes qui afficheront le gain et le nombre générer par la roulette
        txtPlay = myFont.render(str(rewardMultiplicator), True, (0,0,0))
        playRoulette = myFont.render(str(n), True, (0,0,0))

        # Creer le texte qui affichera le choix du joueur, selon la où les options selectionnées precedemment
        if checkPair:
            playChoice = myFont.render("Nombres pairs", True, (0,0,0))
        elif checkImpair:
            playChoice = myFont.render("Nombres impairs", True, (0,0,0))
        elif checkManque:
            playChoice = myFont.render("Manque: 1-18", True, (0,0,0))
        elif checkPasse:
            playChoice = myFont.render("Passe: 19-36", True, (0,0,0))
        elif checkTier1:
            if checkTier2: playChoice = myFont.render("Tier 1 et Tier 2: 0-28", True, (0,0,0))
            else: playChoice = myFont.render("Tier 1: 0-16", True, (0,0,0))
        elif checkTier3:
            if checkTier2: playChoice = myFont.render("Tier 2 et Tier 3: 17-36", True, (0,0,0))
            else: playChoice = myFont.render("Tier 3: 29-36", True, (0,0,0))
        elif checkTier2: playChoice = myFont.render("Tier 2: 17-28", True, (0,0,0))
        else:
            txt = ""
            for i in range(len(terms)):
                txt+=terms[i]
                if i != len(terms) - 1: txt+=", "
            playChoice = myFont.render(txt, True, (0,0,0))
        
        # Verifier si la règle du zéro doit être appliquée
        if zeroChance == "0":
            # Vider la prison si le joueur perd
            if gain == 0: jail=0
            # Si la boucle a déjà été executée precedemment, ne pas redonner le gain (et la valeur de la prison si existante)
            if not play: txtWallet = str(int(txtWallet) + gain + jail)
            # Si le gain n'est pas nul (donc que le joueur a gagné) afficher l'image de succès et le gain, sinon, afficher l'image d'echec
            if gain != 0:
                screen.blit(playWin,(0,0))
                screen.blit(txtPlay, (515-(txtPlay.get_rect().size.__getitem__(0))/2, 315))
            else:
                screen.blit(playLoose, (0,0))

        # Si le joueur a jouer une chance simple, ajouter le gain a la prison
        elif zeroChance == "simple":
            screen.blit(playSimple, (0,0))
            if not play: jail+=int(txtMise)

        elif zeroChance == "multiple":
            jail=0
            screen.blit(playMultiple, (0,0))

        myFont = pygame.font.Font("assets/myFont.ttf", 30)

        # Afficher le choix du joueur, le resultat de la roulette le bouton enter
        
        screen.blit(playChoice, (360-(playChoice.get_rect().size.__getitem__(0))/2, 155))
        screen.blit(playRoulette, (360-(playRoulette.get_rect().size.__getitem__(0))/2, 265))
        screen.blit(enterButtonPNG, (565, 400))

        # Initialiser les bordures du bouton enter
        playRect = enterButtonPNG.get_rect()
        playRect.x = 565
        playRect.y = 400

        # Specifier que la boucle a été joué
        play = True

     # Debut de l'etape "restart"
    elif status == "restart":
    
        # Initialisation des variables
        play = False
        walletFocus = False

        txtMise = ""
        miseFocus = False

        txtSet = ""
        setFocus = False

        checkTier1 = False
        checkTier2 = False
        checkTier3 = False

        checkPair = False
        checkImpair = False
        checkManque = False
        checkPasse = False
        
        # Affichage des elements
        screen.blit(continueRestart, (180, 230))
        screen.blit(restartRestart, (180, 355))
        screen.blit(walletAnnonce, (180, 60))

        # Initialisation des bordures des elements cliquables
        continueRect = continueRestart.get_rect()
        continueRect.x = 180
        continueRect.y = 230

        restartRect = restartRestart.get_rect()
        restartRect.x = 180
        restartRect.y = 355

        # Si le portefeuille est vide, rendre transparent le bouton continuer
        if txtWallet == "0": continueRestart.set_alpha(120)

        # Attribuer la prochaine valeur de la taille de la police, selon le contenu du porte-feuille rentre dans le cadre
        size = 35
        if len(txtWallet) >=14: size = int(525/(len(txtWallet) + 1))
        myFont = pygame.font.Font("assets/myFont.ttf", size)

        # Afficher le contenu du portefeuille
        txt = myFont.render(txtWallet + "€", True, (0,0,0))
        screen.blit(txt, (360-(txt.get_rect().size.__getitem__(0))/2, 108))

    # Click on logo...
    elif status == "rick?":
        i = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
            if not running: break
            IMG = pygame.image.load("assets/rick/frame_" + str(i) + ".png")
            screen.blit(IMG, (40, 0))
            pygame.display.flip()
            pygame.time.wait(20)
            i = (i+1)%147

    pygame.display.flip()

    # Verifier les evenements
    for event in pygame.event.get():

        # Evenements durant l'etape "main"
        if status == "main" and event.type == pygame.MOUSEBUTTONDOWN:
            # Changer d'etape selon le bouton cliqué
            if click(rulesRect): status = "rules"
            elif click(launchRect): status = "wallet"
            elif click(logoRect): status = "rick?"

        # Evenements durant l'etape "rules": si le bouton retour est cliqué, passer a l'etape "main"
        elif status == "rules" and event.type == pygame.MOUSEBUTTONDOWN and click(returnRulesRect): status = "main"
               
        # Evenements durant l'etape "wallet"
        elif status == "wallet":
            # Si l'evenement est un clic, executer
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # Changer l'etat de l'input selon où le joueur clique
                if click(walletRect): walletFocus = True
                elif not click(walletRect): walletFocus = False
                # Si l'input n'est pas vide, egal a zéro et que le joueur clique sur le bouton entrer, passer a l'etape "mise"
                if click(enterWalletRect) and len(txtWallet) != 0 and txtWallet != "0": status = "mise"

            # Si l'input est focus, executer
            if walletFocus:
                # Si un caractère est rentré est que c'est le bouton backspace, effacer le dernier caractère, si c'est un chiffre, l'ajouter
                # a la chaine de caractère
                key = ""
                if event.type == 768: key = event.__dict__.get("unicode")
                if key == "\x08" and len(txtWallet) != 0: txtWallet = txtWallet[:-1]
                if key.isdigit() and not len(txtWallet) >= 15: txtWallet+=key

        # Evenements durant l'etape "mise"
        elif status == "mise":
            # Si l'evenement est un clic, executer
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Changer l'etat de l'input selon où le joueur clique
                if click(miseRect): miseFocus = True
                elif not click(miseRect): miseFocus = False

                # Si l'input n'est pas vide, egal a zéro et que le joueur clique sur le bouton entrer, passer a l'etape "set"
                # et soustraire la mise au porte-feuille
                if click(enterMiseRect) and len(txtMise) != 0 and txtMise != "0": 
                    txtWallet = str(int(txtWallet) - int(txtMise))
                    status = "set"

            if miseFocus:
                # Si un caractère est rentré est que c'est le bouton backspace, effacer le dernier caractère, si c'est un chiffre, l'ajouter
                # a la chaine de caractère, a condition que cela ne fait pas passer la valeur de la mise au dessus de celle du porte-feuille
                key = ""
                if event.type == 768: key = event.__dict__.get("unicode")
                if key == "\x08" and len(txtMise) != 0: txtMise = txtMise[:-1]
                if key.isdigit() and not len(txtMise) >= 15 and int(txtMise + key) <= int(txtWallet) : txtMise+=key

        # Evenements durant l'etape "set"
        elif status == "set":
            # Si l'evenement est un click, executer
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Si le bouton continuer est cliqué et qu'au moins une option est choisie par le joueur, passer a l'etape "play"
                if click(continueSetRect) and (txtSet != "" or checkTier1 or checkTier2 or checkTier3 or checkPair or checkImpair or checkManque or checkPasse): status = "play"

                # Changer l'etat de l'input selon où le joueur clique
                if click(setRect): setFocus = True
                elif not click(setRect): setFocus = False

                # Si le bouton tier1 est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples
                # et l'input, et si tier3 est déjà coché, ne pas coché tier1
                if click(tier1Rect):

                    checkPair = False
                    checkImpair = False
                    checkManque = False
                    checkPasse = False
                    
                    txtSet = ""

                    if checkTier1: checkTier1 = False
                    elif not checkTier3: checkTier1 = True

                # Si le bouton tier1 est cliqué, changer l'etat du bouton, supprimer les checks presentes sur les chances simples et l'input
                elif click(tier2Rect):

                    checkPair = False
                    checkImpair = False
                    checkManque = False
                    checkPasse = False
                    
                    txtSet = ""

                    checkTier2 = not checkTier2

                # Si le bouton tier3 est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples
                # et l'input, et si tier1 est déjà coché, ne pas coché tier3
                elif click(tier3Rect):

                    checkPair = False
                    checkImpair = False
                    checkManque = False
                    checkPasse = False
                    
                    txtSet = ""

                    if checkTier3: checkTier3 = False
                    elif not checkTier1: checkTier3 = True

                # Si le bouton pair est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples,l'input
                # et les autres chances multiples
                if click(pairRect):

                    checkTier1 = False
                    checkTier2 = False
                    checkTier3 = False
                    txtSet = ""

                    checkPair = not checkPair
                    checkImpair = False
                    checkManque = False
                    checkPasse = False                       

                # Si le bouton impair est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples,l'input
                # et les autres chances multiples
                elif click(impairRect):

                    checkTier1 = False
                    checkTier2 = False
                    checkTier3 = False
                    txtSet = ""

                    checkPair = False
                    checkImpair = not checkImpair
                    checkManque = False
                    checkPasse = False                        

                # Si le bouton manque est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples,l'input
                # et les autres chances multiples
                elif click(manqueRect):

                    checkTier1 = False
                    checkTier2 = False
                    checkTier3 = False
                    txtSet = ""

                    checkPair = False
                    checkImpair = False
                    checkManque = not checkManque
                    checkPasse = False                       

                # Si le bouton passe est cliqué, changer l'etat du bouton, supprimer les checks presents sur les chances simples,l'input
                # et les autres chances multiples
                elif click(passeRect):

                    checkTier1 = False
                    checkTier2 = False
                    checkTier3 = False
                    txtSet = ""

                    checkPair = False
                    checkImpair = False
                    checkManque = False
                    checkPasse = not checkPasse                

            # Si l'input est focus, executer
            if setFocus:

                # Supprimer tous les checks marks
                checkTier1 = False
                checkTier2 = False
                checkTier3 = False

                checkPair = False
                checkPasse = False
                checkManque = False
                checkPasse = False
                
                # Verifier que l'evenement est une entrée de caractère, et si c'est un backspace, supprimer le dernier caractère
                key = ""
                if event.type == 768: key = event.__dict__.get("unicode")
                if key == "\x08" and len(txtSet) != 0: txtSet = txtSet[:-1]

                # Assigner a la variable terms les differents nombres rentrés
                terms = txtSet.split(",")

                # Si la chaine de caractère ne depasse pas 12 caractères, executer
                if not (len(txtSet) > 12):
                    # Pour toutes les valeurs entrées, ne pas autoriser l'ecriture si deux nombres egaux sont rentrés
                    # et s'assurer que les nombres rentrés ne sont pas superieurs a 36
                    if len(terms) == 0:
                        if key.isdigit(): txtSet+=key

                    elif len(terms) == 1:
                        if key.isdigit() and not int(terms[0] + key) > 36: txtSet+=key
                        elif key == "," and terms[len(terms) - 1]: txtSet+=key

                    elif len(terms) == 2:
                        if key.isdigit() and not int(terms[1] + key) > 36: txtSet+=key
                        elif key == "," and terms[len(terms) - 1] and (terms[1] != terms[0]): txtSet+=key
                    
                    elif len(terms) == 3:
                        if key.isdigit() and not int(terms[2] + key) > 36: txtSet+=key
                        elif key == "," and terms[len(terms) - 1] and (terms[2] != terms[1] or terms[2] != terms[0]): txtSet+=key

                    elif len(terms) == 4 and len(terms) != 5:
                        if key.isdigit() and not int(terms[3] + key) > 36: txtSet+=key

        # Evenements durant l'etape "play": si le bouton enter est cliqué, passer a l'etape "restart"
        elif status == "play" and event.type == pygame.MOUSEBUTTONDOWN and click(playRect): status = "restart"
        
        # Evenements durant l'etape "restart"
        elif status == "restart" and event.type == pygame.MOUSEBUTTONDOWN:
            # Si le porte-feuille est a zéro, empecher le joueur de continuer (vu qu'il ne pourra pas)
            # Si le joueur clique sur continuer, passer a l'etape "mise"
            if click(continueRect) and txtWallet != "0": status = "mise"
            # Si le joueur clique sur rejouer, passer a l'etape "main"
            elif click(restartRect): status = "main"

        if event.type == pygame.QUIT:
            running = False
