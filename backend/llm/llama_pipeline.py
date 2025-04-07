from transformers import pipeline
import torch

# Load the LLaMA model from Hugging Face
llama = pipeline(
    task="text-generation",
    model="huggyllama/llama-7b",  # Replace with smaller/faster model if needed
    torch_dtype=torch.float16,
    device=0  # GPU index; use 0 for first GPU
)

def generate_news_summary(query: str, context: str = ""):
    # Build the prompt cleanly
    prompt = "You are a personalized news assistant.\n\n"
    prompt += f"User query: {query}\n"

    if context:
        prompt += "Related content:\n" + context + "\n"

    prompt += "\nSummarize the most relevant news and explain why it matters:"

    # Generate response
    output = llama(prompt, max_new_tokens=512, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]
