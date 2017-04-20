'''Sharad Agnihotri
Date: 01/11/2017
program to display the projected population for EACH of next five years WITHOUT USING LOOPS
   assumptions : 
       one birth every 7 seconds
       one death every 13 seconds 
       one new immigrant every 45 seconds
'''
##current population given in example 
CURRPOPULATION = 312032486
##seconds in a day
SECONDSINDAY = 86400
## seconds in year 
SECONDSINYEAR= 365 * SECONDSINDAY
## total births in a year 
totalbirths = SECONDSINYEAR // 7
##total deaths in a year 
totaldeaths = SECONDSINYEAR // 13
## total immigrants arriving per year
newimmigrants = SECONDSINYEAR // 45
## effective yearly increase in population  bithts - deaths + immigrants 
yearlypopincrement= totalbirths - totaldeaths + newimmigrants

print ("totalbirths:" + str(totalbirths) + "\n" + "totaldeaths:" + str(totaldeaths) + "\n" + "newimmigrants:" + str(newimmigrants) )
print("Effective increment population per year:" + str(yearlypopincrement) )
print ("\n\nYearNum \t\t population")
print ("===================================")
''' for each year multiply the yearly increment by the multiple for that year in future 
and add it to base population
''' 
print ("after 1 year      \t\t"+str(CURRPOPULATION + (yearlypopincrement * 1 ) ) )
print ("after 2 year       \t\t"+str(CURRPOPULATION + (yearlypopincrement * 2 ) ) )
print ("after 3 year       \t\t"+str(CURRPOPULATION + (yearlypopincrement * 3 ) ) )
print ("after 4 year       \t\t"+str(CURRPOPULATION + (yearlypopincrement * 4 ) ) )
print ("after 5 year       \t\t"+str(CURRPOPULATION + (yearlypopincrement * 5 ) ) )