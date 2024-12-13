import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('None', 40)

    def choose(self, number, gagnant=None):
        if number == 0:
            self.main()
        if number == 2:
            self.players()
    
    def click(self, coord, yes, menu):
        if 200 <= coord[0] <= 300 and 660 <= coord[1] <= 740:
            if yes:
                if menu == 0:
                    return 2
                else:
                    return 3                
            else:
                pygame.draw.line(self.screen, (255, 255, 255), (200, 740), (380, 740), 5)
        if 500 <= coord[0] <= 600 and 660 <= coord[1] <= 740:
            if yes:
                if menu == 0:
                    return 1
                else:
                    return 4
            else:
                pygame.draw.line(self.screen, (255, 255, 255), (500, 740), (680, 740), 5)

    def main(self):
        image = pygame.image.load("morpion2.png")
        self.screen.blit(image, (200, 100))
        jouer = self.font.render("Jouer", 0, (170, 0, 255))
        self.screen.blit(jouer, (250, 700))
        quitter = self.font.render("Quitter", 0, (170, 0, 255))
        self.screen.blit(quitter, (550, 700))
        pygame.draw.line(self.screen, (255, 255, 255), (448, 680), (448, 740), 4)
    
    def players(self):
        image = pygame.image.load("morpion2.png")
        self.screen.blit(image, (200, 100))
        choix1 = self.font.render("1 joueur", 0, (170, 0, 255))
        self.screen.blit(choix1, (225, 700))
        choix2 = self.font.render("2 joueurs", 0, (170, 0, 255))
        self.screen.blit(choix2, (525, 700))
        pygame.draw.line(self.screen, (255, 255, 255), (448, 680), (448, 740), 4)
    
