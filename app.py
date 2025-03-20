import streamlit as st
from langchain.llms import OpenAI
import os
import subprocess
from dotenv import load_dotenv

# Install dependencies from requirements.txt
def install_requirements():
    if os.path.exists("requirements.txt"):
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
install_requirements()

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API Key from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title('🦜🔗 Quickstart App')

def generate_response(input_text):
    if openai_api_key and openai_api_key.startswith('sk-'):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))
    else:
        st.error("Invalid API Key! Please check your .env file.")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Will RCB win the IPL 2025?')
    submitted = st.form_submit_button('Submit')

    # Ensure API key is valid
    if not openai_api_key or not openai_api_key.startswith('sk-'):
        st.warning('Please enter a valid OpenAI API key in the .env file!', icon='⚠')

    if submitted and openai_api_key and openai_api_key.startswith('sk-'):
        generate_response(text)