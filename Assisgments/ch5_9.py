'''
Financial application: compute future tuition. tuition for a university
is $10,000 this year and increases 5% every year. a program that
computes the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now
'''
printflag=False
##set tuition 
tution=10000
inc=0.05
i=1
#set the variable for sum =0 
sum10=0
sum4=0
#loop 14 times 
while i <=14:
    ##calculate runnign total
    tution = round((tution + tution*inc),2)
    printflag and print("after", i, tution)
    ## if year between 10th and 14th year then find sum for cost of 4 years of education
    if i >= 10 and i<=14:
        if i == 10 :
            sum10 , sum4 = tution,tution
            printflag and print("after 10th year tuition is : ", sum10)
        else:
            sum4 = sum4 + sum4*0.05
            printflag and  print("after ", i, "year tuition is : ", sum4)
    i += 1
print("At 10th year base tuition cost will be :", '{}{}'.format("$",round(sum10,2))  )
print("Cost of 4 year tuition starting 10th year :", '{}{}'.format("$",round(sum4-sum10,2)) )