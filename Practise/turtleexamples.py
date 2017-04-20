import turtle
'''
turtle.showturtle()
turtle.write("Welcome to Python")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.color("red")
turtle.right(90)
turtle.forward(100)
turtle.color("green")
turtle.right(45)
turtle.forward(100)
'''
turtle.showturtle()

# #print Y axis 
turtle.penup()
turtle.goto(0, 200)
turtle.right(90)
turtle.pendown()
turtle.forward(400)
turtle.home()

# #print x axis
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.forward(400)
turtle.home()

# print Circle 1 
x, y,radius  = 0, 40, 20  
# Circle 2 
x2, y2, radius2 = 0, 0, 80 

turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot("red")
turtle.write(str(turtle.position()) + " " + str(radius) + " (c1)")

turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

# print circle 2

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot("red")
turtle.write(str(turtle.position()) + " " + str(radius2) + " (c2)")
turtle.penup()
turtle.goto(x2, y2 - radius2)
turtle.pendown()
turtle.circle(radius2)


# #print line joining centers
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.goto(x2, y2)
# # enter the distance between points 
distance = int(((x2 - x) ** 2 + (y2 - y) ** 2) ** (1 / 2))
turtle.penup()
turtle.goto((x + x2) / 2, (y + y2) / 2)
turtle.pendown()
turtle.write(" ( " + str(distance) + " ) ")


## Logic to print the text 
txt="blank"
# Two point intersection 
if abs(radius - radius2) < distance   and  distance < abs(radius + radius2)  :
    txt="Circles 1 and Circle2 intersect at 2 points"
## One point intersection
elif abs(radius - radius2) == distance or abs(radius + radius2) == distance:
    txt="Circles 1 and Circle2 intersect at one point and circle 1 is outside circle2" if abs(radius - radius2) == distance \
    and radius > radius2 else "Circles 1 and Circle2 intersect at one point and circle 2 is outside circle 1"
## Non Intersection condition 
elif distance > abs(radius + radius2)  or   distance < abs(radius - radius2) :
    txt="Circle do not intersect and circle 1 is outside circle 2" if distance > abs(radius + radius2) else \
    "Circle do not intersect and circle 1 is inside circle 2"  if radius2 > radius else \
    "Circle do not intersect and circle 2 is inside circle 1" 
elif radius==radius2 and x==x2 and y==y2  :
    txt="Circles Overlap Each Other"    
else:
    txt="Error: Something Wrong"
    
    
### print various shapes using circle method
turtle.penup()
winwidth, winheight= turtle.screensize()
turtle.goto(-winwidth*0.70 , -winheight*0.80 )
turtle.pendown()
print("winwidth" , winwidth , winheight)
print("Circle1" , x ,",",y,",", radius)
print("Circle1" , x2 ,",",y2,",", radius2)
print("Distance:",str(distance) )
turtle.penup()
turtle.color("red")
turtle.write(txt, font=("Arial", 12, "normal"))
turtle.goto(0 , 0 )
turtle.color("black")
#turtle.circle(radius,360,5) 

turtle.done()
