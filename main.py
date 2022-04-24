"""Function Graph Drawer

This application allows the user to print the graph(s) of chosen 
functions to the pygame window in the XY coordinate system.

The app accepts user input through a list of checkboxes. 

This program requires that `OpenGL.GL`, `OpenGL.GLU`, `numpy`, 
`tkinter`, and `themedtkinter` be installed within the Python 
environment you are running this code in.

This file contains the following functions:
    * init - initializes a pygame window
    * drawExp - draws exponential function
    * drawLog - draws logarithmic function
    * drawSin - draws sine function
    * drawCos - draws cosine function
    * drawTan - draws tangential function
    * drawSquare - draws square function
    * drawCart - draws the x-y plane
    * clear - clears the screen
    * begin - begins OpenGL drawing
    * end - ends OpenGL drawing
    * warningMin - handles less than exception
    * warningMax - handles more than exception
    * main - the main function of the program
"""

__author__ = "Abdulkarim Getachew (Mania)"
__copyright__ = "Copyright 2022"
__version__ = "0.0.1"
__date__ = "2022/04/23"
__maintainer__ = "Abdulkarim Getachew"
__email__ = "abdulkarimgmohammed@gmail.com"
__status__ = "Production"

# importing all the necessary modules
import pygame
from pygame.locals import *
from OpenGL.GL import * # imports all functions of OpenGL
from OpenGL.GLU import * # imports Graphics Library Utilities
import numpy as np
from tkinter import *
from tkinter.ttk import *

# global variables
# generate 100 points from -1 to 1 range
x = np.linspace(-1, 1, 100)

# Functions 
def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_caption('Graph Plotter')
    # tells pygame that we will be displaying graphics
    # made with OpenGL
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glClearColor(0.0, 0.0, 0.0, 1.0) # RGBA
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # 2D x: -1 => 1 y: -1 => 1

def drawExp():
    glColor3f(1.0, 0.0, 0.0) # body color = RED
    y = np.exp(x)
    
    begin()
    # for every pair a,b of the numbers in x,y
    for a, b in zip(x, y): # zip yields tuples
        glVertex2f(a, b)
    end()

def drawLog():
    glColor3f(0.0, 1.0, 0.0) # body color = GREEN
    y = np.log(x)
    
    begin()
    # for every pair a,b of the numbers in x,y
    for a,b in zip(x, y):
        glVertex2f(a, b)
    end()

def drawSin():
    glColor3f(0.0, 0.0, 1.0) # body color = BLUE
    y = np.sin(x)
    
    begin()
    # for every pair a,b of the numbers in x,y
    for a,b in zip(x, y):
        glVertex2f(a, b)
    end()

def drawCos():
    glColor3f(0.0, 1.0, 1.0) # body color = CYAN 
    y = np.cos(x)
    
    begin()
    # for every pair a,b of the numbers in x,y
    for a,b in zip(x, y):
        glVertex2f(a, b)
    end()

def drawTan():
    glColor3f(1.0, 1.0, 0.0) # body color = YELLOW 
    y = np.tan(x)

    begin()
    # for every pair a,b of the numbers in x,y
    for a,b in zip(x, y):
        glVertex2f(a, b)
    end()

def drawSquare():
    glColor3f(1.0, 0.0, 1.0) # body color = PURPLE
    y = np.power(x, 2)
    
    begin()
    # for every pair a,b of the numbers in x,y
    for a,b in zip(x, y):
        glVertex2f(a, b)
    end()

def drawCart():
    glColor3f(1.0, 1.0, 1.0) # body color = WHITE
    
    glBegin(GL_LINES)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    end()
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    end()

def clear():
    """clears the window with the colors in glClearColor."""
    glClear(GL_COLOR_BUFFER_BIT)

def begin():
    glBegin(GL_LINE_STRIP)

def end():
    glEnd()
    glFlush()

