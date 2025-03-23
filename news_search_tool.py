from langchain.tools import tool
import requests
import os

@tool
def search_news(query: str) -> str:
    """Search for recent news related to the input query."""
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 5,
        "apiKey": os.getenv("NEWS_API_KEY")
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    return "\n".join([f"{a['title']} - {a['description']}" for a in articles])
