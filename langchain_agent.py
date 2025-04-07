# from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import init_chat_model
from langchain import hub
from dotenv import load_dotenv
import os

load_dotenv()
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

prompt_template = hub.pull("fernandoruiz/information_extraction_for_summarization")

# tools = [search_news]

# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True  # for debugging in terminal
# )

