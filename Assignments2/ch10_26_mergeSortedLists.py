##sharad: merge 2 sorted lists

printFlag=False
lst1=[1,5,5,6,7,21,61,111]
lst2=[2,4,5,6,29]

##check which list is bigger, we will choose the smaller list as driving loop to increase performance
if len(lst1) > len(lst2):
    lstbig,lstsmall =lst1,lst2
else:
    lstbig,lstsmall =lst2,lst1

printFlag and print(id(lstbig), id(lstsmall), id(lst1), id(lst2), len(lst1), len(lst2)) 

print(lstsmall)
print(lstbig) 

lst3=list()
i=0
while  i < len(lstsmall) -1:
    ## check if current element of smalllst is less than current element of biglist and 
    ## also check if next eleement of small list is greater than current element of big list
    ## the sorted element (lower value is from small list and higher value is from big list , append  to the new sorted list 
    if lstsmall[i] <= lstbig[i] and lstbig[i] <= lstsmall[i+1] :
        first=lstsmall[i]
        second=lstbig[i]
        lst3.append(first)
        lst3.append(second)
    ## check if current element of smalllst is less than equal to current element of biglist and 
    ## also check if next element of small list is less than current element of big list
    ## the sorted element (lower value is from small list and higher value is from next lement of small list , append  to the new sorted list         
    elif ( lstsmall[i] <= lstbig[i] and lstbig[i] >= lstsmall[i+1] ) :
        first=lstsmall[i]
        second= lstsmall[i+1]
        lst3.append(first)
        lst3.append(second)        
    ## if small element is greater thent he biglist element then lower value is from biglist and higher value is from smalllist
    elif lstsmall[i] > lstbig[i] :
        first=lstbig[i]
        second=lstsmall[i]
        lst3.append(first)
        lst3.append(second)        
    else:
        printFlag and print("Inside Else:")
    printFlag and print ("list ")
    printFlag and print("iteration: " + str(i) + " first:"  +  str(first) + " second:" + str(second)  +  " lstsmall[i]:" + \
          str(lstsmall[i] )  + " lstsmall[i+1]:"  + str(lstsmall[i+1]) + " lstbig[i]:" + str(lstbig[i]) )
    i=i+1

##after we have compared elements in small list then compare last element of small list with last element of big list
## and append remaining of elements from big list to new list.
i=len(lstsmall)-1
while i <  len(lstbig):  
    if i < len(lstsmall)  and  lstsmall[i] < lstbig[i]  :
        lst3.append(lstsmall[i])
        lst3.append(lstbig[i])        
    elif i < len(lstsmall) and lstsmall[i] > lstbig[i]  :
        lst3.append(lstbig[i])
        lst3.append(lstsmall[i])        
    else:
        lst3.append(lstbig[i])
    printFlag and  print (i)
    i=i+1
print("sorted list" , lst3)