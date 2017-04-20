'''
Sharad: (Display the first days of each month)
'''
year = eval(input("Enter the value for the year:"))  ## 2013
dy = eval(input("Enter the integer value for the day the week:"))  ## 2
daysinmonth = 0

## 0 sunday , 6 saturday.
for month in range(0, 12):
    ## check appropriate number of days in month 
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        daysinmonth = 31
    if month == 4 or month == 6 or month == 9 or month == 11:  
        daysinmonth = 30
    if month == 2:
        daysinmonth = 29 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 28
    mnth=month+1
    ## take the mod on the the days in month and add the starting day to the mod to get the first day of next month
    dy = (daysinmonth +dy )%7
    ## for given month do if else for the day and print the output
    if mnth == 1:
        if dy == 0 :
            print("January 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("January 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("January 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("January 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("January 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("January 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("January 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 2:
        if dy == 0 :
            print("Feburary 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("Feburary 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("Feburary 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("Feburary 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("Feburary 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("Feburary 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("Feburary 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 3:
        if dy == 0 :
            print("March 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("March 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("March 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("March 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("March 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("March 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("March 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 4:
        if dy == 0 :
            print("April 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("April 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("April 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("April 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("April 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("April 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("April 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 5:
        if dy == 0 :
            print("May 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("May 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("May 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("May 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("May 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("May 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("May 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 6:
        if dy == 0 :
            print("June 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("June 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("June 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("June 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("June 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("June 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("June 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 7:
        if dy == 0 :
            print("July 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("July 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("July 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("July 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("July 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("July 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("July 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 8:
        if dy == 0 :
            print("August 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("August 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("August 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("August 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("August 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("August 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("August 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 9:
        if dy == 0 :
            print("September 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("September 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("September 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("September 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("September 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("September 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("September 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 10:
        if dy == 0 :
            print("October 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("October 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("October 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("October 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("October 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("October 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("October 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 11:
        if dy == 0 :
            print("November 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("November 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("November 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("November 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("November 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("November 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("November 1,"+ str(year) + " is "+  "Saturday")
    elif mnth == 12:
        if dy == 0 :
            print("December 1,"+ str(year) + " is "+  "Sunday")
        elif  dy == 1 :
            print("December 1,"+ str(year) + " is "+  "Monday")
        elif  dy == 2 :
            print("December 1,"+ str(year) + " is "+  "Tuesday")
        elif  dy == 3 :
            print("December 1,"+ str(year) + " is "+  "Wednesday")
        elif  dy == 4 :
            print("December 1,"+ str(year) + " is "+  "Thursday")
        elif  dy== 5 :
            print("December 1,"+ str(year) + " is "+  "Friday")
        elif  dy == 6 :
            print("December 1,"+ str(year) + " is "+  "Saturday")