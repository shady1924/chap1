'''
tuple2 = tuple([7, 1, 2, 23, 4, 5])
tuplestr=("How are you" )
print((tuple2[2:4]))

print(len(tuplestr))
print(tuple2[-1])

## set 
s1=set()
s2={1,2,3,4}
print(s2)
s3= set([x * 2 for x in range(1, 10)])

set1 = {"green", "red", "blue", "red"}

set3 = set1 ^ { "" , "green", "yellow" }
set1.remove("red")
print(set3)


## dictionaries 

students = {"111-34-3434":"John", "132-56-6290":"Peter"}

for key in students:
    print(key, students[key] )


t1 = (1, 2, 3, 7, 9, 0, 5)
t2 = t1
print(t1 == t2 )


s1 = {1, 2, "Absdc"}
print(len(s1))  
# print(s1[0])  


students = {"peter", "john", 1 , 3 }
students.remove(0)
print(students)


s = {1, 3, 4}
# s = {{1, 2}, {4, 5}}
# s = {[1, 2], [4, 5]}
s = {(1, 2), (4, 5)}
print (s)
'''
s1 = {1, 4, 5, 6}
s2 = {1, 3, 6, 7}
print(s1 ^ s2)

