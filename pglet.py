import pyglet, time, threading, hello
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
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.grid = [[Tile.wall for i in range(height)] for j in range(width)]
        self.adj = [[None for i in range(height)] for j in range(width)]
        self.changes = []

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
        for row in range(self.width):
            for col in range(self.height):
                if self.grid[row][col] == Tile.visited:
                    self.grid[row][col] = Tile.passage

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
                self.changes.append((row, col))
                if row >= 2 and self.grid[row-2][col] == Tile.wall:
                    frontiers.append([row-1, col, row-2, col])
                if col >= 2 and self.grid[row][col-2] == Tile.wall:
                    frontiers.append([row, col-1, row, col-2])
                if row < self.width-3 and self.grid[row+2][col] == Tile.wall:
                    frontiers.append([row+1, col, row+2, col])
                if col < self.height-3 and self.grid[row][col+2] == Tile.wall:
                    frontiers.append([row, col+1, row, col+2])
            time.sleep(0.001)

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

class Display(pyglet.window.Window):
    def __init__(self):
        self.w, self.h = 51, 51 
        super().__init__(width = self.w*8, height = self.h*8, caption = "amodu")
        self.maze = Maze(self.w, self.h)
        pyglet.clock.schedule_interval(self.update, 1.0/60)
        self.shapes = []
        t1 = threading.Thread(target=self.maze.gen_prim)
        t1.start()
        self.vertices = []
        for row in range(self.maze.width):
            for col in range(self.maze.height):

                x, y = row*8, col*8
                self.vertices.append(x)
                self.vertices.append(y)
                self.vertices.append(x)
                self.vertices.append(y+8)
                self.vertices.append(x+8)
                self.vertices.append(y+8)
                self.vertices.append(x+8)
                self.vertices.append(y)

    def on_draw(self):
        self.clear()

        vertex_list = pyglet.graphics.vertex_list(self.maze.width*self.maze.height*4,
            ('v2f', self.vertices),
            ('c3B', self.colors()))

        vertex_list.draw(pyglet.gl.GL_QUADS)

    def colors(self):
        colors = []
        for i in range(self.w):
            for j in range(self.h):
                if self.maze.grid[i][j] == Tile.wall:
                    for k in range(12):
                        colors.append(255)
                else:
                    for k in range(12):
                        colors.append(25)
        return colors

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass
        # print(f'{x}, {y}: {buttons}')

    def update(self, dt):
        pass

    def draw_tile(self, row, col, size):
        pass

if __name__ == '__main__':
    window = Display()
    pyglet.app.run()

