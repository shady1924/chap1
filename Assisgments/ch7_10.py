import time 
class Time:
    def __init__(self):
        currtime = time.time()
        totalSeconds = int(currtime)
        currentSecond = totalSeconds % 60
        totalMinutes = totalSeconds // 60
        totalHours = totalMinutes // 60
        
        self.__second = currentSecond
        self.__minute = totalMinutes % 60
        self.__hour=  totalHours % 24
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setTime(self, elapseTime):
        totalSeconds = int(elapseTime)
        currentSecond = totalSeconds % 60
        totalMinutes = totalSeconds // 60
        totalHours = totalMinutes // 60
        
        self.__second = currentSecond
        self.__minute = totalMinutes % 60
        self.__hour=  totalHours % 24