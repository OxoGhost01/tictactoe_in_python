from board import *
from menu import Menu
import sys

from pygame.locals import *


"""
Joueur : True = croix  ;  False = rond
"""



pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Tic Tac Toe v2.0")
sysFont = pygame.font.SysFont("None", 100)
sysFont2 = pygame.font.SysFont("None", 40)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
jeu = Jeu(screen)
menu = Menu(screen)
game = False
number = 0
fin = False


while True:
    screen.fill(black)
    if not game:
        if not fin:
            menu.choose(number)
            menu.click(pygame.mouse.get_pos(), False, number)
        if fin:
            texte = sysFont.render(f"Le gagnant est : {gagnant}", 0, white)
            screen.blit(texte, (70, 300))
            rejouer = sysFont2.render("Pour rejouer, pressez ESPACE", 0, white)
            screen.blit(rejouer, (200, 500))
    else:
        jeu.dessine()
        a = jeu.check_win()
        if a is not 1:
            if a is True:
                gagnant = "Croix"
            else:
                gagnant = "Rond"
            fin = True
            game = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game:
                number = menu.click(pygame.mouse.get_pos(), True, number)
                if number == 3 or number == 4:
                    game = True
            else:
                coord = jeu.souris(pygame.mouse.get_pos())
                jeu.clic(coord[0], coord[1])
        if event.type == event.type == KEYDOWN:
            if event.key == K_SPACE and fin:
                game = False
                fin = False
                jeu = Jeu(screen)
                menu = Menu(screen)
                number = 0
        if event.type == QUIT or number == 1:
            pygame.quit()
            sys.exit()
    pygame.display.update()
