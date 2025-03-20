import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('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')

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