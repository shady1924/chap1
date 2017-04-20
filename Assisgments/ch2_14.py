##A program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) 
#of a triangle and displays its area.

printFlag=False
validationFlag=False
x1,y1,x2,y2,x3,y3=eval(input("Enter three points for a triangle:"))
s1 = ((x2-x1)**2 + (y2-y1)**2)**0.5 
s2 = ((x3-x2)**2 + (y3-y2)**2)**0.5 
s3 = ((x3-x1)**2 + (y3-y1)**2)**0.5 
s = (s1 + s2 + s3)/2
printFlag and print (s1," ", s2," ", s3) 
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print("Area of triangle is:", format (area, '0.1f' ) )