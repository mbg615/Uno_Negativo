from pyglet.window import Window, key
from pyglet import app

width = 800
height = 600
fus = 1
window = Window(width, height, resizable = True)

#file = open("uno.config", "r")

def on_key_press(symbol, modifiers):
    if symbol == key.F:
        global fus
        fus += 1

def on_key_release(symbol, modifiers):
    if symbol == key.F and fus % 2 == 0:
        window.set_fullscreen(True)

    if symbol == key.F and fus % 2 == 1:
        window.set_fullscreen(False)

def on_draw():
    window.clear()

window.push_handlers(on_key_press, on_key_release, on_draw)
        
app.run()
