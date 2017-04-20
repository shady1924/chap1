import random
printflag=False

def main():
    c=[]
    for i in range(0,4):
        c.append([])
        for j in range(0,4):
            c[i].append(random.randint(0,1))
    
    for i in c:
        print (i)
    
    maxsmrw=0
    smrw=0
    maxrwindex=-1 
    cnt=0        
    for row in c:
        smrw=0
        for val in row :
            smrw=smrw+val
        if smrw > maxsmrw:
            maxsmrw = smrw
            maxrwindex=cnt
        cnt = cnt +1
    print("largest row index is :", maxrwindex)


    maxcolindex=-1 
    cnt=0 
    maxsmcl=0
    for col in range(len(c[0])):
        smcl=0
        for row in range(len(c)):
            smcl = smcl + c[row][col]
        if smcl > maxsmcl:
            maxsmcl = smcl
            maxcolindex=cnt
#         print(c[row][col],end ='')
        cnt = cnt +1            
            
    print("largest col index is", maxcolindex)
main()
