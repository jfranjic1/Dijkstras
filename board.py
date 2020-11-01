import pygame
import nodes
import obstacle

RIGHTCLICK = 1
LEFTCLICK = 2
MIDDLECLICK = 3
NAN = 69
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
        self.startNode = nodes.Node()
        self.startNodeBool = False
        self.endNodeBool = False
        self.endNode = nodes.Node()
        self.obstackles = list()
        self.obstacklesBool = False
    def start(self):
        temp = pygame.Rect((0,0), (self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, self.backgroundColor, temp)
        for i in range(0, self.WIDTH, 10):
            pygame.draw.line(self.surface,self.gridColor, (i, 0), (i, self.HEIGHT))
        for j in range(0, self.HEIGHT , 10):
            pygame.draw.line(self.surface, self.gridColor, (0, j), (self.WIDTH, j))
        #self.startNode.draw(self.surface, 0, 0)
        #self.endNode.draw(self.surface, 790, 590)
        while(1):
            self.clock.tick(100)
            self.screen.blit(self.surface, (0, 0))
            self.keypress()
            if(self.obstacklesBool):
                self.execute(MIDDLECLICK)
            pygame.display.update()

    def keypress(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.execute(RIGHTCLICK)
                    if event.button == 3:
                        self.execute(LEFTCLICK)
                    if event.button == 2:
                       self.obstacklesBool = True
            if(event.type == pygame.MOUSEBUTTONUP):
                 self.obstacklesBool = False
    def execute(self, command):
        if(command == RIGHTCLICK):
            if(self.startNodeBool):
                self.startNode.delete(self.surface)
            self.startNode = nodes.Node(1)
            self.startNode.draw(self.surface, pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0]  % self.squareSize, pygame.mouse.get_pos()[1] -  pygame.mouse.get_pos()[1] % self.squareSize)
            self.startNodeBool = True

        if (command == LEFTCLICK):
            if (self.endNodeBool):
                self.endNode.delete(self.surface)
            self.endNode = nodes.Node(2)
            self.endNode.draw(self.surface, pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % self.squareSize, pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % self.squareSize)
            self.endNodeBool = True
        if (command == MIDDLECLICK):
            self.obstackles.append(obstacle.Obstackle(self.surface, pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % self.squareSize, pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % self.squareSize))

