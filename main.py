from pyglet.window import Window, key, mouse
from pyglet import app, shapes, graphics, image, sprite

#Declaring colors, window, graphics, etc.
winWidth = 800
winHeight = 600
fus = 1
logoImage = image.load("data/UnoNegativoLogoFinal.png")
Red = (255, 0, 0)
Blue = (0, 0 ,255)
window = Window(winWidth, winHeight, resizable = True)
batch = graphics.Batch()

menuBackground = graphics.OrderedGroup(0)
menuForeground = graphics.OrderedGroup(1)

#Updates background according to fullscreen
def backgroundUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    mainBackground.width = winWidth
    mainBackground.height = winHeight

#Updates logo/menu accroding to fullscreen 
def menuUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = logo.x + (winWidth  // 4)
    logo.y = logo.y + (winHeight // 3)

#Returns menu upon removal of fullscreen
def menuReturn():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = 250
    logo.y = 350

#Actions that require a button press
def on_key_press(symbol, modifiers):
    #On F press, increases fus in order to change what f does on each press.
    if symbol == key.F:
        global fus
        fus += 1
 
#Actions that occur on button release
def on_key_release(symbol, modifiers):
    
    #After F is released, decides whether window needs to go fullscreen or return to normal.
    if symbol == key.F and fus % 2 == 0:
        window.set_fullscreen(True) 
        backgroundUpdate()
        menuUpdate()

    if symbol == key.F and fus % 2 == 1:
        window.set_fullscreen(False)
        backgroundUpdate()
        menuReturn()

#Both following functions are test actions for buttons
def hola():
    print("hola")
    return

def adios():
    print("adios")
    return

#Button class: given needed data, creates a button with a boundary, shape, and action to do.
class buttonRect(object):

    #Loads various values of the button
    def __init__(self, x, y, width, height, color, action):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.name = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, batch=batch, group=menuForeground)
        self.action = action

        self.minX = x
        self.maxX = x + width
        self.minY = y
        self.maxY = y + height

    #Creates boundary of the button so that it can be clicked.
    def boundary(self, mousePos):

        mouseX, mouseY = mousePos

        if mouseX > self.minX and mouseX < self.maxX and mouseY > self.minY and mouseY < self.maxY:
            eval(self.action + "()")

#Creates test Buttons.
#holaButton = buttonRect(250, 100, 50, 50, Blue, "hola")
#adiosButton = buttonRect(400, 200, 100, 100, Blue, "adios")

#Loads the button boundary by getting the boundary function from the button class.
def loadButtons(mouseX, mouseY):

    mousePos = mouseX, mouseY

    #holaButton.boundary(mousePos)
    #adiosButton.boundary(mousePos)


#Allows buttons to be clicked when mouse is in boundary
def on_mouse_press(mouseX, mouseY, button, modifiers):

    loadButtons(mouseX, mouseY)

#Creates background of main menu.
mainBackground = shapes.Rectangle(0, 0, winWidth, winHeight, Red, batch=batch, group=menuBackground)
mainBackground.opacity = 220

#Draws all graphics on window: background, buttons, logo, etc.
def on_draw():
    window.clear()
    batch.draw()
    logo.draw()

#Creates logo
logo = sprite.Sprite(logoImage, 250, 350, group=menuForeground)

#Allows window to use all events such as the graphic creation, button presses, and mouse clicks.
window.push_handlers(on_draw, on_key_press, on_key_release, on_mouse_press)
        
app.run()
