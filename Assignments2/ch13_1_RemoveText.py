##  /Users/sharadagnihotri/Downloads/test.txt
infile=input("Enter a Filename:").strip()

fil=open(infile)
removetxt= input("Enter text to be removed:")

lin=fil.read()
linreplaced=lin.replace(removetxt,'')
# print(linreplaced)
fil.close()

outfile=open(infile,"w")
outfile.write(linreplaced)
outfile.close()
print("Done")