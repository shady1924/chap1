import sys
import os.path

## /Users/sharadagnihotri/Documents/workspace/chap1/Assignments2/ch8_ex2_CheckSubStrings.py

def main():
    vowels={ 'A','E','I','O','U'}
    filname=input("Enter the name of the file:").strip()
#     filname="/Users/sharadagnihotri/Documents/workspace/chap1/Assignments2/ch11_10_largestrws_cols.py"
    if not os.path.isfile(filname):
        print("file does not exists")
        sys.exit()    
    infile=open(filname, "r")

    vowelscnt={}
    for lin in infile.readlines():
        linset= set( x.upper() for x in lin )

        for i in (linset & vowels):
            if i in vowelscnt:
                vowelscnt[i] +=1
            else:
                vowelscnt[i] =1

    print(vowelscnt)
    infile.close()
    
main()