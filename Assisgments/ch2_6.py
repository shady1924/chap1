##Sharad: A program that reads an integer between 0 and 1000 and adds all the digits in the integer
##without using loops
digitsSum=0
printFlag=False
validationFlag=False
inputval=eval(input("Enter a value between 0 and 1000:"))

#Check that user input is type int only to prevent other junk values crashing program
if type(inputval) is not int :
    print("\tPlease enter the integer value")
    validationFlag=True
##Check if the user entered value between requested range
elif inputval <0 or int(inputval//1000) > 0 :
    print("\tPlease enter value between 0 and 1000")
    validationFlag=True
else:
    ##extract first digits 
    lastExtractedDigit=int(inputval%10)
    remainderval=int(inputval//10)
    digitsSum=lastExtractedDigit
    printFlag and print("value", str(lastExtractedDigit), " , ", str(remainderval)   )
    ##extract seconds set of digits 
    if remainderval > 0 :
        lastExtractedDigit=int(remainderval%10)
        remainderval=int(remainderval//10)
        digitsSum=digitsSum+lastExtractedDigit
        printFlag and print("IT2: value", str(lastExtractedDigit), " , ", str(remainderval)   )
    ##extract last set of digits if number entered is 3 digits number
    if remainderval > 0 :
        lastExtractedDigit=int(remainderval%10)
        remainderval=int(remainderval//10)
        digitsSum=digitsSum+lastExtractedDigit
        printFlag and print("IT3: value", str(lastExtractedDigit), " , ", str(remainderval)   ) 
print("\tSum of digits for input value is:", digitsSum)  if  not validationFlag  else \
print("\t***Validation failed for input value, cannot calculate data***") 