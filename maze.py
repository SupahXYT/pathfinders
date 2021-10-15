import pygame 
from random import randrange

BLOCKED = 0
PASSAGE = 1
START = 2
END = 3
VISITED = 4

# BLOCKED = 0
# PASSAGE = 1

col_bg = (0, 0, 0)
COL_BG = (0, 0, 0)
col_nofill = (50, 50, 50)
col_fill = (255, 255, 255)
col_start = (0, 255, 0)
col_dest = (255, 0, 0)
col_visited = (255, 0, 0)


class tile:
    def __init__(self, row, col):
        self.state = BLOCKED
        self.color = col_nofill

class starting_tile(tile):
    def __init__(self, row, col):
        super().__init__
        self.color = col_start

class dest_tile(tile):
    def __init__(self, row, col):
        super().__init__
        self.color = col_dest

class maze:
    def __init__(self, width, height):
        self.maze = [[BLOCKED for i in range(height)] for j in range(width)]
        self.width, self.height = width, height

    def random_dumb(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                # Create walls
                if i > 0 and i < len(self.maze) - 1:
                    if j > 0 and j < len(self.maze[i]) - 1:
                        rand_value = randrange(2)
                        self.maze[i][j] = rand_value

    def prims_algorithm(self):
        frontiers = []
        row = 1
        col = 1
        frontiers.append([row, col, row, col])

        while len(frontiers) > 0:
            f = frontiers.pop(randrange(len(frontiers)))
            row = f[2]
            col = f[3]
            if self.maze[row][col] == BLOCKED:
                self.maze[f[0]][f[1]] = self.maze[row][col] = PASSAGE
                if row >= 2 and self.maze[row-2][col] == BLOCKED:
                    frontiers.append([row-1, col, row-2, col])
                if col >= 2 and self.maze[row][col-2] == BLOCKED:
                    frontiers.append([row, col-1, row, col-2])
                if row < self.width-3 and self.maze[row+2][col] == BLOCKED:
                    frontiers.append([row+1, col, row+2, col])
                if col < self.height-3 and self.maze[row][col+2] == BLOCKED:
                    frontiers.append([row, col+1, row, col+2])

    def dfs(self, start, end):
        to_visit = []
        current = start
        while current != end:
            row = current[0]
            col = current[1]
            self.maze[row][col] = VISITED
            # right 
            if col < self.height - 1 and self.maze[row][col+1] == PASSAGE:
                to_visit.append((row, col+1))
            # down 
            if row < self.width - 1 and self.maze[row+1][col] == PASSAGE:
                to_visit.append((row+1, col))
            # left 
            if col > 1 and self.maze[row][col-1] == PASSAGE:
                to_visit.append((row, col-1))
            # up
            if row > 1 and self.maze[row-1][col] == PASSAGE:
                to_visit.append((row-1, col))

            if len(to_visit) > 0:
                current = to_visit.pop(0)
        self.maze[current[0]][current[1]] = VISITED
        return current

class maze_runner:
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((width*8, height*8), pygame.RESIZABLE)
        self.width, self.height = (width, height)
        self.display.fill(col_fill)
        self.maze = [[BLOCKED for i in range(height)] for j in range(width)]
        # self.maze = maze(width, height)
        # self.maze.random_dumb()
        self.prims_algorithm()
        self.dfs((1, 1),(width - 2, height - 2))
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
        self.display.fill(col_bg)
        for row in range(self.width):
            for col in range(self.height):
                if self.maze[row][col] == PASSAGE: 
                    pygame.draw.rect(self.display, col_fill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                elif self.maze[row][col] == VISITED:
                    pygame.draw.rect(self.display, col_visited, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                else:
                    pygame.draw.rect(self.display, col_nofill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))

    def prims_algorithm(self):
        frontiers = []
        row = 1
        col = 1
        frontiers.append([row, col, row, col])

        while len(frontiers) > 0:
            f = frontiers.pop(randrange(len(frontiers)))
            row = f[2]
            col = f[3]
            if self.maze[row][col] == BLOCKED:
                self.maze[f[0]][f[1]] = self.maze[row][col] = PASSAGE
                if row >= 2 and self.maze[row-2][col] == BLOCKED:
                    frontiers.append([row-1, col, row-2, col])
                if col >= 2 and self.maze[row][col-2] == BLOCKED:
                    frontiers.append([row, col-1, row, col-2])
                if row < self.width-3 and self.maze[row+2][col] == BLOCKED:
                    frontiers.append([row+1, col, row+2, col])
                if col < self.height-3 and self.maze[row][col+2] == BLOCKED:
                    frontiers.append([row, col+1, row, col+2])

    def dfs(self, start, end):
        to_visit = []
        current = start
        while current != end:
            row = current[0]
            col = current[1]
            self.maze[row][col] = VISITED

            # right 
            if col < self.height - 1 and self.maze[row][col+1] == PASSAGE:
                to_visit.append((row, col+1))
            # down 
            if row < self.width - 1 and self.maze[row+1][col] == PASSAGE:
                to_visit.append((row+1, col))
            # left 
            if col > 1 and self.maze[row][col-1] == PASSAGE:
                to_visit.append((row, col-1))
            # up
            if row > 1 and self.maze[row-1][col] == PASSAGE:
                to_visit.append((row-1, col))
            current = to_visit.pop(0)
            pygame.time.wait(1)
            self.draw()
            pygame.display.flip()
        self.maze[current[0]][current[1]] = VISITED
        return current

runner = maze_runner(51, 51)
runner.main()

# https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
