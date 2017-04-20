'''
Sharad:Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid,
'''
strj=""
stri=""
strd=""
n1= eval(input("Enter the number of lines:"))
#width for printing
wid=n1*10
for i in range(1,n1+1):
    strj=""
    stri=""
    ##backward loop to print number in reverse 
    for j in range ( i, 1,-1):
        strj += " " + str( j ) + " "
    ##forward loop to print the numbers         
    for k in range ( 1, i+1,1):
        stri += " " + str( k) + " "
        #concatenate the string
    strd=strj+stri
#     print it in the center using ^
    print ('{:{align}{width}}'.format(strd, align='^', width=wid))