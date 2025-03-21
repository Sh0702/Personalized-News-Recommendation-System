import streamlit as st
from langchain.llms import OpenAI
import os
import subprocess
from dotenv import load_dotenv
import openai

# Install dependencies from requirements.txt
def install_requirements():
    if os.path.exists("requirements.txt"):
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
install_requirements()

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API Key from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API Key in the environment for langchain/openai to use
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    openai.api_key = openai_api_key

st.title('🦜🔗 Quickstart App')

def generate_response(input_text):
    try:
        llm = OpenAI(temperature=0.7)
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"Error generating response: {e}")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Will RCB win the IPL 2025?')
    submitted = st.form_submit_button('Submit')

    if not openai_api_key or not openai_api_key.startswith('sk-'):
        st.warning('Please enter a valid OpenAI API key in the .env file!', icon='⚠')

    if submitted and openai_api_key and openai_api_key.startswith('sk-'):
        generate_response(text)