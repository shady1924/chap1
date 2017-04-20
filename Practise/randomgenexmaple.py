import random


rand1, rand2 = random.randint(0,9) , random.randint(0,9)

if rand2 > rand1:
    rand1,rand2 = rand2, rand1 

usrinput= input( ("What is difference of " + str(rand1) +  "-"+  str(rand2) + " : ") )

if (rand1- rand2) == int(usrinput) :
    print("answer is correct")
else:
    print("answer is false")