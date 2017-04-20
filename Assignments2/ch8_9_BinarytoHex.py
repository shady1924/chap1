'''
Sharad: Binary to Hex
'''

def BinaryHex(str1):
    i=len(str1)
    sm=0
    j=0
    while i >=0 and j<=len(str1)-1:
#         print(str1[i-1])
        sm = sm + (int(str1[i-1]))*(2**(j))
        j=j+1
        i = i-1 
#         print(int(str1[i-1]), i,j,sm)
    decimaltoHex(sm)

def decimaltoHex(decimalVal):
    hexval=""
    while decimalVal !=0 : 
        remaindr=decimalVal%16
        hexval= str(getHexChar(remaindr) ) + hexval
        decimalVal=decimalVal//16
    print('{0}0x{1}'.format("Hex number is:", hexval))

def getHexChar(remaindr):
    if  0 <= remaindr <= 9  :  ## if reaminder between 0 and 9 then add ascii value of 0 to remainder and return char at that ascii value 
        return chr(remaindr + ord('0') )
    else:
        ## if remainder between 10 and 15 then reduce 10 from that remainder (eg 10-5 = 5) add the remaining value to ascii of 'a'
        ## and get the ascii value of char at remaining value + ascii val of 'a' and return it.
        return chr(  ord('a')  + remaindr -10   ) 
    
def main():
    str1=input("Enter a binary number:")
#     str1='1111110000'
#     print(str1,  int(str1,2), hex( int(str1,2) ))
    BinaryHex(str1)
    

main()