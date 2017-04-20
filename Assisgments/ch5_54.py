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

# y=10*math.radians(-360*-360)
turtle.penup()
y=100*math.radians(-100)*math.radians(-100)
turtle.goto(-100,y)
turtle.pendown()
for i in range (-100,100):
    y=100*math.radians(i)*math.radians(i)
    turtle.goto(i, y)
turtle.penup()

    
turtle.done()