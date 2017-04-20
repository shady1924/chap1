def binaryToDecimal(binaryString):
    decimalval=0
    return decimaltoBinaeryHelper(binaryString, len(binaryString)-1, decimalval)


def decimaltoBinaeryHelper(binaryString, indx,  decimalval):            
        if indx < 0:
            return decimalval
        else:
            binaryval=int(binaryString[indx])   ## get the binary digit at given index 
            powerval=(len(binaryString) -1 - indx) ## get the value of power to which 2 will be raised, length of string - current index -1 
            decimalval = decimalval + int(binaryString[indx])*(2**(len(binaryString) -1 - indx) )   ## do the sum 
            indx = indx -1  ## decrement the index value  
            return decimaltoBinaeryHelper(binaryString, indx,  decimalval)
               
def main():
#     binstr=int(input("Enter a binary string:"))
    binstr="100"
    print(binaryToDecimal(str(binstr)))

main()