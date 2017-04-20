from Assisgments.ch7_7 import LinearEquation

def main():
#     1.0, 2.0, 2.0, 4.0, 4.0, 5.0 no solution 
#     9.0, 4.0, 3.0, -5.0, -6.0, -21.0  solution 
    # obj1 = LinearEquation(9.0, 4.0, 3.0, -5.0, -6.0, -21.0)
    a, b, c, d, e, f = eval(input("Enter the values for a,b,c,d,e,f: "))
    obj1 = LinearEquation(a, b, c, d, e, f)    
    if obj1.isSolvable():
        print("The value for x is:", obj1.getX(), "value for y is:", obj1.getY())
    else:
        print("Equation is not solvable")
    
main()
