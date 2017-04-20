from test.test_pprint import list2

printflag=True

def binarySearch(list1,elem):
#     if list1 == None:
#         list = []
    listlen= len(list1)-1
    mid=listlen//2
    low=0
    high=listlen
    printflag and print([a for a in range(0,listlen+1)])
    printflag and print(list1)
    while high >= low:
        mid=(low+high)//2   ## set mid value 
        if list1[mid] == elem: ## if element passed is equal to middle value   
            return mid
        elif elem < list1[mid] :  ## if element value is less than value at middle point 
            high=mid-1
        else :
            low=mid+1  ## if element is greater than middle value then increase the low value.

        printflag and high >= low and print( " " +  str(listlen) + " " + "["+str(low)+"]" + str(list1[low]) +  " " \
                             "["+str(mid)+"]" + str(list1[mid]) +  " " \
                             "["+str(high)+"]" + str(list1[high-1]) )

    
    return -low-1  ## return -1 if element not found


def main():
    list1 = [1,32,45,67,6,89,435,345,7768,789,890,45,34,23,345,567,90]
    list1.sort()

    elem=890
    if ( binarySearch(list1,elem) >= 0 ):
        print("Element found")
    else:
        print("Element not found")    
        
main()
