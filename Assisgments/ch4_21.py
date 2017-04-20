'''
Sharad:  (Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week.
'''
##get inputs
year = eval(input("enter year:"))
j = year // 100
k = year % 100
m = eval(input("enter month: 1-12:"))
q = eval(input("enter day of the month: 1-31:"))

##check the special conditions for jan and feb 
if m==1 or m==2:
    m=13 if m==1 else 14
    year=year-1
    j = year // 100
    k = year % 100   
##run the formulae
h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7

##print respective day of week
if h==0 :
    print("Day of the week is Saturday")
elif h==1 :
    print("Day of the week is Sunday")
elif h==2 :
    print("Day of the week is Monday")    
elif h==3 :
    print("Day of the week is Tuesday")     
elif h==4 :
    print("Day of the week is Wednesday")  
elif h==5 :
    print("Day of the week is Thursday")  
elif h==6 :
    print("Day of the week is Friday")                 

