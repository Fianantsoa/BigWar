import pygame
import random

colorGreen = (48, 138, 92)
colorBlue = (99, 110, 126)
#fonction pour avoir les coordonnées des élements selon leur clan
def position(axe, groupe):
    if groupe == "vert":
        i = 0
        listPos = []
        while i < 7:
            if axe == "x":
                pos = random.randint(0, 10)
            if axe == "y":
                pos = random.randint(1, 12)
            if pos in listPos:
                continue
            else:
                listPos.append(pos*50)
                i = i + 1
    if groupe == "bleu":
        i = 0
        listPos = []
        while i < 7:
            if axe == "x":
                pos = random.randint(13, 23)
            if axe == "y":
                pos = random.randint(1, 12)
            if pos in listPos:
                continue
            else:
                listPos.append(pos*50)
                i = i + 1
    return listPos

#fonction qui appelle les armées vert et qui le place sur les positions déja choisis
def callObjetGreen(groupe, positionsXG, positionsYG):
    screen.blit(groupe.green_plane, (positionsXG[0], positionsYG[0]))
    screen.blit(groupe.green_truck1, (positionsXG[1], positionsYG[1]))
    screen.blit(groupe.green_truck2, (positionsXG[2], positionsYG[2]))
    screen.blit(groupe.green_truck3, (positionsXG[3], positionsYG[3]))
    screen.blit(groupe.green_truck4, (positionsXG[4], positionsYG[4]))
    screen.blit(groupe.char_vert1, (positionsXG[5], positionsYG[5]))
    screen.blit(groupe.char_vert2, (positionsXG[6], positionsYG[6]))
#fonction qui appelle les armées bleu et qui le place sur les positions déja choisis
def callObjetBlue(groupe, positionsXB, positionsYB):
    screen.blit(groupe.plane_blue, (positionsXB[0], positionsYB[0]))
    screen.blit(groupe.truck_blue1, (positionsXB[1], positionsYB[1]))
    screen.blit(groupe.truck_blue2, (positionsXB[2], positionsYB[2]))
    screen.blit(groupe.truck_blue3, (positionsXB[3], positionsYB[3]))
    screen.blit(groupe.truck_blue4, (positionsXB[4], positionsYB[4]))
    screen.blit(groupe.char_bleu1, (positionsXB[5], positionsYB[5]))
    screen.blit(groupe.char_bleu2, (positionsXB[6], positionsYB[6]))

#fonction qui place des nuages sur tous les terrain sauf quand une élement est déjà trouvé
def Cloud(deleteX, deleteY, band):
    if band == "green":
        x = 0
        while x != 600:
            y = 50
            while y != 650:
                j = 0
                istrue = False
                while j != len(deleteX):
                    if (x == deleteX[j]) and (y == deleteY[j]):
                        istrue = True
                        y += 50
                        continue
                    j += 1
                if istrue == False:
                    screen.blit(cloud, (x, y))
                    y += 50
            x += 50
    if band == "blue":
        x = 650
        while x != 1250:
            y = 50
            while y != 650:
                j = 0
                true = False
                while j != len(deleteX):
                    if (x == deleteX[j]) and (y == deleteY[j]):
                        true = True
                        y += 50
                        continue
                    j += 1
                if true == False:
                    screen.blit(cloud, (x, y))
                    y += 50
            x += 50
#fonction qui met le score de chacun
def score(band, score1):
    if band == "green":
        pygame.draw.rect(screen, colorGreen, (0, 0, 150, 50))
        scoreOfGreen = font.render("Degat : %d" %score1, 1, (0, 0, 0))
        screen.blit(scoreOfGreen, (10, 5))
    if band == "blue":
        pygame.draw.rect(screen, colorBlue, (1100, 0, 150, 50))
        scoreOfGreen = font.render("%d : Degat" %score1, 1, (0, 0, 0))
        screen.blit(scoreOfGreen, (1110, 5))
#fonction qui compte le nombre de position exacte des élements de chaque côté pour gagner
def compteurPosition(table1, table2):
    table3 = []
    table4 = []
    compter1 = 0
    numberEle = 0
    while compter1 != len(table1):
        compter2 = 0
        while compter2 < len(table3):
            if table1[compter1] == table3[compter2] and \
            table2[compter1] == table4[compter2]:
                numberEle -= 1
                compter2 += 1
                continue
            compter2 += 1
        table3.append(table1[compter1])
        table4.append(table2[compter1])
        compter1 += 1
        numberEle += 1
    return numberEle
#fonction qui retourne le vainqueur
def Winner(winner):
    if winner == "Vert":
        pygame.draw.rect(screen, colorGreen, (475, 200, 300, 200))
        print = fontWinner.render("Gagnant ", 1, (0, 0, 0))
        printGagnant = fontWinner.render(winner, 1, (0, 0, 0))
    if winner == "Bleu":
        pygame.draw.rect(screen, colorBlue, (475, 200, 300, 200))
        print = fontWinner.render("Gagnant ", 1, (0, 0, 0))
        printGagnant = fontWinner.render(winner, 1, (0, 0, 0))
    screen.blit(print, (495, 200))
    screen.blit(printGagnant, (562, 300))

pygame.init()

screen = pygame.display.set_mode((1250, 650))
pygame.display.set_caption("Big War")
icon = pygame.image.load("objet\explosion.png").convert_alpha()
pygame.display.set_icon(icon)
background = pygame.image.load("objet\BigWar.png").convert()
screen.blit(background, (0, 0))
cloud = pygame.image.load("objet\Blanc.png").convert()
scoreGreen = 0
scoreBlue = 0
font = pygame.font.SysFont('Verdana', 25)
fontWinner = pygame.font.SysFont('Verdana', 60)
flecheGreen = pygame.image.load("objet\_FlecheVert.png").convert_alpha()
flecheBlue = pygame.image.load("objet\_FlecheBleu.png").convert_alpha()

