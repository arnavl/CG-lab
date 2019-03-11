# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from graphics import *
import math
def main():
    #assigning values to window port
     xwmin=-500
     ywmin=-500
     xwmax=500
     ywmax=500
    
     #generating window
     win=GraphWin("2D Transformation ",xwmax-xwmin,ywmax-ywmin)
    
     #this will change the cordinate system into 4 quardant
     win.setCoords(xwmin,ywmin,xwmax,ywmax)
    
     #setting the basic properties to display
     win.setBackground("white")
     #t0=Text(Point(15,10),"(0,0)")
     #t0.draw(win)
    
     #y-axis
     yaxis_line=Line(Point(0,ywmin),Point(0,ywmax))
     yaxis_line.setArrow("both")
     yaxis_line.draw(win)
    
     #x-axis
     xaxis_line=Line(Point(xwmin,0),Point(xwmax,0))
     xaxis_line.setArrow("both")
     xaxis_line.draw(win)
    
     #actual size
     #assigning values to window port
     xwmin=-200
     ywmin=-200
     xwmax=200
     ywmax=200
    
    
     win.setBackground("grey")
    
     #y-axis
     yaxis_line=Line(Point(0,ywmin),Point(0,ywmax))
     yaxis_line.setArrow("both")
     yaxis_line.draw(win)
    
     #x-axis
     xaxis_line=Line(Point(xwmin,0),Point(xwmax,0))
     xaxis_line.setArrow("both")
     xaxis_line.draw(win)
     n = int(input("Enter the number of points"))
     print("Enter the points")
     
     newX = [0]*n
     newY = [0]*n
     pointsX = []
     pointsY = []
     
     # Drawing the original polygon
     for i in range(0,n):
         xi = int(input("Enter x"))
         yi = int(input("Enter y"))
         pointsX.append(xi)
         pointsY.append(yi)
    
     line = Line(Point(pointsX[0],pointsY[0]),Point(pointsX[n-1],pointsY[n-1]))
     line.setOutline("hot pink")
     line.draw(win)
     for i in range(0,n-1):
         line = Line(Point(pointsX[i],pointsY[i]),Point(pointsX[i+1],pointsY[i+1])) 
         line.setOutline("hot pink")
         line.draw(win)
     x = 0
     while( x !=-1):
         print("1.Tranlate\n2.Scale\n3.Rotate\n4.Rotate about X - axis \n5.Rotate about Y-axis\n6.Rotate about a point\n7.Shear in X\n8.Shear in Y")
         print("8. Rotate about an arbitrary axis\nExit -> -1")
         x = int(input("Enter choice")) 
         
         if(x==1):
             #Translation    
             Tx = int(input("Enter Tx"))
             Ty = int(input("Enter Ty"))
             
             for i in range (0,n):
                 newX[i] = pointsX[i] + Tx
                 newY[i] = pointsY[i] + Ty
                 
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("green")
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("green")
                 line.draw(win)  
         elif (x==2):
             #Scaling    
             Sx = int(input("Enter Sx"))
             Sy = int(input("Enter Sy"))
             
             for i in range (0,n):
                 newX[i] = pointsX[i]*Sx
                 newY[i] = pointsY[i]*Sy
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("red")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("red")
                 line.draw(win)
         elif (x==3):       
            # Rotation
             angle = int(input("Enter angle in degrees"))
             rad = math.radians(angle)
             Cos = math.cos(rad)
             Sin = math.sin(rad)
             for i in range (0,n):
                 newX[i] = pointsX[i]*Cos - pointsY[i]*Sin
                 newY[i] = pointsX[i]*Sin + pointsY[i]*Cos
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("blue")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("blue")
                 line.draw(win)
         elif (x==4):
             for i in range (0,n):
                 newY[i] = pointsY[i]*(-1)
                 newX[i] = pointsX[i]
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("DarkOrange")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("DarkOrange")
                 line.draw(win)
         elif (x==5):
             for i in range (0,n):
                 newY[i] = pointsY[i]
                 newX[i] = pointsX[i]*(-1)
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("purple")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("purple")
                 line.draw(win)                 
         elif(x==6):
             a = int(input("Enter the x co-ordinate of the point"))
             b = int(input("Enter the y co-ordinate of the point")) 
             AOR = int(input("Enter the angle of rotation")) 
             for i in range (0,n):
                 newX[i] = pointsX[i]-a
                 newY[i] = pointsY[i]-b
                
             rad = math.radians(AOR)
             Cos = math.cos(rad)
             Sin = math.sin(rad)
             for i in range (0,n):
                 newX[i] = newX[i]*Cos - newY[i]*Sin
                 newY[i] = newX[i]*Sin + newY[i]*Cos 
             for i in range (0,n):
                 newX[i] = newX[i]+a
                 newY[i] = newY[i]+b
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("coral")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("coral")
                 line.draw(win)       
         elif(x==7):
             shy = int(input("Enter shy"))
             '''Y' = Y + Shy . X
             X’ = X'''  
             for i in range(0,n):
                 newX[i] = pointsX[i]
                 newY[i] = pointsY[i] +  shy*pointsX[i] 
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("brown")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("brown")
                 line.draw(win)
         elif(x==8):
             shx = int(input("Enter shx"))
             '''Y' = Y + Shy . X
             X’ = X'''  
             for i in range(0,n):
                 newX[i] = pointsX[i]+  shx*pointsY[i]
                 newY[i] = pointsY[i]  
             line = Line(Point(newX[0],newY[0]),Point(newX[n-1],newY[n-1]))
             line.setOutline("DarkOliveGreen")  
             line.draw(win)
             for i in range(0,n-1):
                 line = Line(Point(newX[i],newY[i]),Point(newX[i+1],newY[i+1])) 
                 line.setOutline("DarkOliveGreen")
                 line.draw(win)    
         elif(x==9):
             x0 = int(input("Enter x0"))
             y0 = int(input("Enter y0"))
             x1 = int(input("Enter x1"))
             y1 = int(input("Enter y1"))     
             line = Line(Point(x0,y0),Point(x1,y1)) 
             line.setOutline("AntiqueWhite")
             line.draw(win)               
     win.getMouse()
     win.close() 
main()
