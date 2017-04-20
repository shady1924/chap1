import random
'''
(Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws. 
'''
compis=""
useris=""

compwincnt=0
usrwincnt=0
while compwincnt <3 and  usrwincnt <3:
    compinput=random.randint(0,2)
    usinput=eval(input("Enter number between 0 and 2: "))

    if compinput == 0 :
        compis="scissor"
    elif compinput == 1:
        compis="rock"
    elif compinput == 2 :
        compis="paper"
          
    if usinput == 0 :
        useris="scissor"
    elif usinput == 1:
        useris="rock"
    elif usinput == 2 :
        useris="paper"
    
    if usinput > compinput:
        usrwincnt +=1
        print("Computer is ", compis, "You are ",  useris , "You win ")        
    elif usinput == compinput:
        print("Computer is ", compis, "You are ",  useris , "Its a draw")
        usrwincnt,compinput = usrwincnt,compinput
    else :
        compwincnt += 1
        print("Computer is ", compis, "You are ",  useris , "Its a loose")        
    