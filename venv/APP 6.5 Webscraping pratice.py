import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#Maybe the website is blocking the python agent, set a fake browser in the headers
r=requests.get("https://pythonhow.com/example.html",headers = header)
c=r.content

print(c)

soup = BeautifulSoup(c,"html.parser")
print(soup)

all = soup.find_all("div",{"class":"cities"})
print(type(all))
print(all) #get the cities from soup

print(all[0].find_all("h2")) #第一个城市，伦敦

for i in [0,1,2]:
    print(all[i].find_all("h2")[0].text) #只有城市名，没有<h2>

for item in all:
    print(item.find_all("p")[0].text) #打印p