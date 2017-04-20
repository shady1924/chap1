str=" John 34 Jim 45 Peter 59 Tim 45"

str2= str.split()
print(str2, len(str2))

lst=list()
i=0
j=0
while i < len(str2):
    lst.append([])
    lst[j]=[str2[i], str2[i+1]]
    i=i+2
    j=j+1
print (lst)

lst.sort(key=lambda tup: tup[1])
print (lst)