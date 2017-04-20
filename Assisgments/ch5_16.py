'''
Sharad: (Compute the greatest common divisor) For Listing 5.8, another solution to find
the greatest common divisor of two integers n1 and n2 is as follows: First find d to
be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2.
'''

n1= eval(input("Enter number 1 for finding GCD:"))
n2= eval(input("Enter number 2 for finding GCD:"))
gcd=0
#ensure n1 is always greater
d=n2 if n1>n2 else n1
##loop and check which number divides both n1 and n2, break from loop   
for i in range(d,1,-1) :
    if (n1%i) == 0 and (n2%i) == 0:
        break

print("gcd is:", i)