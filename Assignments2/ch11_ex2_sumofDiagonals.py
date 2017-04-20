def sumMajorDiagonal(m):
    sum =0 
    for rows in range(len(m)):
        for cols in range(len(m[rows])):
            if rows==cols:
                sum = sum + m[rows][cols]
    return sum
                 

def main():
    matrix=[[1,2,3,4],[5,6.5,7,8],[9,10,11,12],[13,14,15,16]]
    sum=sumMajorDiagonal(matrix)
    print("sum is:",  str(sum))
main()