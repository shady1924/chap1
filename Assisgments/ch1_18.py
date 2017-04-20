'''Sharad Agnihotri
Date: 01/11/2017
program to draw a STAR figure using turtle 
'''

import turtle

turtle.showturtle()
#lift pen up 
turtle.penup()
##goto 100 pix towards x and 100 pix towards y to make the star i the center of positive xy plane
turtle.goto(100,100)
## show current location of cursor 
turtle.showturtle()
## draw line at angle of 144
turtle.right(144)
# put pen down  
turtle.pendown()
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.done()