'''
Sharad: (Palindromic prime) A palindromic prime is a prime number that is also palindromic. 
'''
printflag=False

def isPrime(lnum):
    divisor =2
    while divisor <= lnum/2:
        if lnum %divisor==0:
            return False ## return false saying that it is not a prime number        
        divisor += 1
    return True   ### if no number which divides the input then it is prime 

# function to resere the number and return reversed number 
def reversal(inputnum):
    rem=inputnum 
    revstr="0" if inputnum ==0 else ""  ##special check for 0 
    ld=0  ## last digit default 0 
    while rem !=0: ## while remaining digits are !=0 
        ld = rem%10 ## extract last digit 
        rem = int(rem//10) ## remove last digit 
        revstr = revstr + str(ld) # add it to string
    printflag and print ("ld:",ld,"rem:", rem,"retstr", revstr)
    return revstr  ## return value once loop finishes

def isPalindrome(inputnum):
    retval=reversal(inputnum)
    printflag and print("retval", len(str(retval)),"inputnum", len(str(inputnum)) )
    #return true is input is same as reversed string
    return True if int(retval) == inputnum else False
     
        
def main():
    cnt=0 ## counter for palindromic primes
    i=2  ## counter for numbers starting at 2 
    while cnt <100:   ## loop for 100 palindromic primes
        if isPrime(i) and isPalindrome(i):  ## if a number of both prime and pa
            print ('{:{align}{width}}'.format(str(i), align='>', width=10) , end =' ' )
            cnt +=1
            #print(cnt)
            if cnt%10 == 0:
                print()  ## print the end of line for every 10 columns 
        i += 1  ## increment to next number
    print ("\n\ntotal number of palindromic primes:", cnt )
    
main()