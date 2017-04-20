import random

## binary sort 
def binarySort(list1):
    for i in range(0,len(list1)-1):  ## start with index 0 
        currmin = list1[i] ##  curent value is saved in a variable considered as min value
        print("outer",i,currmin)
        for j in range(i+1, len(list1)):  ## start another loop to loop through i+1 index to end of list
            if list1[j] < currmin:  ## if element found which is ess then outer curr element then save index and element
                currmin=list1[j]
                curindex=j
                print("inner", currmin,curindex)
        print(list1)
        if curindex != i :  ## if that element is not equal to the element prevoiusly selelcted in outer loop then swap and continue looping till oter loop reaches the end
             list1[i],list1[curindex] =list1[curindex],list1[i] ##swap
             print(list1)

## insertion sort 
def insertionSort(list1):
    for i in range(1,len(list1)):
        ## save current value into a temp variable 
        currentelement=list1[i]
        ## now set the pointer to index one less than current index
        k=i-1
        ## check if the vlaue at previous index is grater than the current value then 
        ## at the next index (k+1) insert previous value (k) and decrement k while K>=0 and value at k is grater than currvalue
        while k>=0 and list1[k] > currentelement:
            list1[k+1]=list1[k]
            k = k-1 
        ## when out of while loop at K+1 index place the current value. ( since k+1 matches value of i
        list1[k+1]=currentelement
        
        
def main():
    list1=[]
    for i in range(1,10):
        list1.append(random.randint(0,100))
    list1=[73, 82, 24, 96, 76, 75, 55, 32, 98]
    print(list1)
#     random.shuffle(list1)
#     list1.insert(2, 11)
    list1.extend(list1)
    print(list1)
#     binarySort(list1)
    insertionSort(list1)
    print(list1)

main()