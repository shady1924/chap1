'''
Make program on following rules:
If the user input matches the lottery in exact order, the award is $10,000.
If the user input matches the lottery, the award is $3,000.
If one digit in the user input matches a digit in the lottery, the award is $1,000.
'''
import random

printflag=True  ##print flag

rand1 = random.randint(10,99) 
print("Lottery number is:", rand1,"\n")  

LotteryDigit1= int(rand1/10)
#print("Enter the digits", LotteryDigit1)
LotteryDigit2= rand1-(LotteryDigit1*10)
printflag and print("Lottery digit extracted are: ", LotteryDigit1, " and " ,  LotteryDigit2 )
##get input from user
userInput=eval(input("Enter 2 digit number:") )

if int((userInput/100)) > 0 :
    print ("Entered number is not 2 digit number")
else:
    ##extract the individual digits
    UserDigit1= int(userInput/10)
    UserDigit2= userInput - (UserDigit1)*10
    printflag and print("Entered digits", UserDigit1 , " ", UserDigit2)
##Business Rules
if UserDigit1 == LotteryDigit1 and UserDigit2 == LotteryDigit2 :
    print("Award is $10,000!!!!")
elif UserDigit1 == LotteryDigit2 and UserDigit2 == LotteryDigit1:
    print("Award is $3,000!!!!")
elif ( UserDigit1 == LotteryDigit1 or UserDigit1 == LotteryDigit2 ) or ( UserDigit2 == LotteryDigit1 or  UserDigit2 == LotteryDigit2):
    print("Award is $1,000!!!")
else:
    print("Better luck next time!!!")