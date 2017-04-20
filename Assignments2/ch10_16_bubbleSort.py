printflag = False
def bubbleSort(lst):
    ln=len(lst)
    for i in range(1,ln):
        j=i-1
#         print(lst)
        while j < len(lst) -1:
            if lst[j] > lst[j+1]:  ## check if elemet on left is grater than one on right. if yes then swap
                lst[j+1],lst[j]=lst[j],lst[j+1]
            j=j+1
            printflag = False and print("i=", i, "j", j, lst[j], lst[j-1])
#             print(lst)
    
def main():
    numbrstring = input("Enter sorted list of integers separated by space:")
#     numbrstring = "5 1 4 2 8"
    lst1 = []
    temp = numbrstring.split()

    for i in range(0, len(temp)):
        lst1.append(int(temp[i]))
    
    print("Original: ", end="")
    print(lst1)
    bubbleSort(lst1)
    print("Sorted: ", end="")
    print(lst1)
        
main()