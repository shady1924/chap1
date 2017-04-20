str1=input("Enter String 1:")
str2=input("Enter String 2:")

matched=None
printflag=True
matchcnt=0
lenst2=len(str2)
for i in range(0,len(str1) - len(str2) -1):
#     if (str1[i] == str2[0]): ## if the character in outer string matches the second string first character
        print(i,str1[i:i+len(str2)], len(str2))
#         temp1=str1[1:len(str2)]
        matched=None
        j=0
        while j <  len(str2) and i+j < len(str1)-1: ## loop through each character of the search word, start at current pos of string and go to len of word 
            print(j)
            if str1[i+j] == str2[j]:  ## check if subsequent characters in string match the word 
                matched=True
            else:
                matched=False
                break
            j+=1
            
        if matched:
            matchcnt +=1
        else:
            continue
print("there were " + str(matchcnt) + " occurences of word " + "\"" + str2 + "\"" + " in " + "\"" + str1 + "\"")