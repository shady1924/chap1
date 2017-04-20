def LongestSubstr(str1,str2):
    maxreldis=0
    maxistindex=0
    for i in range(0,len(str1)-1):
        for j in range(0,len(str2)-1):
#             print(str1[i], str2[j])
            cntr=0
            reldis=0
            if (  str1[i] == str2[j] ):
                while (j+reldis) < len(str2) and (i+reldis) < len(str1) and str1[i+reldis] == str2[j+reldis] :
                    cntr = cntr+1
                    reldis = reldis+1
            if reldis > maxreldis:
                maxreldis =reldis
                maxistindex = i
    print("Longest Common Prefix is:", str1[maxistindex:maxistindex+maxreldis])

def main():
    str1= input("Enter string 1:")
    str2= input("Enter string 2:")
    LongestSubstr(str1,str2)
    
main()