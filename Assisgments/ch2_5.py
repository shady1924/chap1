##Program to read the subtotal and the gratuity rate and computes the gratuity and total
##setup printflag to print strings
printFlag=True
##enter values for gratuity and subtotal
subtotal, gratuityrate = eval(input("Enter gratuity rate and sub-total for the bill separated by comma :"))
##Check to see if values are not negative
if subtotal <= 0 and gratuityrate <= 0 :
    print("Enter non negative value for rate and sub-total")
else:
    ##calculate gratuity value
    gratuity = subtotal * (gratuityrate / 100)
    printFlag and print("gratuity is gratuity",gratuity )
    print("Total is ", str(subtotal+gratuity))