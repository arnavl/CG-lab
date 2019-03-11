#besky
from gfig import Bresenham
from graphics import *

win = GraphWin('clsc',300,300)
win.setCoords(-300,-300,300,300)


def clip():
	p=[-x1+x0,x1-x0,-y1+y0,y1-y0]
	q=[x0-xmin,xmax-x0,y0-ymin,ymax-y0]
	Dx=x1-x0
	Dy=y1-y0
	te=0
	tl=1
	for i in range(4):
		if(p[i]<0):
			te=max(te,q[i]/p[i])
		elif(p[i]>0):
			tl=min(tl,q[i]/p[i])

	print(tl,te)
	l = Line(Point(x0+Dx*te,y0+Dy*te) , Point(x0+Dx*tl,y0+Dy*tl))
	l.setFill('red')
	l.draw(win)

x0=int(input("Enter x0:"))
y0=int(input("Enter y0:"))
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
l = Line(Point(x0,y0) , Point(x1,y1))
l.setFill('blue')
l.draw(win)

xmin=int(input("Enter xmin : "))
ymin=int(input("Enter ymin : "))
xmax=int(input("Enter xmax : "))
ymax=int(input("Enter ymax : "))
rec=Rectangle(Point(xmin,ymin) , Point(xmax,ymax))
rec.draw(win)
clip()
win.getMouse()
win.close
