'''
Sharad:  Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display
the future day of the week
'''

#currday=0
#dayinfuture=31
currday=eval(input("Enter a todays day:"))
dayinfuture=eval(input("Enter the number of days elapsed since today:"))
curdaystr=""
futuredaystr=""
## validate the data entered between 0 and 7 
if  ( 0 <= int(currday) <= 7 )  :
    futureday=(currday+dayinfuture)%7 if (currday+dayinfuture)>7 else (currday+dayinfuture)
    ##map code to day
    if  currday == 0 :
        curdaystr="Sunday"
    elif currday == 1 :
        curdaystr="Monday"
    elif currday == 2 :
        curdaystr="Tuesday"
    elif currday == 3 :
        curdaystr="Wednesday"
    elif currday == 4 :
        curdaystr="Thursday"
    elif currday == 5 :
        curdaystr="Friday"
    elif currday == 6 :
        curdaystr="Saturday"
    else :
        print("Currday Enter valid day")
    
    print("futureday ", futureday)
    
    if  futureday == 0:
        futuredaystr="Sunday"
    elif futureday == 1:
        futuredaystr="Monday"
    elif futureday == 2:
        futuredaystr="Tuesday"
    elif  futureday == 3:
        futuredaystr="Wednesday"
    elif futureday == 4:
        futuredaystr="Thursday"
    elif  futureday == 5:
        futuredaystr="Friday"
    elif  futureday == 6:
        futuredaystr="Saturday"
    else :
        print("Future Enter valid day")
    print("Today is ", curdaystr, "Day in Future is", futuredaystr)
else:
    print("Enter the the input between 0 and 7")