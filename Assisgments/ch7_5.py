'''
Sharad: Geometry: n-sided regular polygon
'''
import math

class RegularPolygon:
    def __init__(self, n=3, side=1 , x=0 , y=0):
        self.__n = n  ###number of sides 
        self.__side = side  ## length of side 
        self.__x = x  ## x co-ordinate of center of polygon 
        self.__y = y  ## y co-ordinate of center of polygon 
    
    def getN(self):
        return self.__n
    
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setN(self, n):
        self.__n = n 
    
    def setSide(self, side):
        self.__side = side 
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y 
    
    def getPerimiter(self, n, s):
        return n*s
    
    def getArea(self, n,s):
        area = round((n*s*s)/(4 * math.tan(math.pi/n)),4)
        return area
    