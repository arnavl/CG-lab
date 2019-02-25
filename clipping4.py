#parametric 2nd one - sutherland -hodgemnan
from graphics import *
from gfig import xintersect,yintersect,Bresenham
def clipping(x1,y1,x2,y2):
	# (ix,iy),(kx,ky) are the co-ordinate values of
	# the points
	global s
	temp=[]
	print(s)
	for i in range(len(s)):
		k=(i+1) % len(s)
		ix=s[i][0]
		iy=s[i][1]
		kx=s[k][0]
		ky=s[k][1]

		# Calculating position of first point
		# w.r.t. clipper line
		i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1);

		# Calculating position of second point
		# w.r.t. clipper line
		k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1);

		# Case 1 : When both points are inside
		if(i_pos<0 and k_pos<0):
			#Only second point is added
			temp.append([kx,ky])

		# Case 2: When only first point is outside
		elif(i_pos>=0 and k_pos<0):
			# Point of intersection with edge
			# and the second point is added
			temp.append([xintersect(x1,y1, x2, y2, ix, iy, kx, ky),yintersect(x1,y1, x2, y2, ix, iy, kx, ky)])
			temp.append([kx,ky])


		# Case 3: When only second point is outside
		elif(i_pos<0 and k_pos>=0):
			#Only point of intersection with edge is added
			temp.append([xintersect(x1,y1, x2, y2, ix, iy, kx, ky),yintersect(x1,y1, x2, y2, ix, iy, kx, ky)])

	# Copying new points into original array
	# and changing the no. of vertices
	s=temp
	# print(temp)

def clip():
	# print(s)
	# print(cp)
	for i in range(4):
		k=(i+1)%4
		clipping(cp[i][0],cp[i][1],cp[k][0],cp[k][1])

	for i in range(len(s)-1):
		l=Line(Point(s[i][0],s[i][1]),Point(s[i+1][0],s[i+1][1]))
		l.setFill('red')
		l.draw(win)
	l=Line(Point(s[-1][0],s[-1][1]),Point(s[0][0],s[0][1]))
	l.setFill('red')
	l.draw(win)

win = GraphWin('Sutherland-Hodgman',300,300)
win.setCoords(-300,-300,300,300)
Bresenham(-400,0,400,0,win,"black")
Bresenham(0,400,0,-400,win,"black")

sides=int(input("Enter number of sides = "))
s=[]
temp=[]

for i in range(sides):
	temp=[]
	print("\n\nNew sides")
	x = int(input("Enter new x = "))
	y = int(input("Enter new y = "))
	temp.append(x)
	temp.append(y)
	s.append(temp)

for i in range(sides-1):
    Bresenham(s[i][0],s[i][1],s[i+1][0],s[i+1][1],win,"black")

Bresenham(s[-1][0],s[-1][1],s[0][0],s[0][1],win,'blue')

xmin=int(input("Enter xmin : "))
ymin=int(input("Enter ymin : "))
xmax=int(input("Enter xmax : "))
ymax=int(input("Enter ymax : "))
rec=Rectangle(Point(xmin,ymin) , Point(xmax,ymax))
rec.draw(win)
cp=[[xmin,ymin],[xmin,ymax],[xmax,ymax],[xmax,ymin]]

clip()

win.getMouse()
win.close()
