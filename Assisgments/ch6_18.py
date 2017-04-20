import random 

def printMatrix(n):
# loop for rows 
    for i in range(n):
#         loop for columns 
        for j in range(n):
            print (random.randint(0,1), end = " ")
#         move to next line once the all columns are printed 
        print()

def main():
#     get input 
    inputnumber=eval(input("Enter the number for matrix:"))
#     call printmatrix 
    printMatrix(inputnumber)

main()