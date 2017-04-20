from ch8_17_pointClass import Point

def main():
    x1,y1,x2,y2= input("Enter two points x1, y1, x2, y2:").split(",")
    p1 = Point(float(x1.strip()),float(y1.strip()) )
    p2 = Point(float(x2.strip()),float(y2.strip()))
    
    print("Distance between points:" , str(round(p1.distance(p2),1)))
    print(p1.__str__())
    if p1.isNearby(p2):
        print("Points are nearby")
    else:
        print("Points are not near each other")
       
      
main()