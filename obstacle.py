import pygame

class Obstackle:
    def __init__(self, squaresize, surface = 0, x = 0, y = 0):
        squareSize = squaresize
        color = (0,0,255)
        rect = pygame.Rect((x, y), (squareSize,squareSize))
        pygame.draw.rect(surface, color, rect)
