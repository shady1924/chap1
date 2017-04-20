printflag = True;

def decimalToHex(decimalval):
    hexvalue = 0  ## starting point as 0 
    hex = ""
    printflag and  print("decimalval received ", decimalval)
    while decimalval != 0 :
        hexvalue = decimalval % 16  ## get the remainder 
        hex = getHexCharValue(hexvalue) + hex ## get hex character 
        decimalval = decimalval//16  ## get the quotient
        printflag and  print("decimal val left is ", decimalval,"hex val", hex, "hexvalue", hexvalue)
    return hex
        

def getHexCharValue(hexvalue):
    if 0 <= hexvalue <= 9 :
        printflag and print("return value is ", chr(hexvalue))
        return chr(hexvalue + ord('0'))   ## add the hex value of 0 to the input value 
    else:
        printflag and print("return value is ", chr(ord('A') + (hexvalue - 10)))
        return chr(ord('A') + (hexvalue - 10))  ## subtract 10 from current hex values since we already handled that and add it to hex value of A

def main():
    hexretval=decimalToHex(4000000)
    print(hex(4000000))
    print("Hexval is:" ,hexretval )

main()