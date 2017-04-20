num  =  eval(input("Enter an number") )

if num%2 ==0 and num%3==0:
	print("Number is divisible by 2 and 3")
elif num%2 ==0 or num%3==0:
	print("Number is divisible by 2 or by 3")
else:
	print("Number not divisible by either 2 or 3")
	
if (num%2 ==0 or num%3==0)  and not (num%2 ==0 and num%3==0 ):
	print("Number is divisible by 2 or by 3 but not both")
