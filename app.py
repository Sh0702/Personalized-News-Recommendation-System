import streamlit as st
import logging
from datetime import datetime
from langchain_agent import agent, search_news

st.title("📰 ReAct-based Personalized News Generator")

user_query = st.text_input("What do you want news about?")

if st.button("Generate"):
    if user_query:
        with st.spinner("Thinking..."):
            try:
                result = agent.run(user_query)
                st.success(result)

                # Logging for manual observability
                with open("logs.csv", "a") as log:
                    log.write(f"{datetime.now()},{user_query},{result}\n")

            except Exception as e:
                st.error(f"Error: {e}")