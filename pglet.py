import pyglet
import maze_engine

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(width = 500, height = 500, caption = "amodu")
        self.maze = maze_engine.Maze(100, 100)

        self.label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=self.height//2, y=self.width//2)

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.circle.draw()

if __name__ == '__main__':
    window = HelloWorldWindow()
    pyglet.app.run()

