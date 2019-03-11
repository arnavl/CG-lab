from gfig import drawPolygon,Bresenham
from graphics import *
win = GraphWin('gfig',300,300)
win.setCoords(-300,-300,300,300)

Matrix = [[0 for x in range(600)] for y in range(600)]
for i in range(600):
	for j in range(600):
		Matrix[i][j] = 0
		#print(Matrix[i][j])


#prevc = 0
#newc = 1
def fill(Matrix,x,y,prevc,newc,win):
	mi = round(y-300)
	mj = round(x+300)
	pt = Point(x,y)
	stack = []
	stack.append([mi,mj])
	while(stack):
		mi,mj = stack.pop(len(stack)-1)
		#print(mi,mj)
		if(Matrix[mi][mj] != newc):
			Matrix[mi][mj] = newc
			win.plot(mj-300,mi+300,"red")
		if(Matrix[mi+1][mj] != newc):
			stack.append([mi+1,mj])
		if(Matrix[mi-1][mj] != newc):
			stack.append([mi-1,mj])
		if(Matrix[mi][mj+1] != newc):
			stack.append([mi,mj+1])				
		if(Matrix[mi][mj-1] != newc):
			stack.append([mi,mj-1])


v = int(input("enter no of vertices"))
drawPolygon(v,Matrix,win)

#colour = input("Enter colour to fill with")
clickPt = win.getMouse()
fill(Matrix,round(clickPt.getX()),round(clickPt.getY()),0,1,win)
win.getMouse()
win.close()
