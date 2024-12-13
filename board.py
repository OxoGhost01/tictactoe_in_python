import pygame


class Jeu:
    def __init__(self, screen):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.joueur = True
        self.screen = screen

    def change_player(self):
        self.joueur = not self.joueur

    def dessine(self):
        for i in range(1, 3):
            pygame.draw.rect(self.screen, (255, 0, 0), (300 * i, 0, 5, 900))
            pygame.draw.rect(self.screen, (255, 0, 0), (0, 300 * i, 900, 5))
        for x in range(3):
            for y in range(3):
                if self.board[x][y] is True:
                    pygame.draw.line(self.screen, (0, 175, 255), (50 + (300 * x), 50 + (300 * y)), (250 + (300 * x), 250 + (300 * y)), 5)
                    pygame.draw.line(self.screen, (0, 175, 255), (50 + (300 * x), 250 + (300 * y)), (250 + (300 * x), 50 + (300 * y)), 5)
                elif self.board[x][y] is False:
                    pygame.draw.circle(self.screen, (0, 175, 255), (150 + (300 * x), 150 + (300 * y)), 100, 5)

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        return 1
        
    @staticmethod
    def souris(coord):
        for x in range(3):
            for y in range(3):
                if 0 <= coord[0] <= 300 + (x * 300) and 0 <= coord[1] <= 300 + (y * 300):
                    return x, y
    
    def clic(self, x, y):
        if self.board[x][y] is None:
            self.board[x][y] = self.joueur
            self.change_player()