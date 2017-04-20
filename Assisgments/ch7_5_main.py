from Assisgments.ch7_5 import RegularPolygon

def main():
    p1=RegularPolygon()
    p2=RegularPolygon(6,4)
    p3=RegularPolygon(10, 4, 5.6, 7.8)
    
    print("polygon1 area:" , p1.getArea(p1.getN(),p1.getSide()), "Polygon perimeter is:", \
          p1.getPerimiter(p1.getN(),p1.getSide()) )
    print("polygon2 area:" , p2.getArea(p2.getN(),p2.getSide()), "Polygon perimeter  is:", \
          p2.getPerimiter(p2.getN(),p2.getSide()))
    print("polygon3 area:" , p3.getArea(p3.getN(),p3.getSide()),  "Polygon perimeter  is:", \
          p3.getPerimiter(p3.getN(),p3.getSide()))

main()