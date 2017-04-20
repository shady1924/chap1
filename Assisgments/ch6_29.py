'''
Sharad: (Financial: credit card number validation)
It must have between 13 and 16 digits, and the number must start with:
■ 4 for Visa cards
■ 5 for MasterCard credit cards
■ 37 for American Express cards
■ 6 for Discover cards
'''

printflag = False  #print flag

# Return true if the card number is valid
def isValid(number):
    numsiz = getSize(number)
    prefix = getPrefix(number, 1)
    ## check condition for length of card and that it's prefix belogn to set to predefined values
    if (13 <= numsiz <= 16) and (getPrefix(number, 1) == 4 or getPrefix(number, 1) == 5 or \
                                  getPrefix(number, 2) == 37  or getPrefix(number, 1) == 6) :
        printflag and print("Card first check validated")
        ## check the logic for even and odd digits
        if ( (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10) == 0  :
            print("Card is Valid")
        else:
            print("Card is invalid")
    else:
        print("Credit Card is NOT valid ")
    

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    num = number
    sum = 0
    ld = 0
    cnt = 1
    while num != 0 :
        ld = getlastdigit(num)
        num = removelastdigit(num)
        if cnt % 2 == 0:
            doublenum = 0
            doublenum = ld * 2
            ## if doubling the number gives a number of length > 1 then add the digits of the number
            if getSize(doublenum) > 1:
                sum += getDigit(doublenum) ## sum  the digits of the two digit number and add it to total sum 
            else :
                sum += doublenum  ##else just add the number to sum
            printflag and print("sumOfDoubleEvenPlace: sum of even digit is:", sum, "last digit:", ld, "doublenum:",ld * 2,"cnt:",cnt )
        cnt += 1
    return sum  

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    num = number
    sum = 0
    ld = 0
    cnt = 1
    while num != 0 :
        ld = getlastdigit(num)
        num = removelastdigit(num)
        ## logic to add odd digits
        if cnt % 2 != 0:
            sum += ld 
        cnt += 1
        printflag and print("sumOfOddPlace: sum of odd digit is:", sum, "last digit:", ld, "doublenum:",ld * 2,"cnt:",cnt )
    return sum  
      
# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    if getSize(number) == 1 :
        return number
    else :
        num = number
        sum = 0
        ld = 0
        while num != 0 :
            ld = getlastdigit(num)
            num = removelastdigit(num)
            sum += ld
        printflag and print("getDigit: sum of digit is:", sum, "number passed is:", number)
    return sum

# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    cursiz = getSize(int(d))
    prefix = getPrefix(number, cursiz)
    printflag and print("prefixMatched: card prefix prefix:", prefix , type(prefix), d, type(d))
    return True if d == prefix else False
    

# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(inputnum, k):
    numlen = getSize(inputnum)
    divisor = 10 ** (getSize(inputnum) - k)
    prefix = inputnum // divisor
    printflag and print("getPrefix:prefix:", prefix, "inputnum:", inputnum, "k:", k)
    return prefix if numlen > k else inputnum

def getlastdigit(num):
    d = num % 10
    return int(d)

def removelastdigit(num):
    d = int(num / 10)
    return d

# Return the number of digits in d
def getSize(d):
    num = d
    cnt = 0
    ld = 0
    while num != 0 :
        ld = getlastdigit(num)
        num = removelastdigit(num)
        cnt += 1
    # printflag and print("num:", num, "ld", ld, "num", num , cnt)
    return cnt

def main():
    # valid num 4388576018410707
    # invalid num 4388576018402626  
    inputnum = eval(input("Enter the credit card number as Integer number:"))
    if (type(inputnum) is int):
        printflag and print("Number is:", inputnum)
        isValid(inputnum)
    else:
        print("**Wrong Input***..Try Again !!! Please Enter Integer value")

main()
