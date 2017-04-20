def isMarkovMatrix(m):
    flag=True
    for row in range(len(m)):
        sum=0        
        for col in range(len(m[row])):
            if int(float(m[row][col])) < 0:
                flag=False
            sum = sum + float(m[col][row])
        if sum != 1:
            flag=False
    return flag
            
        

def main():
#     c = [ '0.15 0.875 0.375'.split(), '0.55 0.005 0.225'.split(), '0.30 0.12 0.4'.split()]    
    c = [ '0.95 -0.875 0.375'.split(), '0.65 0.005 0.225'.split(), '0.30 0.22 -0.4'.split()]       
#     print (c)
    retval=isMarkovMatrix(c)
    if retval:
        print("Matrix is markov martix")
    else:
        print("Matrix is NOT markov martix")
main()