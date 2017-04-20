'''
Sharad: reverse list 
'''
numbrstring= input("Enter list of integers separated by space:")

list1=numbrstring.split()

print("original list:", end =" ") 
print(list1)
print("Reversed list:", end =" ") 
list1.reverse()
print (list1)
