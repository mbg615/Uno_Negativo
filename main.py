from pyglet.window import *
from pyglet import app

file = open("uno.config", "r")

fullscreen = False

if fullscreen:
    win = Window(fullscreen=True)
else:
    win = Window(width=800,height=600)
app.run()