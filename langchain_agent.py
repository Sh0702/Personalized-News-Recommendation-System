# from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import init_chat_model
from langchain import hub
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

# prompt_template = hub.pull("fernandoruiz/information_extraction_for_summarization")

prompt_template = PromptTemplate.from_template('''
Please identify if the following news articles are related to this topic : {topic}.
    [Start news article]:
    {article}
    [End news article]
    If any articles are related to the topic, use only those articles to return a summary related to the given topic.
    Answer in the most factual way possible. Only use content from the articles.

    Limit the answer only to the summary of the relevant article if available. Do not mention about the articles given as input.
    If the articles are not related return : "Articles not relevant to topic"
    Answer:''')
