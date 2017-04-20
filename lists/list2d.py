list2d=[[1,2],
        [3,4],
        [5,6]
    ]


total=0
for col in range(0,len(list2d[0])):
    for row in (0,len(list2d)-1):
#         total += list2d[row][col]
        print (row, col , list2d[row][col] )
        print(total)
    total=0
    
print(len(list2d))

'''
student=[ ['A','B','C','D'],
         ['B','C','D','E'],
         ['A','B','B','A'],
         ['C','B','C','D']
         ]
key=['A','B','C','D']

# print (len(student[0]))

for stu in range(0,len(student)):
    grade=0
    for stugrade in range(0,len(student[0])):
        if student[stu][stugrade] == key[stugrade]:
            grade += 1
    print("student " + str(student[stu]) + "grade is" + str(100 * grade/len(key)))
'''    