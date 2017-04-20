import turtle
import random
import math
# def drawLine(x1, y1, x2, y2, color = "black", size = 1):
   
# # get distance between two points 
def getDistance(x1, y1, x2, y2):
    return abs(((x2 - x1) ** 2 + (y2 - y2) ** 2) ** 0.5)  ## return absolute value
    
# Draw a point at the specified location (x, y) and optionally print he point number ( fro debugging)
def drawPoint(x, y,ptnum=""):
    turtle.penup()  # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown()  # Pull the pen down     
    turtle.begin_fill()  # Begin to fill color in a shape
    turtle.write(ptnum)
    turtle.circle(1)
    turtle.end_fill()  # Fill the shape
    
# Draw a circle centered at (x, y) with the specified radius
def drawCircle(color="black", x=0, y=0, radius=50):
     turtle.penup()  # Pull the pen up
     turtle.goto(x, y - radius)
     turtle.pendown()  # Pull the pen down
     turtle.circle(radius)
    
# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(color="black", x=0, y=0, width=30, height=30):
     turtle.penup() 
     turtle.goto(x + width / 2, y + height / 2)
     turtle.pendown() 
     turtle.right(90)
     turtle.forward(height)
     turtle.right(90)
     turtle.forward(width)
     turtle.right(90)
     turtle.forward(height)
     turtle.right(90)
     turtle.forward(width)

def main():
    turtle.showturtle()
    rectx,recty,wid,heigth=-75, 0, 100, 100
    drawRectangle("black", rectx,recty,wid,heigth)
    cirx,ciry,rad=50,0,50
    drawCircle("black", cirx,ciry,rad)
    cntcirclepts = 0
    cntrectpts = 0
    
    while cntcirclepts <= 10:
        ## generate the random variables for x,y for the point 
        x, y = random.randint(cirx-int(rad/2)  , cirx+int(rad/2) ), random.randint(ciry-int(rad/2) ,ciry+int(rad/2) )
        ## get distance between random point and center of the circle
        dist=getDistance(cirx,ciry,x, y)
        ## draw the point if the distance between the point and center is less than radius
        if (dist < rad ) :
            print("count", cntcirclepts, x, y , "distance:", dist,  cirx,ciry, rad)
            drawPoint(x, y)
            cntcirclepts +=1  ### increment the loop counter , exit when 10 
            
    while cntrectpts <= 10:
        x, y = random.randint(rectx-int(wid/2)  , rectx+int(wid/2) ), random.randint(recty-int(heigth/2) ,recty+int(heigth/2) )
        dist=getDistance(rectx,recty,x, y)
        ## draw the point if the distance between the point and center is less than width/2 and height/2        
        if (dist < wid/2 ) or (dist < heigth/2 ) :
            print("count", cntcirclepts, x, y , "distance:", dist,  cirx,ciry, rad)
            drawPoint(x, y)
            cntrectpts +=1  ### increment the loop counter , exit when 10 
                        
    turtle.done()


main()
