import turtle
## get co ordinates for point 1
x1,y1 = eval(input("Enter the x and y coordinates for point 1 separated by comma:"))
print("Numbers are ", x1, y1)
## get co ordinates for point 2 
x2,y2 = eval(input("Enter the x and y coordinates for point 1 separated by comma:"))
print("Numbers are ", x2, y2)

distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print("Distance is :",  distance)

turtle.penup()
turtle.goto(x1,y1)
#turtle.penup()
turtle.pendown()
turtle.goto(x2,y2)

turtle.done()
