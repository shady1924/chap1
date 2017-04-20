##Sharad: Write a program that draws a triangle, square, pentagon, hexagon, and octagon
import turtle 

turtle.showturtle()
turtle.penup()
turtle.forward(-200)
turtle.pendown()
##triangle
turtle.color("red")
turtle.right(60)
turtle.begin_fill()
turtle.circle(30,360,3)
turtle.end_fill()

##quad
turtle.penup()
turtle.left(60)
turtle.forward(100)
turtle.pendown()
turtle.color("yellow")
turtle.right(45)
turtle.begin_fill()
turtle.circle(30,360,4)
turtle.end_fill()

##pentagon
turtle.penup()
turtle.left(45)
#print(turtle.heading())
turtle.forward(100)
turtle.pendown()
turtle.color("blue")
turtle.right(36)
turtle.begin_fill()
#print(turtle.heading())
turtle.circle(30,360,5)
#print(turtle.heading())
turtle.end_fill()

##hexagon
turtle.penup()
turtle.left(36)
#print(turtle.heading())
turtle.forward(100)
turtle.pendown()
turtle.color("orange")
turtle.right(30)
turtle.begin_fill()
#print(turtle.heading())
turtle.circle(30,360,6)
#print(turtle.heading())
turtle.end_fill()

##octagon
turtle.penup()
turtle.left(30)
#print(turtle.heading())
turtle.forward(100)
turtle.pendown()
turtle.color("green")
turtle.right(20)
turtle.begin_fill()
#print(turtle.heading())
turtle.circle(30,360,8)
#print(turtle.heading())
turtle.end_fill()

turtle.done()
