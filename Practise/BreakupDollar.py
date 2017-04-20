dollaramount = eval(input("Enter dollar amount:"))

print("dollar value", int(dollaramount))
decimalVal = int( (dollaramount - int(dollaramount)) * 100 )
print("str", decimalVal) 
numquater = decimalVal // 25
print ("NUm Quaters amount is", numquater)
# # num dimes 
remainder = decimalVal - numquater * 25
numdime = remainder // 10
print ("Num dimes is", numdime)
# #num of nickel
remainder = remainder - numdime * 10
numnickel = remainder // 5
print ("Num nickels is", numnickel)
remainder = remainder - numnickel * 5
print ("Num cents is", remainder)

print (type(remainder))