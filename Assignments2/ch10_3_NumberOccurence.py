'''
Sharad: Count number of occurances of number 
'''
numbrstring= input("Enter integers between 1 and 100 separated by space:")

## make the number list 
list1=numbrstring.split()
list1.sort()

for i in range(1,len(list1)):
    k=i-1
    if list1[k] == list1[k+1]:
        elem=list1[k]
    else:
        elem=list1[k]
        cnt=0
        cnt = list1.count(elem)
        if cnt > 0 :
            print ("Number " + str(elem) +  " occurs " +  str(cnt) + " times" )
        else:
            print ("Number " + str(elem) +  " occurs " +  str(cnt) + " time" )