#class des armées vert
class GreenArmy:
    green_plane = pygame.image.load("objet\Avion_v.png").convert_alpha()
    green_truck1 = pygame.image.load("objet\Camion_v.png").convert_alpha()
    green_truck2 = pygame.image.load("objet\Camion_v.png").convert_alpha()
    green_truck3 = pygame.image.load("objet\Camion_v.png").convert_alpha()
    green_truck4 = pygame.image.load("objet\Camion_v.png").convert_alpha()
    char_vert1 = pygame.image.load("objet\Tank_v.png").convert_alpha()
    char_vert2 = pygame.image.load("objet\Tank_v.png").convert_alpha()

#class des armées bleu
class BlueArmy:
    plane_blue = pygame.image.load("objet\Avion_b.png").convert_alpha()
    truck_blue1 = pygame.image.load("objet\Camion_b.png").convert_alpha()
    truck_blue2 = pygame.image.load("objet\Camion_b.png").convert_alpha()
    truck_blue3 = pygame.image.load("objet\Camion_b.png").convert_alpha()
    truck_blue4 = pygame.image.load("objet\Camion_b.png").convert_alpha()
    char_bleu1 = pygame.image.load("objet\Tank_b.png").convert_alpha()
    char_bleu2 = pygame.image.load("objet\Tank_b.png").convert_alpha()


explosionPng = pygame.image.load("objet\Explosion.png").convert_alpha()
explosionMp3 = pygame.mixer.Sound("objet\explosion.mp3")
there = pygame.image.load("objet\Marque.png").convert_alpha()

posXOfGreen = position("x", "vert")
posYOfGreen = position("y", "vert")
posXOfBlue = position("x", "bleu")
posYOfBlue = position("y", "bleu")

armyGreen = GreenArmy()
callObjetGreen(armyGreen, posXOfGreen, posYOfGreen)
armyBlue = BlueArmy()
callObjetBlue(armyBlue, posXOfBlue, posYOfBlue)

posDamageXG = []
posDamageYG = []
alreadyClickXG = []
alreadyClickYG = []

posDamageXB = []
posDamageYB = []
alreadyClickXB = []
alreadyClickYB = []

run = True

player = "green"
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        callObjetGreen(armyGreen, posXOfGreen, posYOfGreen)
        callObjetBlue(armyBlue, posXOfBlue, posYOfBlue)

        #quand c'est le tour du joueur vert
        if player == "green":
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                x, y = int(x/50) * 50, int(y/50) * 50
                
                if x < 600 and y > 49:
                    explosionMp3.play()
                    screen.blit(explosionPng, (x, y))
                        
                    alreadyClickXG.append(x)
                    alreadyClickYG.append(y)

                    j = 0
                    #boucle qui compte tous les armées vert déjà détruit et qui retourne le vainqueur
                    while j != 7:
                        if ((posXOfGreen[j] == x and posYOfGreen[j] == y) or \
                            (posXOfGreen[j]+50 == x and posYOfGreen[j] == y)):
                            x1 = 0
                            damage = False
                            while x1 != len(posDamageXG):
                                if (x == posDamageXG[x1]) and (y == posDamageYG[x1]):
                                    j += 1
                                    damage = True
                                    break
                                x1 += 1
                            if damage == False:
                                posDamageXG.append(x)
                                posDamageYG.append(y)
                                scoreGreen = len(posDamageXG)*10
                        j = j + 1
                    player = "blue"

        #quand c'est le tour du joueur bleu
        if player == "blue":
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                x, y = int(x/50) * 50, int(y/50) * 50

                if 649<x<1250 and y > 49:
                    explosionMp3.play()
                    screen.blit(explosionPng, (x, y))
                    
                    alreadyClickXB.append(x)
                    alreadyClickYB.append(y)

                    j = 0
                    #boucle qui compte tous les armées bleu déjà détruit et qui retourne le vainqueur
                    while j != 7:
                        if ((posXOfBlue[j] == x and posYOfBlue[j] == y) or \
                            (posXOfBlue[j]+50 == x and posYOfBlue[j] == y)):
                            x1 = 0
                            damage1 = False
                            while x1 != len(posDamageXB):
                                if (x == posDamageXB[x1]) and (y == posDamageYB[x1]):
                                    j += 1
                                    damage1 = True
                                    break
                                x1 += 1
                            if damage1 == False:
                                posDamageXB.append(x)
                                posDamageYB.append(y)
                                scoreBlue = len(posDamageXB)*10
                        j = j + 1
                    player = "green"
            
        j = 0
        while j < len(posDamageXG):
            screen.blit(there, (posDamageXG[j], posDamageYG[j]))
            j += 1

        j = 0
        while j < len(posDamageXB):
            screen.blit(there, (posDamageXB[j], posDamageYB[j]))
            j += 1
        if player == "green":
            screen.blit(flecheGreen, (600, 300))
        if player == "blue":
            screen.blit(flecheBlue, (600, 300))
        Cloud(alreadyClickXG, alreadyClickYG, "green")
        Cloud(alreadyClickXB, alreadyClickYB, "blue") 
        positionVert = compteurPosition(posXOfGreen, posYOfGreen)
        positionBleu = compteurPosition(posXOfBlue, posYOfBlue)

        if (positionBleu*20) == scoreBlue:
            winner = "Vert"
            Winner(winner)
        if (positionVert*20) == scoreGreen:
            winner = "Bleu"
            Winner(winner)
    
        if event.type == pygame.QUIT:
            run = False
        score("green", scoreGreen)
        score("blue", scoreBlue)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

    