from langchain.tools import tool
import requests
import os

@tool
def search_news(query: str) -> str:
    """Search for recent news related to the input query."""
    url = "https://newsdata.io/api/1/news"
    
    params = {
        "q": query,
        "language": "en",
        "size": 3,
        "apikey": os.getenv("NEWS_API_KEY")
    }
    response = requests.get(url, params=params)
    
    articles = response.json().get("results", [])
    return "<article separator>".join([f"{a['title']} - {a['content']}" for a in articles])
