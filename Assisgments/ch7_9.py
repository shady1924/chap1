class LinearEquationWithPoints:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3      
        self.__x4 = x4
        self.__y4 = y4                     
    # ## getters    
    def getX1(self):
        return self.__x1
    
    def getY1(self):
        return self.__y1
    
    def getX2(self):
        return self.__x2

    def getY2(self):
        return self.__y2
    
    def getX3(self):
        return self.__x3

    def getY3(self):
        return self.__y3           

    def getX4(self):
        return self.__x4

    def getY4(self):
        return self.__y4   
    
# #  setters 
    def setX1(self, x1):
        self.__x1 = x1
    
    def setY1(self, y1):
        self.__y1 = y1
    
    def setX2(self, x2):
        self.__x2 = x2 

    def setY2(self, y2):
        self.__y2 = y2
    
    def setX3(self, x3):
        self.__x3 = x3 

    def setY3(self, y3):
        self.__y3 = y3       
        
    def setX4(self, x4):
        self.__x4 = x4 

    def setY4(self, y4):
        self.__y4 = y4               

    def isSolvable(self):
        result = ((self.__x1 - self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 - self.__x4)) 
        return True if result != 0 else False 
     ## return X calculated value of intersecting point
    def getX(self):
        result = ((self.__x1 * self.__y2) - (self.__y1 * self.__x2)) * (self.__x3 - self.__x4) - (self.__x1 - self.__x2) * (self.__x3 * self.__y4 - self.__y3 * self.__x4)  \
        / ((self.__x1 - self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 - self.__x4)) 
        return result
    ## return Y calculated value of intersecting point
    def getY(self):
        result = ((self.__x1 * self.__y2) - (self.__y1 * self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 * self.__y4 - self.__y3 * self.__x4)) / ((self.__x1 - self.__x2) * (self.__y3 - self.__y4) - (self.__y1 - self.__y2) * (self.__x3 - self.__x4))
        return result
