# 📰 Personalized News Recommendation System

A lightweight and scalable AI-powered system designed to generate personalized news articles based on user queries. Built with the goal of enhancing user experience through relevant, factual, and context-aware news generation.

🔗 **[App Link](https://personalized-news-recommendation-system.streamlit.app/)**

---

## 🚀 What We Have So Far

1. ✅ A **working prototype** using the **LLaMA 3B model** to generate news articles based on user-provided topics.
2. ✅ A **backend prompt template** that serves as the structured base for generating relevant content from LLM.

---

## ❗ Current Problems

1. ⚠️ **Limited content length** – The generated articles are short due to the small sample size provided by the external News API. This results in even shorter summaries.
2. ⚠️ **Data quality uncertainty** – We're unclear about:
   - Where to source rich, high-quality news datasets.
   - How to assess dataset adequacy for **RAG (Retrieval-Augmented Generation)** or **fine-tuning** purposes.

---

## 🧠 Proposed Solutions

1. 🔍 **Explore advanced architectures** that improve personalization and relevance, such as:
   - **RAG pipelines** with vector stores (e.g., Weaviate, FAISS).
   - Fine-tuned LLMs using topic-clustered and quality-controlled datasets.
   - ReAct-style prompting or Structured Chain of Thought (SCOT) for coherent generation.

2. 📦 Build a **custom data pipeline** to:
   - Aggregate diverse news sources (RSS feeds, APIs, scraping if permitted).
   - Preprocess and evaluate articles based on quality metrics.
   - Store embeddings for efficient retrieval.

---

## 📁 Project Structure (Proposed)


---

## 🛠 Tech Stack

- **Model:** [LLaMA-3B] (via Hugging Face)
- **Frontend:** Streamlit (lightweight UI)
- **Backend:** Python (FastAPI planned), Prompt Engineering
- **Vector Store (Planned):** Weaviate / FAISS
- **Data Sources (Planned):** NewsAPI, NewsData.io, RSS, custom web scrapers

---

## ✅ Next Steps

- [ ] Expand news data sources and build a structured dataset
- [ ] Set up vector database for document retrieval
- [ ] Implement personalization logic based on user preferences
- [ ] Evaluate article quality and summarization effectiveness

---

## 📌 Contributing

We welcome ideas, feedback, and collaboration! Please open an issue or submit a PR if you're interested.

---

## 📃 License

MIT License © 2025 Shreyas Srinivasan

