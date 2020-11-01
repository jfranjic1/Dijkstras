import pygame

class Node:
    def __init__(self, a = 0):
        self.squaresize = 8
        self.x = 0
        self.y = 0
        if(a == 0 or a == 1):
            self.color = (255,0,0)
        if (a == 2):
            self.color = (0,255,0)
    def draw(self, surface, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(surface, self.color, (self.x + self.squaresize/2+1, self.y + self.squaresize/2 + 1), self.squaresize/2)

    def delete(self, surface):
        pygame.draw.circle(surface, (255,255,255), (self.x + self.squaresize/2+1, self.y + self.squaresize/2 + 1), self.squaresize/2)
