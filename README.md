# 📰 Personalized News Recommendation System

This project is an end-to-end AI-powered application that delivers personalized news content based on user queries and interests. It combines vector search, large language models, and modern full-stack development for a responsive and intelligent user experience.

---

## 🚀 Features

- 🔐 **User Authentication** using JWT (FastAPI + PostgreSQL)
- 🔎 **Vector Search** with Weaviate for private document retrieval
- 🌐 **Public News Fallback** using NewsAPI
- 🧠 **Text Generation** using Hugging Face's LLaMA (`huggyllama/llama-7b`)
- 💬 **Contextual Reasoning** via ReAct-style prompt engineering
- 🖥️ **React Frontend** for signup, login, and querying
- 🧠 **Auto-caching** of new content from public to private DB

---

## 🧱 Tech Stack

| Layer        | Tools & Libraries                                       |
|--------------|---------------------------------------------------------|
| Frontend     | React, Axios, React Router                              |
| Backend      | FastAPI, SQLAlchemy, PostgreSQL, JWT, Uvicorn           |
| LLM          | Hugging Face Transformers, `huggyllama/llama-7b`        |
| Retrieval    | Weaviate (Docker + `sentence-transformers`)             |
| Public News  | [NewsAPI.org](https://newsapi.org)                      |
| Infrastructure | Docker Compose (for Weaviate), `.env` for secrets    |

---

## 📂 Project Structure


