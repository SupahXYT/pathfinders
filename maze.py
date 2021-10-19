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

class maze_runner:
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((width*8, height*8), pygame.RESIZABLE)
        self.width, self.height = (width, height)
        self.display.fill(col_fill)
        self.maze = [[BLOCKED for i in range(height)] for j in range(width)]
        self.adj = [[None for i in range(height)] for j in range(width)]
        self.prims_algorithm()
        self.path = self.dfs((1, 1),(width - 2, height-2))

    def main(self):
        self.draw()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            self.draw_path(self.path)
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

    def draw_path(self, path):
        for tile in path:
            pygame.draw.rect(self.display, (0, 255, 34), pygame.Rect(round(tile[0]*8), 
                round(tile[1]*8), round(8), round(8)))

    def recursive_division(self):
        pass

    def wilsons_algorithm(self):
        pass

    def prims_algorithm(self):
        frontiers = []
        row = 1
        col = 1
        frontiers.append([row, col, row, col])

        while len(frontiers) > 0:
            # array implementation of queue
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
                pygame.time.wait(1)
                self.draw()
                pygame.display.flip()

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
                self.adj[row][col+1] = (row, col)
            # down 
            if row < self.width - 1 and self.maze[row+1][col] == PASSAGE:
                to_visit.append((row+1, col))
                self.adj[row+1][col] = (row, col)
            # left 
            if col > 1 and self.maze[row][col-1] == PASSAGE:
                to_visit.append((row, col-1))
                self.adj[row][col-1] = (row, col)
            # up
            if row > 1 and self.maze[row-1][col] == PASSAGE:
                to_visit.append((row-1, col))
                self.adj[row-1][col] = (row, col)

            if len(to_visit) > 0:
                current = to_visit.pop(0)
                pygame.time.wait(5)
                self.draw()
                pygame.display.flip()
            else:
                break

        self.maze[current[0]][current[1]] = VISITED

        # find shortest path
        path = []
        if self.adj[end[0]][end[1]] != None:
            current = end 
            while current != start:
                path.append(current)
                current = self.adj[current[0]][current[1]]
            path.append(start)

        return path

    def go_right(self, start, end):
        pass

runner = maze_runner(51, 51)
runner.main()

# https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
