import streamlit as st
from langchain.llms import OpenAI
import subprocess

# Install dependencies
def install_requirements():
    requirements = ["streamlit", "pandas", "numpy", "requests"]
    for package in requirements:
        subprocess.run(["pip", "install", package], check=True)

install_requirements()

st.title('🦜🔗 Quickstart App')

openai_api_key = st.text_input('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')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Will RCB win the IPL 2025?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)