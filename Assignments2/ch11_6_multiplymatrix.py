printflag=False
def multiplyMatrix(a, b):
    c=[]
    '''
    for rows in range(len(a)):
        c.append([])
        sum=0
        for col in range(len(a[rows]) ):
            sum=0
            sum = sum + a[rows][col]*b[col][rows]
            c[rows].append(sum)
    ''' 
    for  rowsa in range(len(a)):
        c.append([])
        for  rowsb in range(len(b)):
            sum =0
            for colb in range(len(b[rowsb]) ):
                sum = sum + a[rowsa][colb]*b[colb][rowsb]
                printflag and print( a[rowsa][colb], b[colb][rowsb] ,  round(a[rowsa][colb] * b[colb][rowsb],2) ,round( sum ,2) )
            c[rowsa].append(round(sum,2))
            printflag and print() 
    
    return c
def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[0 , 2 , 4] ,[1 , 4.5 , 2.2] ,[1.1 , 4.3, 5.2]]
    if (len(matrix1) * len(matrix1[0])) !=  (len(matrix2) * len(matrix2[0])):
        print("Matrices are not of same dimensions")
    else:
        matrix3 = multiplyMatrix(matrix1, matrix2)
    printflag and  print("sum is:", str(matrix3))
    
    print("Final Matrix:")
    for rows in matrix3:
        print("[", end='')
        for value in rows:
            print (str(value) + " " , end ='' ) 
        print("]", end='')
        print()
    
main()
