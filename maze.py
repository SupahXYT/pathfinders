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
            if row > 1 and self.maze[row-1][col] == PASSAGE:
                to_visit.insert(0, (row-1, col))
            if row < self.width - 1 and self.maze[row+1][col] == PASSAGE:
                to_visit.insert(0, (row+1, col))
            if col > 1 and self.maze[row][col-1] == PASSAGE:
                to_visit.insert(0, (row, col-1))
            if col < self.height - 1 and self.maze[row][col+1] == PASSAGE:
                to_visit.insert(0, (row, col+1))
            current = to_visit.pop(0)
        self.maze[current[0]][current[1]] = VISITED
        return current

    def _print(self, row, col):
        str = ""
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                pass



    def generate_prim(self):
        rand_row, rand_col = self.rand_cell_in_maze()
        rand_row = randrange(self.width)
        rand_col = randrange(self.height)
        self.maze[rand_row][rand_col] = PASSAGE
        frontier_cells = self.get_frontier_cells(rand_row, rand_col)
        while(len(frontier_cells) > 0):

            rand_index = randrange(len(frontier_cells))
            rand_frontier = frontier_cells.pop(rand_index)
             
            row, col = rand_frontier
            self.maze[row][col] = PASSAGE

            neighbors = self.neighbors(rand_frontier[0], rand_frontier[1])
            rand_index = randrange(len(neighbors))
            rand_neighbor = neighbors[rand_index]

            diff = ((rand_neighbor[0] - rand_frontier[0]) >> 1, (rand_neighbor[1] - rand_frontier[1]) >> 1)

            connect_row, connect_col = (rand_frontier[0] + diff[0], rand_frontier[1] + diff[1])
            self.maze[connect_row][connect_col] = PASSAGE

            frontier_cells += self.get_frontier_cells(rand_frontier[0], rand_frontier[1])

    def rand_cell_in_maze(self):
        row = randrange(1, len(self.maze) - 3)
        col = randrange(1, len(self.maze[row]) - 3)

        return (row, col)

    def neighbors(self, row, col):
        neighbors = []
        # if row > 2 and row < len(self.maze) - 3:
        #     if col > 2 and col < len(self.maze[row]) - 3:
        #         if self.maze[row - 2][col] == PASSAGE:
        #             neighbors.append((row - 2, col))
        #         if self.maze[row + 2][col] == PASSAGE:
        #             neighbors.append((row + 2, col))
        #         if self.maze[row][col + 2] == PASSAGE:
        #             neighbors.append((row, col + 2))
        #         if self.maze[row][col - 2] == PASSAGE:
        #             neighbors.append((row, col - 2))

#         if row > 1 and row < len(self.maze) - 3:
#             print("N PASS ROW")
#             if self.maze[row - 2][col] == PASSAGE:
#                 neighbors.append((row - 2, col))
#             if self.maze[row + 2][col] == PASSAGE:
#                 neighbors.append((row + 2, col))
#         if col > 1 and col < len(self.maze[row]) - 3:
#             print("N PASS COL")
#             if self.maze[row][col - 2] == PASSAGE:
#                 neighbors.append((row, col - 2))
#             if self.maze[row][col + 2] == PASSAGE:
#                 neighbors.append((row, col + 2))

        if row > 1: 
            if self.maze[row - 2][col] == PASSAGE:
                neighbors.append((row - 2, col))
        if row < len(self.maze) - 2:
            if self.maze[row + 2][col] == PASSAGE:
                neighbors.append((row + 2, col))
        if col > 1:
            if self.maze[row][col - 2] == PASSAGE:
                neighbors.append((row, col - 2))
        if col < len(self.maze[row]) - 2:
                neighbors.append((row, col + 2))

        return neighbors

    def get_frontier_cells(self, row, col):
        frontier_cells = []

        if row > 1:
            if self.maze[row - 2][col] == BLOCKED:
                frontier_cells.append((row - 2, col))
        if row < len(self.maze) - 2:
            if self.maze[row + 2][col] == BLOCKED:
                frontier_cells.append((row + 2, col))
        if col > 1:
            if self.maze[row][col - 2] == BLOCKED:
                frontier_cells.append((row, col - 2))
        if col < col < len(self.maze[row]) - 2:
                frontier_cells.append((row, col + 2))
            
        # if row > 1 and row < len(self.maze) - 3:
        #     print("F PASS ROW")
        #     if self.maze[row - 2][col] == BLOCKED:
        #         frontier_cells.append((row - 2, col))
        #     if self.maze[row + 2][col] == BLOCKED:
        #         frontier_cells.append((row + 2, col))
        # if col > 1 and col < len(self.maze[row]) - 3:
        #     print("F PASS COL")
        #     if self.maze[row][col - 2] == BLOCKED:
        #         frontier_cells.append((row, col - 2))
        #     if self.maze[row][col + 2] == BLOCKED:
        #         frontier_cells.append((row, col + 2))


#         if row > 2 and row < len(self.maze) - 3:
#             if col > 2 and col < len(self.maze[row]) - 3:
#                 if self.maze[row - 2][col] == BLOCKED:
#                     frontier_cells.append((row - 2, col))
#                 if self.maze[row + 2][col] == BLOCKED:
#                     frontier_cells.append((row + 2, col))
#                 if self.maze[row][col + 2] == BLOCKED:
#                     frontier_cells.append((row, col + 2))
#                 if self.maze[row][col - 2] == BLOCKED:
#                     frontier_cells.append((row, col - 2))
        return frontier_cells

class maze_runner:
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((width*8, height*8), pygame.RESIZABLE)
        self.width, self.height = (width, height)
        self.display.fill(col_fill)
        self.maze = maze(width, height)
        # self.maze.random_dumb()
        self.maze.prims_algorithm()
        self.maze.dfs((1, 1),(width - 2, height - 2))
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
                if (maze[row][col] == PASSAGE): 
                    pygame.draw.rect(self.display, col_fill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                elif maze[row][col] == VISITED:
                    pygame.draw.rect(self.display, col_visited, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                else:
                    pygame.draw.rect(self.display, col_nofill, pygame.Rect(round(row*8), 
                        round(col*8), round(8), round(8)))
                
runner = maze_runner(101, 101)
runner.main()

# https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
