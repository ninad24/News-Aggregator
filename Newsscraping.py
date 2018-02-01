import urllib.request
import requests
from bs4 import BeautifulSoup


url = "https://www.inshorts.com/en/read"

response = requests.get(url)

ptext = response.content.decode('ascii', 'ignore')
soup = BeautifulSoup(ptext, 'lxml')
containers = soup.find_all("div", {"class": 'news-card-title news-right-box'})

headline = []

for each_div in containers:
    span = each_div.find_all('span')
    headline_text = str(span[0].text)
    headline.append(headline_text)
    #print(type(headline_text))
    

with open('headlines.txt', 'w') as w:
        w.write(str(headline))
        w.close()


with open('headlines.txt','r') as f:
    main_headline = f.read()

formatted = list(main_headline.strip('[').split(','))
print(formatted[5])