from langchain.tools import tool
import requests
import streamlit as st
@tool


def search_newsdata(query: str) -> str:
    """Search for recent news related to the input query."""
    url = "https://newsdata.io/api/1/news"
    
    params = {
        "q": query,
        "language": "en",
        "size": 5,
        "apikey": st.secrets["NEWS_DATA_KEY"]
    }
    response = requests.get(url, params=params)
    
    articles = response.json().get("results", [])
    return "\n<article separator>\n".join([f"Title:{a['title']} \\n URL:{a['link']} - {a['description']}" for a in articles])

def search_newsapi(query: str) -> str:
    """Search for recent news related to the input query."""
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "q": query,
        # "language": "en",
        # "size": 3,
        "pageSize":3,
        "apiKey":st.secrets("NEWS_API_KEY")
    }
    response = requests.get(url, params=params)
    
    articles = response.json().get("results", [])
    return "\n<article separator>\n".join([f"Title:{a['title']} \\n URL:{a['link']} - \\n {a['description']}" for a in articles])
