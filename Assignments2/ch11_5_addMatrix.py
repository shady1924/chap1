def addMatrix(a, b):
    c=[]
    for rows in range(len(a)):
        c.append([])
        for col in range(len(a[rows]) ):
             c[rows].append(a[rows][col] + b[rows][col])
    
    return c
def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[0 , 2 , 4] ,[1 , 4.5 , 2.2] ,[1.1 , 4.3, 5.2]]
    matrix3 = addMatrix(matrix1, matrix2)
    print("sum is:", str(matrix3))
    
    
main()
