##  /Users/sharadagnihotri/Downloads/test.txt
infile=input("Enter a Filename:").strip()
infile=open(infile)

lines=infile.readline()

sum =0  
cnt=0 
for i in lines.split():
#     print(i)
    sum = sum+float(i)
    cnt = cnt +1

print("There are ", str(cnt) , " scores")
print("Total value is ", str(sum) )
print("Average value is ", str(sum/cnt) )
