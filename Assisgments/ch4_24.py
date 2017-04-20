'''
Sharad: Game: pick a card ) Write a program that simulates picking a card from a deck of
52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
'''
rank=eval(input("Enter the rank of the card: 1-13:"))
suit=input("Enter the suit of the card: (Clubs,Diamonds,Hearts,Spades):")
rankname=""
suitname=""
if rank ==1 :
    rankname="Ace"
elif rank ==2 :
    rankname="2"    
elif rank ==3 :
    rankname="3"
elif rank ==4 :
    rankname="4"
elif rank ==5 :
    rankname="5"
elif rank ==6 :
    rankname="6"
elif rank ==7 :
    rankname="7"
elif rank ==8 :
    rankname="8"
elif rank ==9 :
    rankname="9"
elif rank ==10 :
    rankname="10"
elif rank ==11 :
    rankname="Jack"
elif rank ==12 :
    rankname="Queen"
elif rank ==13 :
    rankname="King"
else:
    print("Invalid data")

if suit == "Clubs":
    suitname="Clubs"
elif suit == "Diamonds":
    suitname="Diamonds"
elif suit == "Hearts":
    suitname="Hearts"
elif suit == "Spades":
    suitname="Spades"
else :
    suitname="Invalid data"

if suitname !="Invalid data" and rank != "Invalid data" :
    print ("The card you picked is the ", rankname  , "of",  suitname)
else:
    print("Error in running program..possibly worng input values")