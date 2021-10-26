import pyglet
from random import random

class Maze:
    def __init__(self, batch, width, height):
        
            self.width = width 
            self.height = height
            self.grid = [[0 for i in range(height)] for j in range(width)]
            self.randomize()

    def randomize(self):
        for row in range(self.width):
            for col in range (self.height):
                self.grid[row][col] = round(random())

    def draw(self):
        grid_map = pyglet.graphics.Batch()
        grid_map.draw()

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(width = 500, height = 500, caption = "amodu")
        self.maze = Maze(self.batch, 100, 100)



    def on_draw(self):
        self.clear()
        self.label.draw()
        self.maze.draw()


if __name__ == '__main__':
    window = HelloWorldWindow()
    pyglet.app.run()

