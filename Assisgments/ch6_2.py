'''
Sharad: (Sum the digits in an integer) Write a function that computes the sum of the digits
in an integer
'''
printflag =False 
def SumDigitis(x):
    lsum=0
    ld=0  ##last digit 
    rem=x ## remaining digits 
    printflag and print ("x", x)
    while rem !=0:
        ld = rem%10 ## extract last digit 
        rem = int(rem//10) ## remove last digit 
        lsum += ld
        printflag and print ("ld:",ld,"rem:", rem)
    return lsum
    

def main():
    dig=eval(input("Enter the digits to sum:"))
    retval=int(dig)
    retSumVal=SumDigitis(retval)
    print("Sum of digits is:", retSumVal )

main()