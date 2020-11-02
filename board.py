import pygame
import nodes
import obstacle
import GodsAlgorithm


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
        self.squareSize = 20
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
        self.matrix = list()
        self.space = False
        # X, Y, Type (0 normal, 1 start, 2 end, 3 obstacle), visited #
        for i in range(0, self.WIDTH, self.squareSize):
            temp = list()
            for j in range(0, self.HEIGHT, self.squareSize):
                temp.append(((i, j), 0, 0))
            self.matrix.append(temp)

    def start(self):
        temp = pygame.Rect((0,0), (self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.surface, self.backgroundColor, temp)
        for i in range(0, self.WIDTH, self.squareSize):
            pygame.draw.line(self.surface,self.gridColor, (i, 0), (i, self.HEIGHT))
        for j in range(0, self.HEIGHT , self.squareSize):
            pygame.draw.line(self.surface, self.gridColor, (0, j), (self.WIDTH, j))
        #self.startNode.draw(self.surface, 0, 0)
        #self.endNode.draw(self.surface, 790, 590)
        while(1):
            self.clock.tick(100)
            self.screen.blit(self.surface, (0, 0))
            if(not self.space):
                self.keypress()
                if(self.obstacklesBool):
                    self.execute(MIDDLECLICK)
            pygame.display.update()

    def keypress(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    g = GodsAlgorithm.GodsAlgorithm(self.matrix,self.startNode, self.surface, self.screen, self.clock)
                    while(g.itteration()):
                        pass
                    print("finished")
                if event.key == pygame.K_LCTRL:
                    self.obstacklesBool = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.execute(RIGHTCLICK)
                    if event.button == 3:
                        self.execute(LEFTCLICK)
            if(event.type == pygame.KEYUP):
                if event.key == pygame.K_LCTRL:
                    self.obstacklesBool = False


    def execute(self, command):
        if(command == RIGHTCLICK):
            if(self.startNodeBool):
                self.startNode.delete(self.surface)
                self.matrix[int(self.startNode.x / self.squareSize)][int(self.startNode.y / self.squareSize)] = ((self.startNode.x, self.startNode.y), 0, 0)
            self.startNode = nodes.Node(1)
            self.startNode.draw(self.surface, pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0]  % self.squareSize, pygame.mouse.get_pos()[1] -  pygame.mouse.get_pos()[1] % self.squareSize)
            self.matrix[int(self.startNode.x/self.squareSize)][int(self.startNode.y/self.squareSize)] = ((self.startNode.x,self.startNode.y), 1, 0)
            self.startNodeBool = True

        if (command == LEFTCLICK):
            if (self.endNodeBool):
                self.endNode.delete(self.surface)
                self.matrix[int(self.endNode.x / self.squareSize)][int(self.endNode.y / self.squareSize)] = ((self.endNode.x, self.endNode.y), 0, 0)
            self.endNode = nodes.Node(2)
            self.endNode.draw(self.surface, pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % self.squareSize, pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % self.squareSize)
            self.endNodeBool = True
            self.matrix[int(self.endNode.x / self.squareSize)][int(self.endNode.y / self.squareSize)] = ((self.endNode.x, self.endNode.y), 2, 0)
        if (command == MIDDLECLICK):
            x = pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0] % self.squareSize
            y = pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1] % self.squareSize
            self.obstackles.append(obstacle.Obstackle(self.surface, x,y))
            x = int (x/self.squareSize)
            y = int (y/self.squareSize)
            self.matrix[x][y] = ((x*self.squareSize,y*self.squareSize), 3, 0)

    def drawRect(self, visited):
        pass
