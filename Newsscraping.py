import urllib.request
import requests
import os
from bs4 import BeautifulSoup


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))



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
    
    

with open('headlines.txt', 'w') as w:
        w.write(str(headline))
        w.close()


with open('headlines.txt','r') as f:
    main_headline = f.read()

formatted = list(main_headline.strip('[').split(','))

final_out = []
for each_line in range(len(formatted)):
    new_string = formatted[each_line].replace("'", "")
    final_out.append(new_string)

notify("News Update", final_out[0])









