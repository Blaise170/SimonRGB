from graphics import *
import random
import time


## authored by: blaise170
##
## Simon Game v1.2
##
## Uses the Graphics package by Zelle
## Module can be found here: http://mcsp.wartburg.edu/zelle/python/graphics.py

class Button( object ):
    def __init__( self, rect, color, win ):
        self.rect = rect
        self.color = color
        self.win = win
        self.rect.setFill(color)
        self.rect.draw(win)
    def setFill( self, color ):
        self.rect.setFill(color)
        
def SimonRGB():
    win = GraphWin("Simon!", 600, 600)
    win.setBackground("black")
    win.setCoords(0,0,500,500)

    rect1 = Button(Rectangle(Point(25,25), Point(225,225)), 'red', win)
    rect2 = Button(Rectangle(Point(275,25), Point(475,225)), 'blue', win)
    rect3 = Button(Rectangle(Point(25,275), Point(225,475)), 'green', win)
    rect4 = Button(Rectangle(Point(275,275), Point(475,475)), 'yellow', win)
            
    seq = []
    x=0
    while x == 0:
        y = random.randint(1,4)
        seq.append(y)
        for y in seq:
            if y == 1:
                rect1.setFill('pink')
                time.sleep(1)
                rect1.setFill('red')
            elif y == 2:
                rect2.setFill('cyan')
                time.sleep(1)
                rect2.setFill('blue')
            elif y == 3:
                rect3.setFill('light green')
                time.sleep(1)
                rect3.setFill('green')
            else:
                rect4.setFill('white')
                time.sleep(1)
                rect4.setFill('yellow')
        for y in seq:
            clk = win.getMouse()
            if y == 1:
                if 25 < clk.getX() < 225 and 25 < clk.getY() < 225:
                    print 'Correct'
                else:
                    lost = Text(Point(250,250),'Sorry, you lose. Click to exit.')
                    lost.setTextColor('cyan')
                    lost.draw(win)
                    x = x +1
                    break
            elif y == 2:
                if 275 < clk.getX() < 475 and 25 < clk.getY() < 225:
                    print 'Correct'
                else:
                    lost = Text(Point(250,250),'Sorry, you lose. Click to exit.')
                    lost.setTextColor('cyan')
                    lost.draw(win)
                    x = x + 1
                    break
            elif y == 3:
                if 25 < clk.getX() < 225 and 275 < clk.getY() < 475:
                    print 'Correct'
                else:
                    lost = Text(Point(250,250),'Sorry, you lose. Click to exit.')
                    lost.setTextColor('cyan')
                    lost.draw(win)
                    x = x + 1
                    break
            else:
                if 275 < clk.getX() < 475 and 275 < clk.getY() < 475:
                    print 'Correct'
                else:
                    lost = Text(Point(250,250),'Sorry, you lose. Click to exit.')
                    lost.setTextColor('cyan')
                    lost.draw(win)
                    x = x + 1
                    break
            
    win.getMouse()
    win.close()

        
SimonRGB()