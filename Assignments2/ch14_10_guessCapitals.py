import random
state= {
    "    Alabama    ":"    Montgomery    ",
    "    Alaska    ":"    Juneau    ",
    "    Arizona    ":"    Phoenix    ",
    "    Arkansas    ":"    Little Rock    ",
    "    California    ":"    Sacramento    ",
    "    Colorado    ":"    Denver    ",
    "    Connecticut    ":"    Hartford    ",
    "    Delaware    ":"    Dover    ",
    "    Florida    ":"    Tallahassee    ",
    "    Georgia    ":"    Atlanta    ",
    "    Hawaii    ":"    Honolulu    ",
    "    Idaho    ":"    Boise    ",
    "    Illinois    ":"    Springfield    ",
    "    Indiana    ":"    Indianapolis    ",
    "    Iowa    ":"    Des Moines    ",
    "    Kansas    ":"    Topeka    ",
    "    Kentucky    ":"    Frankfort    ",
    "    Louisiana    ":"    Baton Rouge    ",
    "    Maine    ":"    Augusta    ",
    "    Maryland    ":"    Annapolis    ",
    "    Massachusetts    ":"    Boston    ",
    "    Michigan    ":"    Lansing    ",
    "    Minnesota    ":"    Saint Paul    ",
    "    Mississippi    ":"    Jackson    ",
    "    Missouri    ":"    Jefferson City    ",
    "    Montana    ":"    Helena    ",
    "    Nebraska    ":"    Lincoln    ",
    "    Nevada    ":"    Carson City    ",
    "    New Hampshire    ":"    Concord    ",
    "    New Jersey    ":"    Trenton    ",
    "    New Mexico    ":"    Santa Fe    ",
    "    New York    ":"    Albany    ",
    "    North Carolina    ":"    Raleigh    ",
    "    North Dakota    ":"    Bismarck    ",
    "    Ohio    ":"    Columbus    ",
    "    Oklahoma    ":"    Oklahoma City    ",
    "    Oregon    ":"    Salem    ",
    "    Pennsylvania    ":"    Harrisburg    ",
    "    Rhode Island    ":"    Providence    ",
    "    South Carolina    ":"    Columbia    ",
    "    South Dakota    ":"    Pierre    ",
    "    Tennessee    ":"    Nashville    ",
    "    Texas    ":"    Austin    ",
    "    Utah    ":"    Salt Lake City    ",
    "    Vermont    ":"    Montpelier    ",
    "    Virginia    ":"    Richmond    ",
    "    Washington    ":"    Olympia    ",
    "    West Virginia    ":"    Charleston    ",
    "    Wisconsin    ":"    Madison    ",
    "    Wyoming    ":"    Cheyenne    "
}

state1={}
for i in state:
    state1[i.strip()] = state[i].strip()

print (state1)

i=0
correctcnt=0
rndstateset=set()
while i < 50:
    rndstate=random.choice(list(state1.keys()))
#     print(rndstate)
    if rndstate not in rndstateset:
#         print ( rndstateset )
        rndstateset.add(rndstate)
        inputstr= "What is capital of " + rndstate + ": ";
        answer=input(inputstr)
        if answer == state1[rndstate]:
            print("Correct answer!!")
            correctcnt += 1
        else:
            print("Incorrect answer!!")
        i +=1 
    else:
        continue

print("Total Correct answers are", str(correctcnt) , " out of ", str(i) )