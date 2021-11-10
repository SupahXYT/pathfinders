import pyglet, time, threading
from random import randrange
import maze_engine

class Display(pyglet.window.Window):
    def __init__(self):
        super().__init__(width = 71*8, height = 51*8, caption = "amodu")
        self.maze = maze_engine.Maze(71, 51)
        self.maze.gen_prim()
        self.batch = pyglet.graphics.Batch()
        self.sh = square(50, 50, self.width, self.height)
        pyglet.clock.schedule_interval(self.update, 1.0/60)
        t1 = threading.Thread(target=self.sh.move)
        t1.start()

    def on_draw(self):
        self.clear()
        # vertices = []
        # color = []
        # for row in range(self.maze.width):
        #     for col in range(self.maze.height):
        #         if self.maze.grid[row][col] == maze_engine.Tile.wall:
        #             x, y = row*8, col*8
        #             vertices.append([x, y, x, y+8, x+8, y+8, x+8, y])
        #             color.append([25, 25, 25])
        #         else:
        #             x, y = row*8, col*8
        #             vertices.append([x, y, x, y+8, x+8, y+8, x+8, y])
        #             color.append([255, 255, 255])

        # vertex_list = pyglet.graphics.vertex_list(8,
        # ('v2i', vertices))

        triangles = 10
        vertices = []
        for i in range(triangles):
            x, y = randrange(self.width), randrange(self.height)
            vertices.append(x)
            vertices.append(y)
            vertices.append(x+10)
            vertices.append(y+10)
            vertices.append(x+10)
            vertices.append(y)

        vertex_list = pyglet.graphics.vertex_list(triangles*3, ('v2i', vertices))
        vertex_list.draw(pyglet.gl.GL_TRIANGLES)

        # https://wiki.python.org/moin/PythonSpeed/PerformanceTips

        # vertex_list.draw(pyglet.gl.GL_QUADS)
        # pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLES, ('v3i', (10, 10, 20, 20, 30, 30)))

        # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINES,
        #     [0, 1, 2, 3],
        #     ('v2f', (0, 0, self.width, self.height, self.width/2, 0, 0, self.height))
        # )

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2, 0, 2, 3],
            ('v2i', (self.sh.x, self.sh.y,
                     self.sh.x, self.sh.y + 10,
                     self.sh.x + 10, self.sh.y + 10,
                     self.sh.x + 10, self.sh.y))
        )

        pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2],
            ('v2i', (self.sh.x, self.sh.y,
                     self.sh.x, self.sh.y + 10,
                     self.sh.x + 10, self.sh.y + 10)),
            ('c3B', [123, 123, 123, 123, 123, 123, 123, 123, 123])
        )

        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
        ('v2i', (10, 10, 10, 20, 20, 20, 20, 10)))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(f'{x}, {y}: {buttons}')

    def update(self, dt):
        pass

class square:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.vx, self.vy = 5, 0

    def move(self):
        for i in range(1000):
            if self.x < 0:
                self.vx = -self.vx
            if self.x > self.width:
                self.vx = -self.vx

            self.x += self.vx 
            time.sleep(1.0/60)

if __name__ == '__main__':
    window = Display()
    # print("past")
    pyglet.app.run()

