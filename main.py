import engine
import sys

# Run the game engine
def runGame():
    engine.main()

# Run game engine directly without GUI
args = sys.argv[1:]
if len(args) == 1 and args[0] == '--no_gui':
    running = True
    while running:
        runGame()
    exit()

from pyglet.window import Window, key, mouse
from pyglet import app, shapes, graphics, image, sprite

# Declaring colors, window, graphics, etc.
winWidth = 800
winHeight = 600
fus = 1
logoImage = image.load("data/UnoNegativoLogoFinal.png")
BgColor = (238, 21, 31)
Blue = (0, 0 ,255)
fullscreen = False
window = Window(winWidth, winHeight, resizable = True)
mainMenu = graphics.Batch()

mainBackground = graphics.OrderedGroup(0)
mainForeground = graphics.OrderedGroup(1)  

# Updates main menu

def mainMenuUpdate(fullscreen):
    winSize = window.get_size()
    (winWidth, winHeight) = winSize

    if fullscreen == True:
        logo.x = logo.x + (winWidth  // 4)
        logo.y = logo.y + (winHeight // 3)
        mainBackground.width = winWidth
        mainBackground.height = winHeight

        holaButton.x = holaButton.x + (winWidth  // 4)
        holaButton.y = holaButton.y + (winHeight // 3)
        holaButton.update()


    if fullscreen == False:
        logo.x = 250
        logo.y = 350
        mainBackground.width = winWidth
        mainBackground.height = winHeight

    
# Actions that require a button press
def on_key_press(symbol, modifiers):
    # On F press, increases fus in order to change what f does on each press.
    if symbol == key.F:
        global fus
        fus += 1
        
        
# Actions that occur on button release
def on_key_release(symbol, modifiers):
    
    # After F is released, decides whether window needs to go fullscreen or return to normal.
    if symbol == key.F and fus % 2 == 0:
        fullscreen = True
        window.set_fullscreen(True) 
        mainMenuUpdate(fullscreen)

    if symbol == key.F and fus % 2 == 1:
        fullscreen = False
        window.set_fullscreen(False)
        mainMenuUpdate(fullscreen)

# Both following functions are test actions for buttons
# Button class: given needed data, creates a button with a boundary, shape, and action to do.
class buttonRect(object):

    #Loads various values of the button
    def __init__(self, x, y, width, height, color, batch, group, action):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.batch = batch
        self.group = group
        self.name = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, batch = self.batch, group = self.group)
        self.action = action

        self.minX = x
        self.maxX = x + width
        self.minY = y
        self.maxY = y + height

        self.storX = x
        self.storY = y
    


    # Creates boundary of the button so that it can be clicked.
    def boundary(self, mousePos):

        self.minX = self.x
        self.maxX = self.x + self.width
        self.minY = self.y
        self.maxY = self.y + self.height

        mouseX, mouseY = mousePos

        if mouseX > self.minX and mouseX < self.maxX and mouseY > self.minY and mouseY < self.maxY:
            eval(self.action + "()")

        
    def update(self):

        self.name = shapes.Rectangle(self.x, self.y, self.width, self.height, self.color, batch = self.batch, group = self.group)


# Creates test Buttons.
# Example: adiosButton = buttonRect(400, 200, 100, 100, Blue, "adios")
holaButton = buttonRect(300, 250, 200, 50, Blue, mainMenu, mainForeground, "runGame")

# Loads the button boundary by getting the boundary function from the button class.
def loadMenuBoxes(mouseX, mouseY):

    mousePos = mouseX, mouseY

    holaButton.boundary(mousePos)

# Allows buttons to be clicked when mouse is in boundary
def on_mouse_press(mouseX, mouseY, button, modifiers):

    loadMenuBoxes(mouseX, mouseY)

# Creates background of main menu.
mainBackground = shapes.Rectangle(0, 0, winWidth, winHeight, BgColor, batch = mainMenu, group = mainBackground)
mainBackground.opacity = 220


# Draws all graphics on window: background, buttons, logo, etc.
def on_draw():
    window.clear()
    mainMenu.draw()
    
    
# Creates logo
logo = sprite.Sprite(logoImage, 250, 350, batch = mainMenu, group = mainForeground)


# Allows window to use all events such as the graphic creation, button presses, and mouse clicks.
window.push_handlers(on_draw, on_key_press, on_key_release, on_mouse_press)
        
app.run()