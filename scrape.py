import requests
import pandas as pd
from bs4 import BeautifulSoup

pnames=[]
prices=[]
desc=[]
rev=[]

for i in range (2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    
    r=requests.get(url)
#print(r.content)

    soup=BeautifulSoup(r.text,"lxml")

    names=soup.find_all("div",class_="KzDlHZ")
    for i in names:
        name=i.text
        pnames.append(name)

#print(pnames)


    pric=soup.find_all("div",class_="Nx9bqj _4b5DiR")
    for i in pric:
        price=i.text
        prices.append(price)

#print(prices)


    d=soup.find_all("ul",class_="G4BRas")
    for i in d:
        d1=i.text
        desc.append(d1)

#print(desc)

#print(soup)

            #np=soup.find("a",class_="_9QVEpD").get("href")
            #cnp="https://www.flipkart.com"+np
            #print(cnp)


#scraping data of the page


df=pd.DataFrame({'Product Name':pnames,"Description":desc,"Price":prices})
df.to_csv("flipkart_mobiles_under_50k.csv")