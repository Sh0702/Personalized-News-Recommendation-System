from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from news_search_tool import search_news
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")  # deterministic
tools = [search_news]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # for debugging in terminal
)