def warningMin():
    warning = Tk()
    warning.geometry('350x100')
    warning.title('Warning')
    Label(text = 'LESS THAN REQUIRED FUNCTIONS CHOSEN!\nPlease choose at least two functions to proceed').pack(fill = BOTH)
    ok = Button(warning, text = 'OK', command = warning.destroy)
    ok.pack(side = 'bottom', pady = 10)
    warning.mainloop()
    main() # main function call #2

def warningMax():
    warning = Tk()
    warning.geometry('400x150')
    warning.title('Warning')
    Label(text = 'MORE THAN REQUIRED FUNCTIONS CHOSEN!\nPlease choose no more than six functions to proceed\n').pack(fill = BOTH)
    Label(text = "This may be because you have chosen 'Draw All functions'\nin combination with one or more of the remaining function(s)").pack(fill = BOTH)
    ok = Button(warning, text = 'OK', command = warning.destroy)
    ok.pack(side = 'bottom', pady = 5)
    warning.mainloop()
    main() # main function call #3

def main():
    # create a tkinter window to accept user input
    root = Tk()
    root.geometry('320x320')
    root.title('Function Graph Drawer') 

    # Display description text
    label = Label(text = 'Select at least two of any functions \nyou want to draw from the list below:')
    label.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    # Accepting user input using checkboxes
    isExp = IntVar()
    exp = Checkbutton(root, text = 'Exponential function', variable = isExp, onvalue = 1, offvalue = 0, )#foreground = 'red')
    exp.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    isLog = IntVar()
    log = Checkbutton(root, text = 'Logarithmic function', variable = isLog, onvalue = 1, offvalue = 0, )#foreground = 'green')
    log.pack(side = 'top', fill = BOTH, padx = 5, pady = 5, )

    isSin = IntVar()
    sin = Checkbutton(root, text = 'Sine function', variable = isSin, onvalue = 1, offvalue = 0)#foreground = 'blue')
    sin.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    isCos = IntVar()
    cos = Checkbutton(root, text = 'Cosine function', variable = isCos, onvalue = 1, offvalue = 0, )#foreground = 'cyan')
    cos.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    isTan = IntVar()
    tan = Checkbutton(root, text = 'Tangential function', variable = isTan, onvalue = 1, offvalue = 0, )#foreground = 'yellow')
    tan.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    isSqr = IntVar()
    sqr = Checkbutton(root, text = 'Square function', variable = isSqr, onvalue = 1, offvalue = 0, )#foreground = 'purple')
    sqr.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    isAll = IntVar()
    all = Checkbutton(root, text = 'Draw All functions', variable = isAll, onvalue = 1, offvalue = 0)
    all.pack(side = 'top', fill = BOTH, padx = 5, pady = 5)

    # Submit button
    submit = Button(root, text = 'Draw', command = root.destroy)
    submit.pack(fill = Y, padx = 5, pady = 15, side = 'bottom')
    
    # Making the app user friendly so that a user can
    # force stop the application using the close[X] button
    root.protocol('WM_DELETE_WINDOW', quit)
    
    root.mainloop()
    
    init() # init function call
    
    while True:
        # ensuring that the infinite loop is eventually broken
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clear()
        drawCart()

        # Processing user input
        numDraw = 0
        if isAll.get() == 1:
            drawCos()
            drawExp()
            drawLog()
            drawSin()
            drawTan()
            drawSquare()
            numDraw += 6
        if isExp.get() == 1:
            drawExp()
            numDraw += 1
        if isLog.get() == 1:
            drawLog()
            numDraw += 1
        if isSin.get() == 1:
            drawSin()
            numDraw += 1
        if isCos.get() == 1:
            drawCos()
            numDraw += 1
        if isTan.get() == 1:
            drawTan()
            numDraw += 1
        if isSqr.get() == 1:
            drawSquare()
            numDraw += 1

        # Exceptions handling
        if numDraw < 2:
            warningMin()
        elif numDraw > 6:
            warningMax()

        pygame.display.flip()
        pygame.time.wait(10)

main() # main function call #1
