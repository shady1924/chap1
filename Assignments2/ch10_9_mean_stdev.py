'''
Sharad: calculate mean and stdwv
'''
printflag=False

def mean(x):
    sm=sum(x)
    cnt=len(x)
    if cnt  > 0 :
        printflag and  print(sm,cnt)
        return sm/cnt
    else:
        return 0

def stddev(meanval, lst):
    cnt=len(lst)
    sm=0
    for i in range(0,len(lst)):
        sm = sm+(lst[i]-meanval)**2  ## do summation
        printflag and  print(lst[i], round((lst[i]-meanval)**2,2))
    ## if list is not empty,
    if cnt  > 0 :
        printflag and  print(sm/(cnt-1))
        return (sm/(cnt-1))**(1/2)  ## it is important to put 0.5 instead of 1/2 since 1/2 gives wrong values. Use (1/2)
    else:
        return 0

def main():
    numbrstring= input("Enter integers separated by space:")
    lst1=[]
    temp=numbrstring.split()

    for i in range(0, len(temp)):
        lst1.append(float(temp[i]))
    
    print(lst1)
    meanval=round(mean(lst1),2)
    print("Mean is: " +  str(meanval))
    print("Standard deviation is: " + str(stddev(meanval, lst1)))
  
main()