import streamlit as st
import requests

st.set_page_config(page_title="LLM News Generator", layout="centered")

st.title("🧠 Personalized News Generator")

query = st.text_input("Enter your topic of interest:")
context = st.text_area("Optional context (paste related content here):", height=200)

if st.button("Generate Summary"):
    with st.spinner("Generating..."):
        res = requests.post("http://localhost:8000/generate", json={"query": query, "context": context})
        st.subheader("📄 Summary:")
        st.write(res.json()["response"])
