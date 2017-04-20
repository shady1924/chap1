def sumDigits(intsum,num1,len):
    if len <0 :
        return intsum
    else:
        intsum += int(num1[len])        
        return sumDigits(intsum,num1,len-1)

def main():
    num1=int(input("Enter an Integer: "))
#     print(len(num1))
    intsum=0
    print("Sum of digits of the integer is :" + str(sumDigits(intsum,str(num1),len(str(num1))-1)))

main()