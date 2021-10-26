import pygame
from random import randrange

class Tile:
    wall = 0
    passage = 1 
    start = 2
    dest = 3
    visited = 4

class Color:
    wall = (80, 81, 79)
    passage = (255, 252, 255)
    start = (58, 255, 75)
    dest = (255, 106, 56)
    to_visit = (36, 123, 160)
    visited = (36, 177, 194)
    path = (255, 105, 126)

class Maze:
    def __init__(self, display, width, height):
        self.display = display 
        self.width = width 
        self.height = height
        self.grid = [[Tile.wall for i in range(height)] for j in range(width)]
        self.adj = [[None for i in range(height)] for j in range(width)]

    # Set all tiles in grid to passage
    def clear(self):
        for row in range(self.width):
            for col in range(self.height):
                self.grid[row][col] = Tile.passage

    # Set all tiles in grid to wall
    def block(self):
        for row in range(self.width):
            for col in range(self.height):
                self.grid[row][col] = Tile.wall

    # Set visited tiles to passage 
    # returns updated surfaces
    def flush(self):
        rects = []
        for row in range(self.width):
            for col in range(self.height):
                if self.grid[row][col] == Tile.visited:
                    self.grid[row][col] = Tile.passage
                    rects.append(pygame.draw.rect(self.display, Color.passage, 
                        pygame.Rect(row*8, col*8, 8, 8)))
        return rects

    # Full screen drawing function
    def draw(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.grid[row][col] == Tile.passage: 
                    pygame.draw.rect(self.display, Color.passage,
                        pygame.Rect(row*8, col*8, 8, 8))
                elif self.grid[row][col] == Tile.visited:
                    pygame.draw.rect(self.display, Color.visited, 
                        pygame.Rect(row*8, col*8, 8, 8))
                else:
                    pygame.draw.rect(self.display, Color.wall, 
                        pygame.Rect(row*8, col*8, 8, 8))

    def draw_path(self, start, dest, path):
        rects = []
        for tile in path:
            rects.append(pygame.draw.rect(self.display, Color.path, 
                pygame.Rect(tile[0]*8, tile[1]*8, 8, 8)))
        rects.append(pygame.draw.rect(self.display, Color.start, 
            pygame.Rect(start[0]*8, start[1]*8, 8, 8)))
        rects.append(pygame.draw.rect(self.display, Color.dest, 
            pygame.Rect(dest[0]*8, dest[1]*8, 8, 8)))
        return rects

    def draw_sd(self, start, dest):
        rects = []
        rects.append(pygame.draw.rect(self.display, Color.start, 
            pygame.Rect(start[0]*8, start[1]*8, 8, 8)))
        rects.append(pygame.draw.rect(self.display, Color.dest, 
            pygame.Rect(dest[0]*8, dest[1]*8, 8, 8)))
        return rects

    def gen_prim(self):
        frontiers = []
        row = 1
        col = 1
        frontiers.append([row, col, row, col])

        while len(frontiers) > 0:
            f = frontiers.pop(randrange(len(frontiers)))
            row = f[2]
            col = f[3]
            if self.grid[row][col] == Tile.wall:
                self.grid[f[0]][f[1]] = self.grid[row][col] = Tile.passage
                if row >= 2 and self.grid[row-2][col] == Tile.wall:
                    frontiers.append([row-1, col, row-2, col])
                if col >= 2 and self.grid[row][col-2] == Tile.wall:
                    frontiers.append([row, col-1, row, col-2])
                if row < self.width-3 and self.grid[row+2][col] == Tile.wall:
                    frontiers.append([row+1, col, row+2, col])
                if col < self.height-3 and self.grid[row][col+2] == Tile.wall:
                    frontiers.append([row, col+1, row, col+2])

    def dfs(self, start, dest):
        to_visit = []
        current = start
        while current != dest:
            row = current[0]
            col = current[1]
            self.grid[row][col] = Tile.visited

            # right 
            if col < self.height - 1 and self.grid[row][col+1] == Tile.passage:
                to_visit.append((row, col+1))
                self.adj[row][col+1] = (row, col)
            # down 
            if row < self.width - 1 and self.grid[row+1][col] == Tile.passage:
                to_visit.append((row+1, col))
                self.adj[row+1][col] = (row, col)
            # left 
            if col > 1 and self.grid[row][col-1] == Tile.passage:
                to_visit.append((row, col-1))
                self.adj[row][col-1] = (row, col)
            # up
            if row > 1 and self.grid[row-1][col] == Tile.passage:
                to_visit.append((row-1, col))
                self.adj[row-1][col] = (row, col)

            if len(to_visit) > 0:
                current = to_visit.pop(0)
            else:
                break

        self.grid[current[0]][current[1]] = Tile.visited

        # find shortest path
        path = []
        if self.adj[dest[0]][dest[1]] != None:
            current = dest
            while current != start:
                path.append(current)
                current = self.adj[current[0]][current[1]]
            path.append(start)

        return path

    def dfs_visual(self, start, dest):
        # Draw maze before optimized drawing 
        # prevents black background if bg not drawn already 
        self.grid[start[0]][start[1]] = Tile.visited
        self.draw()
        pygame.display.flip()

        to_visit = []
        current = start
        while current != dest:
            rects = []
            row = current[0]
            col = current[1]
            self.grid[row][col] = Tile.visited

            # right 
            if col < self.height - 1 and self.grid[row][col+1] == Tile.passage:
                to_visit.append((row, col+1))
                self.adj[row][col+1] = (row, col)
                rect = pygame.draw.rect(self.display, Color.visited, 
                    pygame.Rect(row*8, (col+1)*8, 8, 8))
                rects.append(rect)
            # down 
            if row < self.width - 1 and self.grid[row+1][col] == Tile.passage:
                to_visit.append((row+1, col))
                self.adj[row+1][col] = (row, col)
                rect = pygame.draw.rect(self.display, Color.visited, 
                    pygame.Rect((row+1)*8, col*8, 8, 8))
                rects.append(rect)
            # left 
            if col > 1 and self.grid[row][col-1] == Tile.passage:
                to_visit.append((row, col-1))
                self.adj[row][col-1] = (row, col)
                rect = pygame.draw.rect(self.display, Color.visited, 
                    pygame.Rect(row*8, (col-1)*8, 8, 8))
                rects.append(rect)
            # up
            if row > 1 and self.grid[row-1][col] == Tile.passage:
                to_visit.append((row-1, col))
                self.adj[row-1][col] = (row, col)
                rect = pygame.draw.rect(self.display, Color.visited, 
                    pygame.Rect((row-1)*8, col*8, 8, 8))
                rects.append(rect)

            if len(to_visit) > 0:

                for tile in to_visit:
                    rect = pygame.draw.rect(self.display, Color.to_visit, 
                        pygame.Rect(current[0]*8, current[1]*8, 8, 8))
                    rects.append(rect)

                current = to_visit.pop(0)
                pygame.display.update(rects)
                pygame.time.wait(3)
            else:
                break

        self.grid[current[0]][current[1]] = Tile.visited

        # find shortest path
        path = []
        if self.adj[dest[0]][dest[1]] != None:
            current = dest
            while current != start:
                path.append(current)
                current = self.adj[current[0]][current[1]]
            path.append(start)

        return path

class Display:
    def __init__(self, width, height):
        self.display = pygame.display.set_mode((width*8, height*8))
        self.width = width
        self.height = height
        self.maze = Maze(self.display, width, height)
        self.maze.gen_prim()
        self.start = (1, 1)
        self.dest = (width // 2, height//2)
        self.path = self.maze.dfs_visual(self.start, self.dest)

    def main(self):
        running = True 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.maze.draw_path(self.start, self.dest, self.path)
            pygame.display.flip()
            pygame.time.wait(100)

if __name__ == '__main__':
    runner = Display(71, 51)
    runner.maze.flush()
    runner.maze.draw()
    pygame.display.flip()
    runner.main()

