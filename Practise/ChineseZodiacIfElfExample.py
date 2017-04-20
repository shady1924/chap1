import math

UsrInput= eval(input("Enter the year as yyyy:"))

yr=UsrInput%12
print("year is" + str(yr) )
if yr == 0 :
    print("Zodiac Sign is Monkey")
elif yr == 1:
    print("Zodiac Sign is Rooster")
elif yr == 2:
    print("Zodiac Sign is Dog")  
elif yr == 3:
    print("Zodiac Sign is Pig")  
elif yr == 4:
    print("Zodiac Sign is Rat")  
elif yr == 5:
    print("Zodiac Sign is OX")  
elif yr == 6:
    print("Zodiac Sign is Tiger")  
elif yr == 7:
    print("Zodiac Sign is Rabit")  
elif yr == 8:
    print("Zodiac Sign is Dragon")  
elif yr == 9:
    print("Zodiac Sign is Snake")
elif yr == 10:
    print("Zodiac Sign is Horse")
elif yr == 11:
    print("Zodiac Sign is Sheep")     
else :
    print("Cannot calculate Zodiac")