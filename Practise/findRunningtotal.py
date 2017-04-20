list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(0,len(list1),1):
    sum=sum+list1[i]
    list1[i]=sum
# list1.reverse()
# print(list1)    
import numpy as np
arr=[1,2,3,4,5,6,7,8,9,10]
data1= np.array([1,2,3,4,5,6,7,8,9,10])
print(data1.sum()-data1)