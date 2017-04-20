class Point:
    def __init__ (self, x=0, y=0):
        self.__x = x 
        self.__y = y 

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self, p1 ):
        d= ((p1.getX() - self.__x)**2 + (p1.getY() - self.__y)**2 ) **0.5
        return d
    
    def isNearby(self,p):
        if self.distance(p ) < 5:
            return True
        else:
            False
    
    def __str__ (self):
        return "("+str(self.__x)+","+str(self.__y)+")"