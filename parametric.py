#parametric
from graphics import *
from gfig import Bresenham
def clip():
	n=[[-1,0],[1,0],[0,1],[0,-1]]
	pe=[[xmin,ymax],[xmax,ymin],[xmax,ymax],[xmin,ymin]]
	D=[x1-x0,y1-y0]
	te=0
	tl=1
	for i in range(4):
		num=[x0-pe[i][0],y0-pe[i][1]]
		num=-((num[0]*n[i][0])+(num[1]*n[i][1]))
		den=n[i][0]*D[0]+n[i][1]*D[1]
		if(den==0):
			print("parallel lines")
			break
		t=num/den
		if(den>0):
			tl=min(tl,t)
		else:
			te=max(te,t)
	print(tl,te)
	print(x0+D[0]*te,y0+D[1]*te,x0+D[0]*tl,y0+D[1]*tl)
	l = Line(Point(x0+D[0]*te,y0+D[1]*te) , Point(x0+D[0]*tl,y0+D[1]*tl))
	l.setFill('red')
	l.draw(win)

win = GraphWin('Parametric',300,300)
win.setCoords(-300,-300,300,300)
Bresenham(-300,0,300,0,win,"black")
Bresenham(0,400,0,-400,win,"black")
x0=int(input("Enter x0:"))
y0=int(input("Enter y0:"))
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
Bresenham(x0,y0,x1,y1,win,"black")

xmin=int(input("Enter xmin : "))
ymin=int(input("Enter ymin : "))
xmax=int(input("Enter xmax : "))
ymax=int(input("Enter ymax : "))
rec=Rectangle(Point(xmin,ymin) , Point(xmax,ymax))
rec.draw(win)
clip()

win.getMouse()
win.close()
