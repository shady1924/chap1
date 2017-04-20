'''
Sharad: Count characters in a string, ASSUMPTION: count characters only between a-z, A-Z, rest will be ignored.
'''
def countLetter(str):
    cnt=0
    for j in str:    
        if  ( (ord('A')<= ord(j) <= ord('Z')) or  ((ord('a')<= ord(j) <= ord('z') )) ):
            cnt +=1 
    return cnt

def main():
    str = input("Enter a String:")
#     for i in str :
#         print(ord(i))
    cnt=countLetter(str)
    print("Number of letters in the string is: ", int(cnt))
main()