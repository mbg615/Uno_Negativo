from pyglet.window import Window, key, mouse
from pyglet import app, shapes, graphics, image, sprite

#Declares variables; window, colors, png's, etc.
winWidth = 800
winHeight = 600
fus = 1
logoImage = image.load("data/UnoNegativoLogoFinal.png")
Red = (255, 0, 0)
Blue = (0, 0 ,255)
window = Window(winWidth, winHeight, resizable = True)
batch = graphics.Batch()

#Creates groups for foreground and background.
menuBackground = graphics.OrderedGroup(0)
menuForeground = graphics.OrderedGroup(1)

#Updates background according to fullscreen.
def backgroundUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    mainBackground.width = winWidth
    mainBackground.height = winHeight

#Updates menu according to fullscreen.
def menuUpdate():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = logo.x + (winWidth  // 4)
    logo.y = logo.y + (winHeight // 3)

#Returns menu on removal of fullscreen.
def menuReturn():
    winSize = window.get_size()
    (winWidth, winHeight) = winSize
    logo.x = 250
    logo.y = 350

#Actions that occur on key press.
def on_key_press(symbol, modifiers):
    
    #If F pressed, increase fus so that it changes what happens on key press.
    if symbol == key.F:
        global fus
        fus += 1
 
#Actions that occur on key release
def on_key_release(symbol, modifiers):
    
    #If F released, toggles Fullscreen
    if symbol == key.F and fus % 2 == 0:
        window.set_fullscreen(True) 
        backgroundUpdate()
        menuUpdate()

    if symbol == key.F and fus % 2 == 1:
        window.set_fullscreen(False)
        backgroundUpdate()
        menuReturn()

#Test actions for buttons (Hola and adios)
def hola():
    print("hola")
    return

def adios():
    print("adios")
    return

#Class which creates button when given data.
class buttonRect(object):

    #Loads various aspects of the button like dimensions, color, and action.
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

    #Creates bounding box for the button.
    def boundary(self, mousePos):

        mouseX, mouseY = mousePos

        if mouseX > self.minX and mouseX < self.maxX and mouseY > self.minY and mouseY < self.maxY:
            eval(self.action + "()")

#Creates test buttons.
#holaButton = buttonRect(250, 100, 50, 50, Blue, "hola")
#adiosButton = buttonRect(400, 200, 100, 100, Blue, "adios")

#Loads buttons
def loadButtons(mouseX, mouseY):

    mousePos = mouseX, mouseY

    #holaButton.boundary(mousePos)
    #adiosButton.boundary(mousePos)


#Actions on mouse click; pulls boundary of buttons to make it clickable.
def on_mouse_press(mouseX, mouseY, button, modifiers):

    loadButtons(mouseX, mouseY)

#Declares main background.
mainBackground = shapes.Rectangle(0, 0, winWidth, winHeight, Red, batch=batch, group=menuBackground)
mainBackground.opacity = 220

#Draws all graphics; background, buttons logo, etc.
def on_draw():
    window.clear()
    batch.draw()
    logo.draw()

#Declares Logo
logo = sprite.Sprite(logoImage, 250, 350, group=menuForeground)

#Allows window to use events; drawing, clicking, pressing of buttons.
window.push_handlers(on_draw, on_key_press, on_key_release, on_mouse_press)
     
#Launches code as an app.
app.run()
