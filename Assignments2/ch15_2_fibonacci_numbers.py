def main():
    f0 = 0
    f1 = 1
    index = 5
    j=2
    currentfib = 0
    while j <=   (index  ): 
        currentfib = f0 + f1
        f1 = currentfib
        f0 = f1
        j= j + 1
    
    print ("current fibonacci number is: " +  str(currentfib) )

    
main()
