import pyglet, time, threading
from random import randrange
import maze_engine

class Display(pyglet.window.Window):
    def __init__(self):
        super().__init__(width = 71*8, height = 51*8, caption = "amodu")
        self.maze = maze_engine.Maze(71, 51)
        self.batch = pyglet.graphics.Batch()
        # t1 = threading.Thread(target=self.random_draw)
        # t1.start()

    def on_draw(self):
        self.clear()
        # for row in range(self.maze.width):
        #     for col in range(self.maze.height):
        #         if self.maze.grid[row][col] == maze_engine.Tile.wall:
        #             pyglet.shapes.Rectangle(x=row*8, y=col*8, width=8, height=8, color=(30, 30, 30)).draw()
        #         else:
        #             pyglet.shapes.Rectangle(x=row*8, y=col*8, width=8, height=8, color=(255, 255, 255)).draw()
        # pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLES, ('v3i', (10, 10, 20, 20, 30, 30)))

        pyglet.graphics.draw_indexed(2, pyglet.gl.GL_POINTS,
            [0, 1],
            ('v2i', (10, 15, 30, 35))
        )

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2, 0, 2, 3],
            ('v2i', (100, 100,
                     150, 100,
                     150, 150,
                     100, 150))
        )
        self.flip()

    def random_draw(self):
        while(True):
            print("thread")
            self.maze.block()
            self.maze.gen_prim()
            time.sleep(1)

if __name__ == '__main__':
    window = Display()
    pyglet.app.run()

