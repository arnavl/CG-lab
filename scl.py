
from graphics import *
from gfig import drawPolygon,Bresenham
win = GraphWin('gfig',300,300)
win.setCoords(-300,-300,300,300)

Matrix = [[0 for x in range(600)] for y in range(600)]
for i in range(600):
 for j in range(600):
  Matrix[i][j] = 0
  #print(Matrix[i][j])

v = int(input("enter no of vertices"))
linesr = drawPolygon(v,Matrix,win)
#print(lines)
class Side:
    def __init__(self, line):
        x0,y0,x1,y1 = line
        if y1 < y0:
            x0,y0,x1,y1 = x1,y1,x0,y0
        self.X = x0
        self.ymx = y1
        self.ymn = y0
        if y1!=y0:
            self.slope = (x1-x0)/(y1-y0)

def scanline(lines,Matrix):
    edge = list()
    print(lines)
    for line in lines:
        if line[1]!=line[3]:
            edge.append(Side(line))
    #edge = sorted(edge)
    activeedge = list()
    y=-300
    while (len(edge)>0 or len(activeedge)>0) and y<=300:
        i=0
        while i<len(edge):
            if edge[i].ymn == y:
                activeedge.append(edge[i])
                edge.pop(i)
            else:
                i+=1
        i=0
        while i<len(activeedge):
            if y == activeedge[i].ymx:
                activeedge.pop(i)
            else:
                i+=1
        #activeedge = sorted(activeedge)
  #fill
        f=0
        for x in range(-300,300):
            for e in activeedge:
#mi = round(y-300)#mj = round(edge.+300)
                if int(e.X) == x:
                    f+=1
                    f=f%2
            if(f==1):
                #print(x,y)
                pt = Point(x,y)
                pt.draw(win)
        y += 1
        for e in activeedge:
            e.X += e.slope

#colour = input("Enter colour to fill with")
#clickPt = win.gedgeMouse()
scanline(linesr,Matrix)
win.getMouse()
win.close()

scl.py
Displaying scl.py.
