infile="/Users/sharadagnihotri/Downloads/test.txt"
fil=open(infile)
chrs=0
wrds=0
lines=0

lin=fil.readline()
while lin != "":
#     print(lin)
    lines=lines+1
    wrds= wrds + len(lin.split())
    for ch in lin:
        chrs=chrs+1
    lin=fil.readline()

print("chrs", str(chrs))
print("lines", str(lines))
print("wrds", str(wrds))

fil.close()