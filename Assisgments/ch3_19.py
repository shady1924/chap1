'''
Sharad:(Turtle: draw a line) Write a program that prompts the user to enter two points
and draw a line to connect the points and displays the coordinates of the points,
'''
import turtle

x1,y1 = eval(input("Enter x,y co-ordinates for point 1 separated by comma:"))
x2,y2 = eval(input("Enter x,y co-ordinates for point 2 separated by comma:"))

##logic to void overlap of text on line under certain scenarios 
yd1 = y1-10 if y1<0 else y1 +10 
yd2 = y2-10 if y2<0 else y2 +10 

turtle.penup()
turtle.goto( x1, y1)
turtle.pendown()
turtle.goto( x2, y2)

turtle.penup()
turtle.goto( x1, yd1)
turtle.pendown()
turtle.write(str( "(" + str(x1) + "," + str(y1) +" ) ") )

turtle.penup()
turtle.goto( x2, yd2)
turtle.pendown()
turtle.write(str( "(" + str(x2 ) + "," + str(y2) +" ) ") )

turtle.done()