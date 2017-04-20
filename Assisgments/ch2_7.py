##Sharad: A a program that prompts the user to enter the minutes (e.g., 1 billion),
## and displays the number of years and days for the minutes
##without using loops
printFlag=False
validationFlag=False
print("test input value",str(3*365*24*60 + 7*24*60) ) 
inputval=eval(input("Enter an integer value for number of minutes:"))
inputDays=int(inputval/60/24)
printFlag and print("Type of input values is" , type(inputval))
if type(inputval) is not int :
    print("\tPlease enter the integer value not decimal value")
    validationFlag=True
else:
    numYear=int(inputDays/365)
    daysLeft=int( (inputDays - int(numYear*365) ) )
    printFlag and print("Number of years is ",numYear)
    printFlag and print("Number of days is ",daysLeft)
print(inputval, " minutes is approximately" ," years ", numYear, " and " ,daysLeft,  "days "  )  if  not validationFlag  else \
print("\t***Validation failed for input value, cannot calculate data***") 