import pygame 
from random import randrange

BLOCKED = 0
PASSAGE = 1

col_bg = (0, 0, 0)
col_nofill = (50, 50, 50)
col_fill = (255, 255, 255)

class maze:
    def __init__(self, width, height):
        self.maze = [[BLOCKED for i in range(height)] for j in range(width)]

    def random_dumb(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                # Create walls
                if i > 0 and i < len(self.maze) - 1:
                    if j > 0 and j < len(self.maze[i]) - 1:
                        rand_value = randrange(2)
                        self.maze[i][j] = rand_value

    def generate_prim(self):
        current_row = randrange(len(self.maze))
        current_col = randrange(len(self.maze[0]))
        self.maze[current_row][current_col] = PASSAGE
        frontier_cells = self.get_frontier_cells(current_row, current_col)
        loo = 0
        while(len(frontier_cells) > 0):
            print(loo)
            rand_index = randrange(len(frontier_cells))
            rand_frontier = frontier_cells.pop(rand_index)

            neighbors = self.neighbors(rand_frontier[0], rand_frontier[1])
            rand_index = randrange(len(neighbors))
            rand_neighbor = neighbors[rand_index]

            diff = (rand_neighbor[0] - rand_frontier[0], rand_neighbor[1] - rand_frontier[1])

            connect_row, connect_col = (rand_frontier[0] - diff[0], rand_frontier[1] - diff[1])
            self.maze[connect_row][connect_col] = PASSAGE

            frontier_cells += self.get_frontier_cells(rand_frontier[0], rand_frontier[1])
            loo += 1

    def neighbors(self, row, col):
        neighbors = []
        if row > 2:
            if self.maze[row - 2][col] == PASSAGE:
                neighbors.append((row - 2, col))
        if row < len(self.maze) - 3:
            if self.maze[row + 2][col] == PASSAGE:
                neighbors.append((row + 2, col))
        if col > 2:
            if self.maze[row][col + 2] == PASSAGE:
                neighbors.append((row, col - 2))
        if col < len(self.maze[row]) - 3:
            if self.maze[row + 2][col - 2] == PASSAGE:
                neighbors.append((row, col + 2))
        print(f'neighbors: {neighbors}')
        return neighbors

    def get_frontier_cells(self, row, col):
        frontier_cells = []
        if row > 2:
            if self.maze[row - 2][col] == BLOCKED:
                frontier_cells.append((row - 2, col))
        if row < len(self.maze) - 3:
            if self.maze[row + 2][col] == BLOCKED:
                frontier_cells.append((row + 2, col))
        if col > 2:
            if self.maze[row][col + 2] == BLOCKED:
                frontier_cells.append((row, col - 2))
        if col < len(self.maze[row]) - 3:
            if self.maze[row + 2][col - 2] == BLOCKED:
                frontier_cells.append((row, col + 2))
        print(f'frontier:  {frontier_cells}')
        return frontier_cells

class display:
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
        self.width, self.height = (width, height)
        self.display.fill(col_fill)
        self.maze = maze(width, height)
        self.maze.random_dumb()
        self.maze.generate_prim()
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
                else:
                    pygame.draw.rect(self.display, col_nofill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                
d = display(30, 30)
d.main()

# https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
