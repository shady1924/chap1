import math

a, b, c = eval(input("Enter 3 sides of the triangle separated by comma:"))


if a + b < c or b + c < a or c + a < b :
    print("Please enter valid values for sides of a triangle (sum of 2 sides is always greater than third side)")
else:
    angleARad = math.acos((a * a - b * b - c * c) / (-2 * b * c))
    angleBRad = math.acos((b * b - a * a - c * c) / (-2 * b * c))
    angleCRad = math.acos((c * c - a * a - b * b) / (-2 * b * c))
    ConvertToDegreeFactor = (180 / 22) * 7
    AngleADeg = math.ceil(angleARad * ConvertToDegreeFactor)
    print("angle A is ", math.ceil(angleARad * ConvertToDegreeFactor) , end=" / ") 
    print("angle B is ", math.ceil(angleBRad * ConvertToDegreeFactor) , end=" / ")
    print("angle C is ", math.ceil(angleCRad * ConvertToDegreeFactor) , end=" / ")
    
    math
