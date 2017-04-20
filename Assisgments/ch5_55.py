'''
Sharad: Write a program to draw the 8X8 chess board 
'''
import math
import turtle

y=0
x=0
i=0
printflag=False
#x axus 
turtle.showturtle()
turtle.speed(0)
# flag for the first col of row 
coloFlag=False  ### false means black
# flag for the alternating cells 
rowcolorflag=True ### true means white
printflag=False ##print flag 
#     loop for 8 rows
for row in range(1,9):
    ## flip the flag for row and cell 
    coloFlag=not coloFlag
    rowcolorflag = coloFlag 
#     loop for 8 cols
    for col in range(1,9):
        turtle.pendown()
        turtle.right(45)
        rowcolorflag = not rowcolorflag
        printflag and print("rowcolorflag", rowcolorflag)
#         flip the color
        xcolor= "black" if rowcolorflag==True  else "white"        
#         choose fill color 
        turtle.fillcolor(xcolor)
        turtle.begin_fill()
#         draw the circle 
        turtle.circle(20,360,4)
        turtle.end_fill()
#         set the correct angle parallel to x axis 
        turtle.left(45)
#         move forward one block 
        turtle.forward(27)
    turtle.penup()
#     goto to start to draw second row 
    turtle.goto(0,row*27)

turtle.done()