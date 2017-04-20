##Write a program that prompts the user to enter a monthly saving amount and \
#displays the account value after the sixth month.

printFlag=False
validationFlag=False
Principal=eval(input("Enter monthly savings amount:"))
## Formula P (1 + r/n)**(nt)
monthlyInterest=0.05/12
##first month 
value=100*(1 + monthlyInterest)
##second month 
value=(Principal + value)*(1 + monthlyInterest)
##third month 
value=(Principal + value)*(1 + monthlyInterest)
##fourth month 
value=(Principal + value)*(1 + monthlyInterest)
##fifth month 
value=(Principal + value)*(1 + monthlyInterest)
##sixth month 
value=(Principal + value)*(1 + monthlyInterest)
print("After the sixth month, the account value is", format(value,'0.2f'))