import pygame

class Board:
    def __init__(self):
        ########################
        # SCREEN INITIALIZED #
        ######################
        self.WIDTH = 800
        self.HEIGHT  = 600
        self.backgroundColor = (255,255,255)
        self.gridColor = (100,100,100)
        self.squareSize = 10
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
    def start(self):
        temp = pygame.Rect((0,0), (self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, self.backgroundColor, temp)
        for i in range(0, self.WIDTH, 10):
            pygame.draw.line(self.surface,self.gridColor, (i, 0), (i, self.HEIGHT))
        for j in range(0, self.HEIGHT , 10):
            pygame.draw.line(self.surface, self.gridColor, (0, j), (self.WIDTH, j))
        while(1):
            self.clock.tick(10)
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()