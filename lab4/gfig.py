from graphics import *
def Bresenham(x0, y0, x1, y1,win,color):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    p = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        pt = Point(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        #Matrix[round(pt.getY())-300][round(pt.getX())+300] = 1
        pt.setOutline(color)
        pt.draw(win)

        if(p >= 0):
            y += 1
            p -= 2*dx
        p += 2*dy

def drawPolygon(v,Matrix,win):
    x=list()
    for i in range(v):
        a,b=input().split()
        x.append([int(a),int(b)])
    #print(x)
    for i in range(len(x)):
        Bresenham(x[i][0],x[i][1],x[(i+1)%v][0],x[(i+1)%v][1],win,Matrix)

def drawCircle(xc,yc,x,y):
    pt = Point(xc+x,yc+y)
    pt.draw(win)
    pt = Point(xc-x,yc+y)
    pt.draw(win)
    pt = Point(xc+x,yc-y)
    pt.draw(win)
    pt = Point(xc-x,yc-y)
    pt.draw(win)
    pt = Point(xc+y,yc+x)
    pt.draw(win)
    pt = Point(xc-y,yc+x)
    pt.draw(win)
    pt = Point(xc+y,yc-x)
    pt.draw(win)
    pt = Point(xc-y,yc-x)
    pt.draw(win)


def plotCircle(xc,yc,radius):
    x = 0
    y = radius
    p = 3-2*radius
    while(y>=x):
        x += 1
        if(p>0):
            y -=1
            p = p + 4*(x-y) + 10
        else:
            p = p+4*x+6
        drawCircle(xc,yc,x,y)


def plotElipse(xradius,yradius,xc,yc):
    x = 0
    y = yradius

    rx = xradius
    ry = yradius

    # decision parameter region1
    d1 = (ry*ry) - (rx*rx*ry) + (0.25*rx*rx)
    dx =  2*ry*ry*x
    dy = 2*rx*rx*y

    while(dx<dy):
        pt = Point(x+xc,y+yc)
        pt.draw(win)
        pt = Point(xc-x,yc+y)
        pt.draw(win)
        pt = Point(xc+x,yc-y)
        pt.draw(win)
        pt = Point(xc-x,yc-y)
        pt.draw(win)

        x += 1
        dx = dx + (2*ry*ry)
        d1 = d1+dx + (ry*ry)
        if(d1>=0):
            y -=1
            dy = dy - (2*rx*rx)
            d1 = d1 - dy

    #region 2

    d2 = ((ry*ry)*((x+0.5)*(x+0.5))) +((rx * rx) * ((y - 1) * (y - 1)))-(rx * rx * ry * ry)
    while(y >=0):
        pt = Point(x+xc,y+yc)
        pt.draw(win)
        pt = Point(xc-x,yc+y)
        pt.draw(win)
        pt = Point(xc+x,yc-y)
        pt.draw(win)
        pt = Point(xc-x,yc-y)
        pt.draw(win)
        y -=1
        dy = dy -(2*rx*rx)
        d2 = d2 + (rx * rx) - dy;
        if(d2<=0):
            x +=1
            d2 = d2 + dx

def xintersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num=(x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
	den=(x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num/den

def yintersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
	return num/den
            


#win = GraphWin('gfig',300,300)
#win.setCoords(-300,-300,300,300)
#Bresenham(0,0,100,100)
#Bresenham(100,100,-100,100)
#Bresenham(-100,100,-50,-50)
#Bresenham(-50,-50,-100,50)
#Bresenham(-100,50,0,0)
#n = int(input('enter no of vertices'))
#drawPolygon(n)
#plotCircle(100,100,50)
#plotElipse(150,130,0,0)
#win.close()

