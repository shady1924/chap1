c = [[23.5 ,35 ,2 ,10], [4.5 ,3 ,45 ,3.5], [35 ,44 ,5.5, 11.6]]
maxval=c[0][0]

rowind=0
maxrwind=0
maxclind=0
for row in c:
    colind=0
    for value in row:
        if value > maxval:
            maxrwind=rowind
            maxclind=colind
            maxval=value
#             print(value, maxval, rowind ,colind , maxrwind,maxclind )
        colind = colind +1
    rowind = rowind +1
         
print("location of largest element is at: (" + str(maxrwind) + ","  + str(maxclind) + ")" )            
            