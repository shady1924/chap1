

def hextoDecimal(hex):
    decimalvalue = 0
    for i in range(len(hex)):  # # get each character from hex value
        ch = hex[i] 
        if  '0' <= ch <= '9' or 'A' <= ch <= 'F' :  
            decimalvalue = decimalvalue * 16 + gethextoDecimal(chr(i))    
        else:
            return None
    return decimalvalue

def gethextoDecimal(ch):
    if  'A' <= ch <= 'F' :
        return 10+ ord(ch) - ord('A') 
    else:
        return ord(ch) - ord('0') 

def main():
    hexvalue = "AB8C"
    decimalvalue = hextoDecimal(hexvalue)
    print(decimalvalue)

main()
    
