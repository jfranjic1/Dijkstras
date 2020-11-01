import pygame

class Node:
    def __init__(self):
        self.squaresize = 10
        self.x = 0
        self.y = 0
        self.color = (255,0,0)
    def draw(self, surface, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(surface, self.color, (self.x + self.squaresize/2, self.y + self.squaresize/2), self.squaresize/2)
