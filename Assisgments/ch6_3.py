'''
Sharad:  Return the reversal of an integer, e.g. reverse(456) returns
# 654
'''
printflag=False
# function to resere the number and return reversed number 
def reversal(inputnum):
    rem=inputnum
    revstr="0" if inputnum ==0 else ""  ##special check for 0 
    ld=0 ## last digit default 0 
    while rem !=0:  ## while remaining digits are !=0 
        ld = rem%10 ## extract last digit 
        rem = int(rem//10)
        revstr = revstr + str(ld)
        printflag and print ("ld:",ld,"rem:", rem,"retstr", revstr)
    return revstr

def isPalindrome(inputnum):
    retval=reversal(inputnum)
    printflag and print("retval", len(str(retval)),"inputnum", len(str(inputnum)) )
    #return true is input is same as reversed string
    return True if int(retval) == inputnum else False
     

def main():
    inputnum=eval(input("Enter an interger to be tested for palindorme:"))
    #retflag=isPalindrome(inputnum)
    if isPalindrome(inputnum):
        print("Its palindrome")
    else:
        print("Its NOT palindrome")
        
main()