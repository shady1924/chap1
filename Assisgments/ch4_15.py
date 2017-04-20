'''
Sharad: Input 4 digit number, Make program on following rules:
If the user input matches the lottery in exact order, the award is $10,000.
If the user input matches the lottery, the award is $3,000.
If one digit in the user input matches a digit in the lottery, the award is $1,000.
'''
import random

printflag=False  ##print flag

rand1 = random.randint(100,999) 
print("Lottery number is:", rand1,"\n")  

src=rand1
LotteryDigit1 = src%10
remaindernum= src//10

src=remaindernum
LotteryDigit2 = src%10 
remaindernum= src//10 

src=remaindernum
LotteryDigit3 = src%10 
remaindernum= src//10

printflag and print("Lottery digit extracted are: ", LotteryDigit1, " and " ,  LotteryDigit2 , \
                    "LotteryDigit3:", LotteryDigit3)
##get input from user
userInput=eval(input("Enter 3 digit number:") )

if len(str(userInput)) != 3 :
    print ("Entered number is not 3 digit number")
else:
    ##extract the individual digits
    src=userInput
    UserDigit1 = src%10
    remaindernum= src//10
    
    src=remaindernum
    UserDigit2 = src%10 
    remaindernum= src//10 
    
    src=remaindernum
    UserDigit3 = src%10 
    remaindernum= src//10
    
    printflag and print("Entered digits", UserDigit1 , " ", UserDigit2, " ",  UserDigit3 )
    
    printflag and print((UserDigit1 == LotteryDigit1 or UserDigit1 == LotteryDigit2 or UserDigit1 == LotteryDigit3 ) )
    printflag and print((UserDigit2 == LotteryDigit1 or UserDigit2 == LotteryDigit2 or UserDigit2 == LotteryDigit3 ) )
    printflag and print((UserDigit3 == LotteryDigit1 or UserDigit3 == LotteryDigit2 or UserDigit3 == LotteryDigit3 ) )
        
    
    ##Business Rules
    if UserDigit1 == LotteryDigit1 and UserDigit2 == LotteryDigit2 and UserDigit3 == LotteryDigit3 :
        print("Award is $10,000!!!!")
    elif (UserDigit1 == LotteryDigit1 or UserDigit1 == LotteryDigit2 or UserDigit1 == LotteryDigit3 ) and \
     (UserDigit2 == LotteryDigit1 or UserDigit2 == LotteryDigit2 or UserDigit2 == LotteryDigit3 ) and  \
     (UserDigit3 == LotteryDigit1 or UserDigit3 == LotteryDigit2 or UserDigit3 == LotteryDigit3 ):
        print("Award is $3,000!!!!")
    elif (UserDigit1 == LotteryDigit1 or UserDigit1 == LotteryDigit2 or UserDigit1 == LotteryDigit3 ) or \
     (UserDigit2 == LotteryDigit1 or UserDigit2 == LotteryDigit2 or UserDigit2 == LotteryDigit3 ) or  \
     (UserDigit3 == LotteryDigit1 or UserDigit3 == LotteryDigit2 or UserDigit3 == LotteryDigit3 ):
        print("Award is $1,000!!!")
    else:
        print("Better luck next time!!!")