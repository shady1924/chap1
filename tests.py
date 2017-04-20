import random


'''
print (format(12312324.2342342, '30.3f') )

print('%10s' % ('test',))

print("/" + '{:<10}'.format('test') + "/" )

print("/" + format(57,'50.2%' ) + "/")
print("/" + format(0.573242340,'<50.2%' ) + "/")

print("/" + format (22342342,'<x') +"/"   )

print(format ( 31 ,'b') )

print (format(int('11111',2)))



print( int(5.1**2) )
print( int(5**2) )

#print(format (9.75,"$0.2f") )

print('{0}{1}'.format('$', '9.75', ' ') )


rand1 = random.randint(100,999)   
src=rand1
lastdigit1 = src%10
remaindernum= src//10

src=remaindernum
lastdigit2 = src%10 
remaindernum= src//10 

src=remaindernum
lastdigit3 = src%10 
remaindernum= src//10

for i in range (ord('A'),ord('z') ):
    print (i, chr(i) ) 

print(ord('A'), ord('a'),ord('Z') ) 


for i in range(0,10):
    print( ord(str(i)), i)

    
import re
# prg=re.compile("[[()[\]{}]]")
# result=re.sub(r'[[()[\]{}]]' , repl, "print(\"largest row index is :\", maxrwindex)")
# print(result)
def addspace(m):
    print(m.group(0))
    return " "+m.group(0)+" "


import re
# regex = re.compile(r"[[()[\]{}]]", re.IGNORECASE)
text="print(\"largest () row  {} index is :\", maxrwindex)"
print( re.sub(r"[(){}:]", addspace , text) )
# print( re.findall(r"[(){}]", text) ) 


list1 = [2, 3, 5, 2, 33, 21, "sharad"]
print(len(list1), list1[-4:-2])
list1.remove(100)
print(list1)

'''
str1 =  "sharad agnihotri"
str2 = "sharad"
print( str2 in str1)