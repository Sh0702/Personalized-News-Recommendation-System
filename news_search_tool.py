from langchain.tools import tool
import requests
import streamlit as st
@tool
def search_news(query: str) -> str:
    """Search for recent news related to the input query."""
    url = "https://newsdata.io/api/1/news"
    
    params = {
        "q": query,
        "language": "en",
        "size": 3,
        "apikey": st.secrets["NEWS_API_KEY"]
    }
    response = requests.get(url, params=params)
    
    articles = response.json().get("results", [])
    return "\n<article separator>\n".join([f"{a['title']} - {a['description']}" for a in articles])
