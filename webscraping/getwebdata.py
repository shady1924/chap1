import requests
import re
import time
from bs4 import BeautifulSoup

def getnumpages(soup):
    return len(soup.find("div",'paginator').find("select").find_all("option"))

def gettableheader(soup):
    return soup.find("table", id="myTable01").find("thead").find_all("tr")

def getdata(pagenumber):
    page = requests.get("http://www.trackitt.com/usa-immigration-trackers/h4-ead/page/" + str(pagenumber))   
    soup = BeautifulSoup(page.content, 'html.parser') 
    return soup

def main():
    numpages=0
    soup = getdata(1)
    numpages=getnumpages(soup) 
    tabheader=gettableheader(soup) 
    tabheader=repr(re.sub('(\n+| \n)','|',tabheader[0].get_text()) )
    tabheader=re.sub('\|+','|',tabheader)
    tabheader=tabheader[7:len(tabheader)-1]+"\n"
    print(tabheader) 
    outfile = open("/Users/sharadagnihotri/Downloads/EADVisas.csv", "a")
    outfile.write(tabheader)
#     for pages in range(1,numpages):
    for pages in range(1,numpages):        
        print("\n\n\n\#########################################################") 
#         rows,numpages = getdata(pages,numpages)
        soup = getdata(pages)
        rows = soup.find("table", id="myTable01").find("tbody").find_all("tr")        
        print (rows, str(numpages))        
        arr = []        
        for rw in range(0, len(rows) - 1):
            cells = rows[rw].find_all("td")
            arr.append([])
            for col in range (0, len(cells) - 1):
                arr[rw].append(cells[col].get_text().strip())
        
        for row in arr:
            for val in row:
#                 print(val, end='|')
                val=val+'|'
                outfile.write(val)
            outfile.write("\n")
#             print("")
        time.sleep(2)
    outfile.close()
main()
