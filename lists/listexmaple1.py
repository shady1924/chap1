'''
list1 = [1,2,3,4,5]
print(list1, id(list1))
list1.append(100)
print(list1,id(list1))
list1.insert(30, 102)
print(list1,id(list1), len(list1))
list1.insert(-1, 106)
print(list1,id(list1))
list1.sort()
print(list1,id(list1))
list1.extend([111,222,333])
print(list1,id(list1), len(list1))

list1.pop(-3)
print(list1,id(list1), len(list1))

str="abcdef"
list1=list(str)
print(len(list1))
for i in range(len(list1)-1,0,-1):  ### the loop has to go one element less than lenght of list 
    print(list1[i], end="")   
    print()
    
list1= [x for x in range(0,5)]
print(list1)
list1 =[0.5 * x for x in list1]
print(list1)

list2="Welcome#t##the#world".split("#")
list1=list(list2)
print(id(list1),id(list2))

list1 = list(99*["False"])
print(list1)
'''

list1=26*[0]
list1[21]=44
print(list1)