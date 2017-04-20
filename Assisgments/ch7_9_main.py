from Assisgments.ch7_9 import LinearEquationWithPoints

def main():
#     2.0, 2.0, 0, 0
#     0, 2.0, 2.0, 0
    x1, y1, x2, y2 = eval(input("Enter the end points for first line: "))
    x3, y3, x4, y4 = eval(input("Enter the end points for second line: "))
    obj1 = LinearEquationWithPoints(x1, y1, x2, y2, x3, y3, x4, y4)    
    if obj1.isSolvable():
        print("Intersecting point is: (", obj1.getX(), ",", obj1.getY(), ")")
    else:
        print("Equation is not solvable")
    
    
main()
