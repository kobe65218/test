import requests
from bs4 import BeautifulSoup

html = requests.get("https://today.line.me/tw/v2/tab")
soup = BeautifulSoup(html.text,"lxml")
titles = soup.select("div.swiper-wrapper a")
titles_all = []
for title in titles:
    titles_all.append("https://today.line.me/" + title["href"])
print(titles_all)
#%%
import datetime

data = []
for title in titles_all:

    html = requests.get(title)
    soup = BeautifulSoup(html.text,"lxml")
    contexts = soup.select("a.articleCard.articleCard--horizontal")
    d = {}
    for context in contexts:
        try:
            title = context.select("div.articleCard-content div")[0].text.replace(" ","")
            source = context.select("div.articleCard-content span")[0].text.replace(" ","")
            print(title)
            print(source)
            url = "https://today.line.me/"+context["href"]
            print(url)
            time_html = requests.get(url)
            time_soup = BeautifulSoup(time_html.text, "lxml")
            time = time_soup.select("div.entityPublishInfo-meta span.entityPublishInfo-meta-info.text.text--f.text--secondary.text--regular")[0].text.replace(" ","")
            print(time)
            d["title"] = title
            d["source"] = source
            d["url"] = url
            d["time"] = title

        except :
            print("not context")
        data.append(d)


print(data)
