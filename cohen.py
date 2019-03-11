#cohen-sutherland algorithm
from graphics import *
from gfig import Bresenham
#setting window

matrix = []
win = GraphWin('clsc',300,300)
win.setCoords(-300,-300,300,300)

#setting clipping window


ymax = int(input("enter ymax of window"))
xmax = int(input("enter xmax of window"))
ymin = int(input("enter ymin of window"))
xmin = int(input("enter xmin of window"))

Bresenham(xmin,ymin,xmin,ymax,win,"black")
Bresenham(xmin,ymin,xmax,ymin,win,"black")
Bresenham(xmax,ymin,xmax,ymax,win,"black")
Bresenham(xmin,ymax,xmax,ymax,win,"black")

INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000

def computeOutcode(x, y): 
    outcode = 0 
    if x < xmin:      
        outcode =outcode | LEFT 
    elif x > xmax:    
        outcode =outcode | RIGHT 
    if y < ymin:      
        outcode =outcode | BOTTOM  
    elif y > ymax:    
        outcode =outcode | TOP  
  
    return outcode 

def clipping(x0,y0,x1,y1,win):
    outcode0=computeOutcode(x0,y0)
    outcode1=computeOutcode(x1,y1)
    
    done=False
    accept=False
    while True:
        if (outcode0==0 and outcode1==0):#trivial accept
            accept=True
            break
        elif (outcode0 & outcode1):#trivial reject
            done=True
            break
        else:
            if outcode0>outcode1:
                outcodeOut=outcode0
            else:
                outcodeOut=outcode1
            if outcodeOut & TOP:           # point  above the clip ( diagram)
                x = x0 + (x1 - x0) *(ymax - y0) / (y1 - y0) 
                y = ymax 
  
            elif outcodeOut & BOTTOM:    # point  below the clip  
                x = x0 + (x1 - x0) *(ymin - y0) / (y1 - y0) 
                y = ymin 
  
            elif outcodeOut & RIGHT:  # point  right of the clip  
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0) 
                x = xmax 
  
            elif outcodeOut & LEFT:     # point left of the clip  
                y = y0 + (y1 - y0) *(xmin - x0) / (x1 - x0) 
                x = xmin 
  
            #intersection point x,y
            #  replace o/s point with intersection
            if outcodeOut == outcode1: 
                x1 = x 
                y1 = y 
                outcode1 = computeOutcode(x1, y1) 
            else:
                x0 = x 
                y0 = y 
                outcode0 = computeOutcode(x0,y0) 
    if accept:
        Bresenham(int(x0),int(y0),int(x1),int(y1),win,"red")
    if done:
        #print("Boo")
        Bresenham(int(x0),int(y0),int(x1),int(y1),win,"yellow")




x0,y0 = input("enter point1").split()
x1,y1 = input("enter point2").split()
Bresenham(int(x0),int(y0),int(x1),int(y1),win,"yellow")
clipping(int(x0),int(y0),int(x1),int(y1),win)
win.getMouse()

