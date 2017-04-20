def biggestNumberInList(list1):
    for i in (0,len(list1)-1,1):
        j=0
        while j < len(list1)-1:
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                print(i, j, list1[j+1] , list1)
            j += 1
        print(list1)
    
    
def main():
    list1=[60,5,1,100,2,200,6]
    #print(list1)
    biggestNumberInList(list1)

main()