from fastapi import FastAPI, Body
from llm.llama_pipeline import generate_news_summary

app = FastAPI()

@app.post("/generate")
def generate(data: dict = Body(...)):
    query = data.get("query")
    context = data.get("context", "")
    result = generate_news_summary(query, context)
    return {"response": result}
