#cohen-sutherland algorithm
from graphics import *
from gfig import Bresenham
inside = 0
left = 1
right = 2
top = 8
bottom = 4

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

def compute(x1,y1):
	out = inside
	if(x1<xmin):
		out = left
	if(x1>xmax):
		out = right
	if(y1 < ymin):
		out = bottom
	if(y1 > ymax):
		out = top

	return out

def clipping(x0,y0,x1,y1,win):
	outp1 = compute(x0,y0)
	outp2 = compute(x1,y1)
	accept = False
	print(outp1,outp2)

	while True:
		if(outp1 == 0 and outp2 == 0):
			accept = True
			break #point inside
		elif(outp1&outp2)!= 0:
			break
		else:
			outcode = max(outp1,outp2)
			if outcode & top:
				y = ymax
				x = x0 + (x1-x0)*(y-y0/y1-y0)
				#print('t')
			elif outcode & right:
				x = xmax
				y = y0 + (x-x0)*(y1-y0)/(x1-x0)
				#print('r')
			elif outcode & bottom:
				x = x0 + (x1 - x0)*(ymin - y0) / (y1 - y0)
				y = ymin
				#print('b')
			elif outcode & left:
				y = y0 + (y1 - y0)*(xmin - x0) / (x1 - x0)
				x = xmin
				#print('l')
			#print(x,y)
			#print(outcode)
			if(outcode == outp1):
				x0 = x
				y0 = y
				outp1 = compute(x0,y0)
				#print('b')
			else:
				x1 = x
				y1 = y
				outp2 = compute(x1,y1)


	if accept:
		Bresenham(x0,y0,x1,y1,win,"red")
	else:
		print("Line rejected")




x0,y0 = input("enter point1").split()
x1,y1 = input("enter point2").split()
Bresenham(int(x0),int(y0),int(x1),int(y1),win,"yellow")
clipping(int(x0),int(y0),int(x1),int(y1),win)
win.getMouse()

