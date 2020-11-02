import  pygame
import nodes
import pygame

class GodsAlgorithm:
    def __init__(self, matrix, startNode, surface, screen, clock, squaresize):
        self.matrix = matrix
        self.squaresize = squaresize
        self.paths = list()
        self.screen = screen
        self.clock = clock
        self.blocksWide = int(800/self.squaresize)
        self.blocksHigh = int(600/ self.squaresize)
        self.surface = surface
        x = int(startNode.x / self.squaresize)
        y = int(startNode.y/self.squaresize)
        self.visited = list()
        self.ok = False
        for i in range(0, self.blocksWide):
            temp = list()
            for j in range (0, self.blocksHigh):
                temp.append(0)
            self.visited.append(temp)
        self.visited[x][y] = 1
        self.paths.insert(0, ((x, y), (x, y)))
        self.cursors = list()
        self.cursors.append(((x,y),(x,y)))
        print(self.cursors)
        self.var = ((0,0),(0,0))
        # (10, 10) (10, 11) (10, 12) #
    def itteration(self):
        self.clock.tick(100)
        for temp in self.cursors:
            x = temp[0][0]
            y = temp[0][1]
            if(self.cursorInvalid(x, y)):
                continue
            #if (not x == 0 and not x == self.blocksWide-1 and not y == 0  and not y == self.blocksHigh -1 and self.visited[x + 1][y] and self.visited[x - 1][y] and self.visited[x][y - 1] and self.visited[x][y + 1]): self.cursors.remove(temp)
            #if (skipLeft and self.visited[x][y+1] and self.visited[x][y-1]): self.cursors.remove(temp)
            #if (skipRight and self.visited[x][y + 1] and self.visited[x][y - 1]): self.cursors.remove(temp)
            #if (skipDown and self.visited[x+1][y] and self.visited[x-1][y]): self.cursors.remove(temp)
            #if (skipUp and self.visited[x + 1][y] and self.visited[x - 1][y]): self.cursors.remove(temp)
            if(self.right(x, y)):
                    return False
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            if (self.left(x, y)):
                return False
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            if (self.up(x, y)):
                return False
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            if (self.down(x, y)):
                return False
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()
        return True

    # X, Y, Type (0 normal, 1 start, 2 end, 3 obstacle), visited #
    def right(self, x, y):
        x = int (x)
        y = int (y)
        if(x + 1 > self.blocksWide-1): return
        if (self.matrix[x + 1][y][1] == 3):
            return False
        if (self.visited[x + 1][y] == 1): return False
        self.cursors.append(((x + 1, y),(x , y)))
        self.paths.append(((x + 1, y),(x , y)))
        self.visited[x + 1][y] = 1
        a = (x + 1)* self.squaresize
        b = y * self.squaresize
        temp = pygame.Rect((a,b),(self.squaresize,self.squaresize))
        pygame.draw.rect(self.surface, (0,255,0), temp)
        if (self.matrix[x + 1][y][1] == 2): return True

        return False

    def left(self, x, y):
        x = int(x)
        y = int(y)
        if (x - 1 < 0): return
        if (self.matrix[x - 1][y][1] == 3): return False
        if (self.visited[x - 1][y] == 1): return False
        self.cursors.append(((x - 1, y), (x, y)))
        self.paths.append(((x - 1, y), (x, y)))
        self.visited[x - 1][y] = 1
        a = (x - 1) * self.squaresize
        b = y * self.squaresize
        temp = pygame.Rect((a, b), (self.squaresize, self.squaresize))
        pygame.draw.rect(self.surface, (0, 255, 0), temp)
        if (self.matrix[x - 1][y][1] == 2): return True
        return False

    def up(self, x, y):
        x = int(x)
        y = int(y)

        if (y - 1 < 0): return False
        if (self.matrix[x][y - 1][1] == 3): return False
        if (self.matrix[x][y -1][2] == 1): return False
        self.cursors.append(((x, y - 1), (x, y)))
        self.paths.append(((x, y - 1), (x, y)))
        self.visited[x][y - 1] = 1
        a = (x) * self.squaresize
        b = (y-1) * self.squaresize
        temp = pygame.Rect((a, b), (self.squaresize, self.squaresize))
        pygame.draw.rect(self.surface, (0, 255, 0), temp)
        if (self.matrix[x][y - 1][1] == 2): return True
        return False

    def down(self, x, y):
        x = int(x)
        y = int(y)
        if (y + 1 > self.blocksHigh-1): return False
        if (self.matrix[x][y + 1][1] == 3): return False
        if (self.matrix[x][y + 1][2] == 1): return False
        self.cursors.append(((x, y + 1), (x, y)))
        self.paths.append(((x, y + 1), (x, y)))
        self.visited[x][y + 1] = 1
        a = (x) * self.squaresize
        b = (y + 1) * self.squaresize
        temp = pygame.Rect((a, b), (self.squaresize, self.squaresize))
        pygame.draw.rect(self.surface, (0, 255, 0), temp)
        if (self.matrix[x][y + 1][1] == 2): return True
        return False

    def cursorInvalid(self, x, y):
        if((self.cursorLeftBlock(x,y) or self.cursorLeftVisited(x,y)) and (self.cursorRightBlock(x,y) or self.cursorRightVisited(x,y)) and (self.cursorUpBlock(x,y) or self.cursorUpVisited(x,y)) and (self.cursorDownBlock(x,y) or self.cursorDownVisited(x,y))):
            return True
        return False
    def cursorLeftVisited(self, x, y):
        if (not x == 0 and self.visited[x-1][y]):
            return True
        return False

    def cursorRightVisited(self, x, y):
        if(not x == self.blocksWide-1 and self.visited[x+1][y]):
            return True
        return False

    def cursorUpVisited(self, x, y):
        if (not y == 0 and self.visited[x][y-1]):
            return True
        return False

    def cursorDownVisited(self, x, y):
        if (not y == self.blocksHigh-1 and self.visited[x][y+1]):
            return True
        return False

    def cursorLeftBlock(self, x, y):
        if(x == 0):return True
        if(self.matrix[x-1][y][1] ==3):
            return True
        return False

    def cursorRightBlock(self, x, y):
        if (x == self.blocksWide - 1): return True
        if (self.matrix[x+1][y][1] == 3):
            return True
        return False

    def cursorUpBlock(self, x, y):
        if (y == 0): return True
        if (self.matrix[x][y-1][1] == 3):
            return True
        return False

    def cursorDownBlock(self, x, y):
        if (y == self.blocksHigh-1): return True
        if (self.matrix[x][y + 1][1] == 3):
            return True
        return False




