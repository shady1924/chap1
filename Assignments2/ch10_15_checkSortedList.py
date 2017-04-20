printFlag=False
def isSorted(lst):
    sortedFlag = True
    for i in range(0, len(lst) - 1):
        j = i + 1
        printFlag and  print("i:",i,"j",j)
        while j > 0 :
            if lst[j] < lst[j - 1]:
                printFlag and print("value j:",lst[j],"value at j-1",lst[j-1])
                sortedFlag = False
                break
            j = j - 1
        if sortedFlag == False:
            break
    
    return sortedFlag

def main():
    numbrstring = input("Enter sorted list of integers separated by space:")
    lst1 = []
    temp = numbrstring.split()

    for i in range(0, len(temp)):
        lst1.append(int(temp[i]))
    
    if (isSorted(lst1)) :
        print("List is already sorted")
    else:
        print("List is Not sorted")
    
main()
