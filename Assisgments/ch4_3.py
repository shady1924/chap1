#Sharad:  #solve 2X2 linear equations
a,b,c,d,e,f= eval(input("Enter 6 numbers separated by comma:"))

if (a*d -b*c) == 0:
    print("The equation has no solution")
else:
    x= (e*d -b*f)/(a*d - b*c)
    y= (a*f -e*c)/(a*d - b*c)
    print ("value of x is ",  format(x,'0.1f') )
    print ("value of x is ",  format(y,'0.1f') )