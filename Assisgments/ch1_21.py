'''Sharad Agnihotri
Date: 01/11/2017
program to draw a clock showing time as 9:15 using turtle 
'''

import turtle

turtle.showturtle()
turtle.showturtle()
#lift pen up 
turtle.penup()
##go towards the negative y axis so that circle is drawn in center of screen 
turtle.goto(0,-200)
## show current location of cursor 
turtle.showturtle()
# put pen down  
turtle.pendown()
## draw a circle with radius of 200 pix
turtle.circle(200)
## draw hour arm and minute arm 
turtle.penup()
turtle.goto(150,0)
turtle.pendown()
turtle.left(180)
turtle.color("red")
turtle.forward(150)
turtle.color("blue")
turtle.forward(150)
## draw seconds arm 
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("green")
turtle.right(90)
turtle.forward(150)
## write the text at the bottom of figure
turtle.penup()
turtle.right(90)
turtle.goto(-10,-210)
turtle.pendown()
turtle.write("09:15:00")

turtle.done()