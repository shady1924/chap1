def letterDigitCheck(str):
    lettercnt=0
    digcnt=0
    retflag=True
    errcode=""
    for i in str:
        if ( ord('a') <= ord(i) <= ord('z')  or ord('A') <= ord(i) <= ord('Z')  or ord('0') <= ord(i) <= ord('9') ):
            if ord('a') <= ord(i) <= ord('z')  or ord('A') <= ord(i) <= ord('Z'):
                lettercnt = lettercnt+ 1
#                 print("i:", i, lettercnt ) 
            elif ord('0') <= ord(i) <= ord('9'):
                digcnt = digcnt + 1 
#                 print("i:", i, digcnt )
            else:
                retflag=False
        else:
            retflag=False
            errcode=errcode + "Password String contains characters other than char and digits \n"
    if digcnt < 2:
        retflag=False
        errcode=errcode + "Digits less than 2 \n"
    return  errcode  

def main():
    userstr=input("Enter the password string:")
#     userstr = "abcs19241!"
    
    if len(userstr) < 9:
        print("Password check failed, password has less than 9 characters length")
    errtxt=letterDigitCheck(userstr)
    if errtxt != "":
        print("Password check failed, Error String:", errtxt )
    else:
        print("It worked!!!" )
        

main()
