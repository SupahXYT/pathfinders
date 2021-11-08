import pyglet, time, threading
from random import randrange
import maze_engine

class Display(pyglet.window.Window):
    def __init__(self):
        super().__init__(width = 71*8, height = 51*8, caption = "amodu")
        self.maze = maze_engine.Maze(71, 51)
        self.batch = pyglet.graphics.Batch()
        t1 = threading.Thread(target=self.random_draw)
        t1.start()

    def on_draw(self):
        print("asd")
        self.clear()
        for row in range(self.maze.width):
            for col in range(self.maze.height):
                if self.maze.grid[row][col] == maze_engine.Tile.wall:
                    pyglet.shapes.Rectangle(x=row*8, y=col*8, width=8, height=8, color=(30, 30, 30)).draw()
                else:
                    pyglet.shapes.Rectangle(x=row*8, y=col*8, width=8, height=8, color=(255, 255, 255)).draw()
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

