'''
Sharad: Write a program that plots the sine
function in red and cosine in blue
'''
import math
import turtle

y=0
x=0
i=0

#x axus 
turtle.showturtle()

turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.goto(400,0)
turtle.penup()

##y axus 
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.goto(0,200)
turtle.penup()

# sine wave 

y=100*math.sin(math.radians(-360))
turtle.goto(-360, y)
turtle.color("blue")
turtle.pendown()
for i in range (-360,360):
    y=100*math.sin(math.radians(i))
    turtle.goto(i, y)
turtle.penup()

##cos wave 
y=100*math.cos(math.radians(i))
turtle.goto(-360, y)
turtle.pendown()
turtle.color("red")
for i in range (-360,360):
    y=100*math.cos(math.radians(i))
    turtle.goto(i, y)
    
turtle.done()