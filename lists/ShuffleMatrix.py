import random
'''
matrix=[[1,2,3],[3,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
print(matrix)

for row in range(len(matrix)):
    #print (row, matrix[row])
    for value in range(len(matrix[row])):
        i=random.randint(0,len(matrix)-1)
        j=random.randint(0,len(matrix[row])-1 )
        
        #print(value, matrix[row][value])
        #exchange
        matrix[row][value],matrix[i][j]=matrix[i][j],matrix[row][value]

print(matrix)
'''
matrix=[]
for row in range(0,5):
    matrix.append([])
    for col in range(random.randint(0,5)):
        matrix[row].append(col)

print(matrix)