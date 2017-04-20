import sys
import os.path
import re
def addspace(m):
    return " "+m.group(0)+" "

def main():
    keywords={ "import", "open", "input", "for", "readline","range", "if", "and", "def", "append","and"}
    escapes=["(", ")", ":", "{", "}"]
#     filname=input("Enter the name of the file:").strip()
    filname="/Users/sharadagnihotri/Documents/workspace/chap1/Assignments2/ch11_10_largestrws_cols.py"
    if not os.path.isfile(filname):
        print("file does not exists")
        sys.exit()    
    infile=open(filname, "r")

    wrdcnt={}
    for lin in infile.readlines():
        ## put a space before and after some special characters so that keyword gets separated by a space
        lin1=re.sub(r"[(){}:]", addspace , lin)  
        lindict= set(lin1.split())
#         print(lindict) 
        for i in (lindict & keywords):
            if i in wrdcnt:
                wrdcnt[i] +=1
            else:
                wrdcnt[i] =1

    print(wrdcnt)
    infile.close()
    
main()