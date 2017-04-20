'''
Sharad: (Find the two highest scores) Write a program that prompts the user to enter the
number of students and each student’s score, and displays the highest and second highest
scores.
'''
##get number of students and set the variables
numofstudents=eval(input("print integer value for number of students:"))
i=0
highestscore=0
secondhigestscore=0
score=0
##loop through all students and get score for each one of them 
while i < numofstudents:
    score=eval(input("Enter the score for the student:"))
    #if current score is higher than previous stored score then change 
    if score > highestscore :
        secondhigestscore ,highestscore = highestscore, score
    i +=1

print("\n\nHighest score is: ", highestscore,"\tSecond HIghest score is:", secondhigestscore)