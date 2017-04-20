 # Open file for input
 
def countletters(infile):
   lettarr = 26 * [0]
   for ch in infile:
       if ch.isalpha():
           lettarr[ord(ch) - ord('a')] += 1
   return lettarr

infile = open("/Users/sharadagnihotri/Documents/GSU/R/rcodedata/grocery.csv", "r")
print("\n(2) Using read(number): ")
s1 = infile.readlines()
print(s1)
print(repr(s1))
infile.close()  # Close the input file

import urllib.request
infile = urllib.request.urlopen("http://www.gamespot.com/raw-data/")
s = infile.read().decode()

countarr = countletters(s.lower())

for i in range (len(countarr)):
    print("character " + chr(ord('a') + i) + " appears " + str(countarr[i])) 

infile.close()
    
    
