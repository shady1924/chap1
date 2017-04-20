import turtle
'''
 A program that prompts the user to enter the center of a 
 rectangle, width, and height, and displays the rectangle
 '''

x, y, width, height = eval(input("Enter center of triangle along with width and height:"))
#x, y, width, height = 50,50,100,150

if width > 0 and height > 0 :
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x,y)
    ##from center goto half of width and turn right
    turtle.goto(x+width//2,y)
    turtle.pendown()
    turtle.right(90)
    ##move forward half of height and turn right
    turtle.forward(height//2)
    turtle.right(90)
    ##move forward full width and turn right 
    turtle.forward(width)
    turtle.right(90)
    ##move forward full height , turn right and move forrward full width and turn right
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    ##come back to starting 
    turtle.forward(height//2)
    turtle.done()
else:
    print("***Enter positive values for width and height***")