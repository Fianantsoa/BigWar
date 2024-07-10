import pygame
import random

colorGreen = (48, 138, 92)
colorBlue = (99, 110, 126)

class Groupe:
    def __init__(self, avion, camion1, camion2, camion3, camion4, char1, char2):
        self.avion = avion
        self.camion1 = camion1
        self.camion2 = camion2
        self.camion3 = camion3
        self.camion4 = camion4
        self.char1 = char1
        self.char2 = char2

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1250, 700))
        pygame.display.set_caption("Jeu de course")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        self.fontWinner = pygame.font.SysFont(None, 100)
        self.nuage = pygame.image.load("nuage.png")
        self.deleteX = []
        self.deleteY = []
        self.scoreGreen = 0
        self.scoreBlue = 0
        self.winner = None
        self.game_over = False
        
        # Création des groupes
        self.groupeVert = Groupe(avion_vert, camion_vert1, camion_vert2, camion_vert3, camion_vert4, char_vert1, char_vert2)
        self.groupeBleu = Groupe(avion_bleu, camion_bleu1, camion_bleu2, camion_bleu3, camion_bleu4, char_bleu1, char_bleu2)

    def position(self, axe, groupe):
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

    def callObjet(self, groupe, positionsX, positionsY):
        if groupe == "vert":
            self.screen.blit(self.groupeVert.avion, (positionsX[0], positionsY[0]))
            self.screen.blit(self.groupeVert.camion1, (positionsX[1], positionsY[1]))
            self.screen.blit(self.groupeVert.camion2, (positionsX[2], positionsY[2]))
            self.screen.blit(self.groupeVert.camion3, (positionsX[3], positionsY[3]))
            self.screen.blit(self.groupeVert.camion4, (positionsX[4], positionsY[4]))
            self.screen.blit(self.groupeVert.char1, (positionsX[5], positionsY[5]))
            self.screen.blit(self.groupeVert.char2, (positionsX[6], positionsY[6]))
        elif groupe ==
