from pyglet.window import Window, key
from pyglet import app, shapes, graphics, image, sprite

winWidth = 800
winHeight = 600
fus = 1
logoImage = image.load("data/UnoNegativoLogoFinal.png")
BgColor = (238, 21, 31)
window = Window(winWidth, winHeight, resizable = True)
batch = graphics.Batch()
background = graphics.OrderedGroup(0)
foreground = graphics.OrderedGroup(1)

def backgroundUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    mainBackground.width = winWidth
    mainBackground.height = winHeight

def menuUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = logo.x + (winWidth  // 4)
    logo.y = logo.y + (winHeight // 3)

def menuReturn():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = 250
    logo.y = 350

def on_key_press(symbol, modifiers):
    if symbol == key.F:
        global fus
        fus += 1

def on_key_release(symbol, modifiers):
    if symbol == key.F and fus % 2 == 0:
        window.set_fullscreen(True) 
        backgroundUpdate()
        menuUpdate()

    if symbol == key.F and fus % 2 == 1:
        window.set_fullscreen(False)
        backgroundUpdate()
        menuReturn()


mainBackground = shapes.Rectangle(0, 0, winWidth, winHeight, BgColor, batch=batch, group=background)

def on_draw():
    window.clear()
    batch.draw()
    logo.draw()

logo = sprite.Sprite(logoImage, 250, 350, group=foreground)

window.push_handlers(on_draw, on_key_press, on_key_release)
        
app.run()