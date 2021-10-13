import pygame 
from random import randrange

col_bg = (0, 0, 0)
col_border = (255, 255, 255)
col_fill = (255, 255, 255)

class maze:
    def __init__(self, width, height):
        self.maze = [[0 for i in range(height)] for j in range(width)]

        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                rand_value = randrange(2)
                self.maze[i][j] = rand_value

class display:
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
        self.width, self.height = (width, height)
        self.display.fill(col_bg)
        self.maze = maze(width, height)
        pygame.display.flip()

    def main(self):
        self.draw()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
            pygame.time.wait(100)

    def draw(self):
        maze = self.maze.maze
        self.display.fill(col_bg)
        for row in range(self.width):
            for col in range(self.height):
                if(maze[row][col]): 
                    pygame.draw.rect(self.display, col_fill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                
d = display(30, 30)
d.main()

