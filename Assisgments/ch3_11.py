## Sharad:program to reverse a four digit number WITHOUT using loops

num = eval(input("Enter a four digit number:"))

revnum =""
if len(str(num)) != 4 :
    print("Enter 4 digit number")
else:
    ## get the last digit of the number using mod and append to variable
    revnum += str(int(num%10))
    ##get the remaining digits after the last digit has been removed as a result of division by 10
    num = int(num/10)
    revnum += str(int(num%10))
    num = int(num/10)
    revnum += str(int(num%10))
    num = int(num/10)
    revnum += str(int(num%10))
    num = int(num/10)            
    print(revnum," ", num )