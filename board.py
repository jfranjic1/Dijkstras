import pygame

class Board:
    def __init__(self):
        ########################
        # SCREEN INITIALIZED #
        ######################
        self.WIDTH = 800
        self.HEIGHT  = 600
        self.backgroundColor = (255,255,255)
        self.gridColor = (0,0,0)
        self.squareSize = 10
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
    
