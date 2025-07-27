import os
from mistralai import Mistral 
from dotenv import load_dotenv 
import requests
from bs4 import BeautifulSoup
import json

# Load environment variables from .env file
load_dotenv()

# This function fetches news headlines from Google News RSS
def fetch_news():
    query = 'India'
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    news_items = []
    items = soup.find_all('item')

    for item in items:
        news = {
            'title': item.title.text,
            'link': item.link.text,
            'PubDate': item.pubDate.text,
            'description': item.description.text,
            'source': item.source.text if item.source else 'unknown source'
        }
        news_items.append(news)

    return news_items

# This function sends news data to Mistral AI and gets a summary
def summarize_news(news_list):
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)

    # Combine all news descriptions into a single text
    news_text = ""
    for news in news_list[:5]:  # You can change the number of articles here
        news_text += f"Title: {news['title']}\nDescription: {news['description']}\n\n"

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes recent news."
            },
            {
                "role": "user",
                "content": f"Summarize the following news articles:\n\n{news_text}"
            },
        ]
    )

    return chat_response.choices[0].message.content


news_data = fetch_news()

summary = summarize_news(news_data)

print("\n📰 SUMMARY FROM MISTRAL:\n")
print(summary)
