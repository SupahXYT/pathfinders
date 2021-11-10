import pyglet
window = pyglet.window.Window(800, 800)
mypic = pyglet.resource.image('drip.jpg')
sprite = pyglet.sprite.Sprite(mypic, x=0, y=0, subpixel=True)

def move_sprite(dt):
    sprite.x += 50*dt

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.clock.schedule_interval(move_sprite, 1.0/60)

pyglet.app.run()
