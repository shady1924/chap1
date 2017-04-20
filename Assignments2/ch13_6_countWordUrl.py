import urllib.request

url = input("Enter a URL for a file: ").strip()
infile = urllib.request.urlopen(url)
str1= infile.read().decode()

wrdcnt=0 
for i in str1.split():
    wrdcnt = wrdcnt+1
#     print(i)

print("Word count from URL is: ",  str(wrdcnt) )