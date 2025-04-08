# from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import init_chat_model
from langchain import hub
from langchain_core.prompts import PromptTemplate

llm = init_chat_model("llama3-8b-8192", model_provider="groq")

# prompt_template = hub.pull("fernandoruiz/information_extraction_for_summarization")

prompt_template = PromptTemplate.from_template('''
    Please identify if the following news articles are related to this topic : {topic}.
    [Start news article]:
    {article}
    [End news article]
    Return the title, url and summary of the description only for the articles relevant to the topic, as a numbered list in the following format.
    
    Title: <title> \n
    Url: <url> \n
    Summary: <summary>
                                                                                             
    Answer in the most factual way possible. Only use content from the articles.

    If the articles are not related return : "Articles not relevant to topic"
    Answer:''')
