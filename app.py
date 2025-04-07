import streamlit as st
import logging
from datetime import datetime
from langchain_agent import llm, prompt_template
from news_search_tool import search_news

st.title("📰 ReAct-based Personalized News Generator")

user_query = st.text_input("What do you want news about?")

if st.button("Generate"):
    if user_query:
        with st.spinner("Thinking..."):
            try:
                news_data = search_news(user_query)

                injected_prompt = prompt_template.invoke({"topic": user_query, "article": news_data})

                result = llm.invoke(injected_prompt)
                
                st.success(result.content)

                # Logging for manual observability
                with open("logs.csv", "a") as log:
                    log.write(f"{datetime.now()},{user_query},{result}\n")

            except Exception as e:
                st.error(f"Error: {e}")