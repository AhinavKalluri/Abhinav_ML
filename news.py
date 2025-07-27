import requests
from bs4 import BeautifulSoup
import json

def fetch():
    query='butter'
    url="https://news.google.com/rss/search?q="+query+'&hl=en-IN&gl=IN&ceid=IN:en'
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'xml')

    new_items=[]
    items=soup.find_all('item')
    for item in items:
        news= {
            'title':item.title.text,
            'link':item.link.text,
            'PubDate':item.pubDate.text,
            'description':item.description.text,
            'source':item.source.text if item.source else 'unknownsource'\
        }


        new_items.append(news)

        return new_items



news=fetch()

with open('news.json','w') as f:
    json.dump(news,f,indent=4)