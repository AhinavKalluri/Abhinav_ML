import requests
from bs4 import BeautifulSoup
import json

def fetch():
    query='India'
    url="https://news.google.com/rss/search?q="+query+'&hl=en-IN&gl=IN&ceid=IN:en'
    response=requests.get(url)
    # print(response.content)
    with open('news.txt','wb') as file:
        file.write(response.content)
fetch()
    